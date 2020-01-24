"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
modeling brushes, mainly for blendshape targets (similar to DPK_paintDeform.mel)
- Smooth delta: average the vertex vector (from target to current mesh)
  with the neighboring vertex vectors, to:
    - preserve local surface details
    - stay "on model"
    - skin sliding
    - smooth/relax on compression/extension
- average vertex: set the vertex position to the average position of its neighbors
- copy position
    - delete some deformation
    - blend between different meshes

FEATURES
- right click popup menus for "Set target", "minDeltaLength", "space"
- minDeltaLenght: ignores deformation vectors shorter than this value
- space: object and worldspace are the most common
- Same deformation strength no matter what the edited blendshape target weight and
  envelope values are

USAGE
import prDeformPaint
prDeformPaint.Ui()

INSTALLATION
Your Maya environment has to be able to access the folders of:
(MAYA_PLUG_IN_PATH:)
.../prmaya/plugins/prMovePointsCmd.py
(MAYA_SCRIPT_PATH:)
.../prmaya/scripts/prDeformPaintBrush.mel
.../prmaya/scripts/prDeformPaint.py

MOTIVATION
- Replace DPK_paintDeform.mel, because:
  - It permanently breaks meshes that are in edit blendshape target mode
  - It crashes Maya when flooding twice in a row (workaround is re-enter tool
    between each flood)
  - It is slow (MEL)
  - It is sometimes extra slow for no apparent reason
- Is useful in addition to the maya sculpt brushes because:
  - missing "average delta"
  - they are buggy (erase delta not really deleting deltas, ...)
  - they do not support flooding vertex selection
  - they do not support viewport "isolate selected" mesh components

TODO
- settings as menubar
- merge UI into "tool settings" window with "paint scripts tool"

TODO (maybe)
- optional move to closestPoint after each deformation:
  - support maya "live object"
  - custom closest point target
  - currently sculpted mesh as closestPoint ("preserve volume")
"""

from itertools import izip
from collections import defaultdict

import maya.cmds as mc
import maya.api.OpenMaya as om
import pymel.core as pm
import maya.mel as mm


def reinitializeMaya(*args, **kwargs):
    """reload plugin and mel script"""
    initializeMaya(*args, **kwargs)
    mc.unloadPlugin('prMovePointsCmd.py')
    mm.eval('source prDeformPaintBrush;')
    mm.eval('rehash;')
    initializeMaya(*args, **kwargs)


def initializeMaya(prMovePointsCmdPath=None,
                   prDeformPaintBrushPath=None):
    """
    load the required plugin and mel script

    manual usage example:
    prDeformPaint.initializeMaya('/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py',
                                 '/home/prthlein/private/code/prmaya/prmaya/scripts/prDeformPaintBrush.mel')

    :param prMovePointsCmdPath: only required if it's not in a MAYA_PLUG_IN_PATH
    :param prDeformPaintBrushPath: only required if it's not in a MAYA_SCRIPT_PATH
    :return:
    """
    prMovePointsCmdPath = prMovePointsCmdPath or 'prMovePointsCmd.py'
    if not mc.pluginInfo(prMovePointsCmdPath, q=True, loaded=True):
        mc.loadPlugin(prMovePointsCmdPath)

    if mm.eval('whatIs "$prDP_operation"') == 'Unknown':
        prDeformPaintBrushPath = prDeformPaintBrushPath or 'prDeformPaintBrush.mel'
        mm.eval('source "{}";'.format(prDeformPaintBrushPath))


class Ui(pm.uitypes.Window):
    _TITLE = 'prDeformPaintUi_001'

    target = None
    operation = None

    def __new__(cls):
        """ delete possible old window and create new instance """
        if pm.window(cls._TITLE, exists=True):
            pm.deleteUI(cls._TITLE)
        self = pm.window(cls._TITLE, title=cls._TITLE)
        return pm.uitypes.Window.__new__(cls, self)

    def __init__(self, defaultOperation=0,
                 setBaseFromSelection=True,
                 minDeltaLengthDefault=0.00001,
                 spaceDefault=om.MSpace.kObject,
                 duplicateTemplate=True,
                 duplicateVisiblity=True):
        """
        :param defaultOperation: int. 0=Smooth delta, 1=average vertex, ..
        :param setBaseFromSelection: set selection as base, if there was no
                                     previous base stored
        :param minDeltaLengthDefault: deltas shorter than this are ignored
        :param spaceDefault:om.MSpace.k___
        :param duplicateTemplate: set duplicate to template
        :param duplicateVisiblity: hide duplicate
        """
        initializeMaya()
        with pm.verticalLayout() as mainLayout:
            with pm.horizontalLayout() as baseLayout:
                pm.button(l='Base:', c=pm.Callback(self.setBaseFromSelection))
                self.base = pm.textField(en=False)
                variableTest = mm.eval('whatIs "$prDP_operation"')
                if variableTest != 'Unknown':
                    self.base.setText(mm.eval('$tempMelVar=$prDP_driver'))
            baseLayout.redistribute(0, 1)
            pm.popupMenu(parent=baseLayout, button=3)
            pm.menuItem(label='Intermediate of selection',
                        c=pm.Callback(self.setBaseFromSelectionIntermediate))
            pm.menuItem(label='Duplicate of selected',
                        c=pm.Callback(self.setBaseFromDuplicateOfSelection))

            with pm.verticalLayout() as operationLayout:
                self.operation1 = pm.radioButtonGrp(
                        labelArray2=['Smooth delta', 'Copy vertex'],
                        numberOfRadioButtons=2,
                        columnWidth2=[110, 110],
                        columnAlign2=['left', 'left'],
                        changeCommand=pm.Callback(self.syncUiSettings))
                self.operation1.setSelect(defaultOperation + 1)
                self.operation2 = pm.radioButtonGrp(
                    shareCollection=self.operation1,
                    labelArray2=['Closest point', 'Closest vertex'],
                    numberOfRadioButtons=2,
                    columnWidth2=[110, 110],
                    columnAlign2=['left', 'left'],
                    changeCommand=pm.Callback(self.syncUiSettings))
                pm.separator()
                self.operation3 = pm.radioButtonGrp(
                    shareCollection=self.operation1,
                    label1='Average vertex',
                    numberOfRadioButtons=1,
                    columnWidth=[1, 110],
                    columnAlign=[1, 'left'],
                    changeCommand=pm.Callback(self.syncUiSettings))
            operationLayout.redistribute(5, 5, 1, 5)

            pm.frameLayout('settings', collapsable=True, collapse=True)
            with pm.verticalLayout() as settingsLayout:

                with pm.formLayout() as spacesLayout:
                    self.space = pm.optionMenu(
                            label='space:',
                            changeCommand=pm.Callback(self.syncUiSettings))
                    spaces = defaultdict(list)
                    for attr in dir(om.MSpace):
                        if attr.startswith('__'):
                            continue
                        spaces[getattr(om.MSpace, attr)].append(attr)
                    self.space.addItems([str(v) for v in spaces.values()])
                    self.space.setSelect(spaceDefault+1)
                spacesLayout.redistribute()
                pm.popupMenu(parent=spacesLayout, button=3)
                pm.menuItem(label='(default:) {}'.format(spaces[spaceDefault]),
                            c=pm.Callback(self.setSpace, spaceDefault))

                with pm.horizontalLayout() as minDeltaLayout:
                    pm.text('minDeltaLength:')
                    self.minDeltaLength = pm.floatField(
                            precision=8, value=minDeltaLengthDefault,
                            changeCommand=pm.Callback(self.syncUiSettings))
                minDeltaLayout.redistribute(0, 1)
                pm.popupMenu(parent=minDeltaLayout, button=3)
                pm.menuItem(
                    label='(default:) {}'.format(str(minDeltaLengthDefault)),
                    c=pm.Callback(self.setMinDeltaLength, minDeltaLengthDefault)
                )
                pm.menuItem(divider=True)
                value = 0.1
                for x in range(8):
                    label = '{:.8f}'.format(value)
                    label = label[:label.rfind('1') + 1]
                    if value < 0.0001:
                        label = '{} ({})'.format(label, value)
                    pm.menuItem(label=label,
                                c=pm.Callback(self.setMinDeltaLength, value))
                    value *= 0.1

                self.duplicateTemplate = pm.checkBoxGrp(
                        label='duplicate.template:',
                        value1=duplicateTemplate,
                        columnWidth2=[100, 100], columnAlign2=['right', 'left'])
                self.duplicateVisibility = pm.checkBoxGrp(
                        label='duplicate.visibility:',
                        value1=duplicateVisiblity,
                        columnWidth2=[100, 100], columnAlign2=['right', 'left'])

            settingsLayout.redistribute()
            with pm.horizontalLayout() as toolLayout:
                pm.button(label='Enter Tool', command=pm.Callback(self.enterTool))
                pm.button(label='Close', command=pm.Callback(self.close))
            toolLayout.redistribute()
        mainLayout.redistribute(0, 0, 0, 1)

        if setBaseFromSelection and not self.base.getText():
            self.setBaseFromSelection()

        self.show()
        self.syncUiSettings()

    def syncUiSettings(self):
        print('syncUiSettings')
        mm.eval('$prDP_driver = "{}"'.format(self.base.getText()))
        mm.eval('$prDP_operation = {}'.format(self.getOperation()))
        mm.eval('$prDP_space = {}'.format(self.space.getSelect()-1))
        mm.eval('$prDP_minDeltaLength = {}'.format(self.minDeltaLength.getValue()))

    def enterTool(self):
        mm.eval('prDeformPaint_initialize();')
        self.syncUiSettings()

    def close(self):
        pm.deleteUI(self._TITLE)

    def setBase(self, mayaObject):
        self.base.setText(mayaObject)
        self.syncUiSettings()

    def setBaseFromSelection(self):
        self.setBase((mc.ls(sl=True, type=['transform', 'mesh']) or [''])[0])

    def setBaseFromSelectionIntermediate(self):
        base = (mc.ls(sl=True, type=['transform', 'mesh']) or [''])[0]
        if mc.ls(base, type='mesh'):
            base = mc.listRelatives(base, parent=True)[0]
        children = mc.listRelatives(base, children=True)
        self.setBase((mc.ls(children, intermediateObjects=True) or [''])[-1])

    def setBaseFromDuplicateOfSelection(self):
        selection = (mc.ls(sl=True, type=['transform', 'mesh']) or [None])[0]
        if not selection:
            raise ValueError('Nothing selected to duplicate')
        duplicate = mc.duplicate(selection)[0]
        duplicate = mc.rename(duplicate, duplicate+'_DELETE')
        for attr in ['t', 'tx', 'ty', 'tz',
                     'r', 'rx', 'ry', 'rz',
                     's', 'sx', 'sy', 'sz',
                     'v', 'template']:
            fullAttr = '{}.{}'.format(duplicate, attr)
            mc.setAttr(fullAttr, lock=False)
            for attrInput in mc.listConnections(fullAttr, source=True,
                                                destination=False, p=True) or []:
                mc.disconnectAttr(attrInput, fullAttr)

        if mc.listRelatives(duplicate, parent=True):
            mc.parent(duplicate, world=True)
        mc.setAttr('{}.template'.format(duplicate), self.duplicateTemplate.getValue1())
        mc.setAttr('{}.visibility'.format(duplicate), self.duplicateVisibility.getValue1())
        self.setBase(duplicate)
        mc.select(selection)

    def getOperation(self):
        firstRow = self.operation1.getSelect()
        if firstRow != 0:
            return firstRow - 1
        secondRow = self.operation2.getSelect()
        if secondRow != 0:
            return secondRow + 1
        thirdRow = self.operation3.getSelect()
        if thirdRow != 0:
            return thirdRow + 3
        raise ValueError('Unknown operation')

    def setSpace(self, value):
        """because setSelect does not trigger the changeCommand"""
        self.space.setSelect(value+1)
        self.syncUiSettings()

    def setMinDeltaLength(self, value):
        """because pm.popupMenu does not have a changeCommand flag"""
        self.minDeltaLength.setValue(value)
        self.syncUiSettings()


def getBlendshapeFromMesh(mesh):
    """
    :param mesh: mesh or transform (with mesh child)
    :return:
    """
    if mc.ls(mesh, type='transform'):
        transform = mesh
    else:
        transform = mc.listRelatives(mesh, parent=True)
    children = mc.listRelatives(transform, children=True)
    orig = mc.ls(children, intermediateObjects=True)
    if not orig:
        return None
    history = mc.listHistory(orig, future=True, groupLevels=True, pruneDagObjects=True)
    return (mc.ls(history, type='blendShape') or [None])[0]


def getEditBlendshapeMultiplier(mesh, cacheValue=None):
    """
    get a multiplier to normalize the deformation (same deformation strength,
    no matter what the edited target and envelope values are)
    :param mesh: mesh or transform (with mesh child)
    :param cacheValue:
    :return:
    """
    if cacheValue is not None:
        return cacheValue
    blendshape = getBlendshapeFromMesh(mesh)
    if not blendshape:
        return 1.0
    targetIndex = mc.getAttr('{}.inputTarget[0].sculptTargetIndex'.format(blendshape))
    if targetIndex == -1:
        return 1.0
    weights = mc.getAttr('{}.weight'.format(blendshape))[0]
    weightIndices = mc.getAttr('{}.weight'.format(blendshape), multiIndices=True)
    weight = weights[weightIndices.index(targetIndex)]
    if weight < 0.0001:
        raise ValueError('Edit blendshape weight is too small: {}'.format(weight))
    envelope = mc.getAttr('{}.envelope'.format(blendshape))
    if envelope < 0.0001:
        raise ValueError('Envelope is too small: {}'.format(envelope))
    return 1.0/(weight*envelope)


def getMItMeshVertex(meshName):
    if not mc.objExists(meshName):
        raise ValueError('object does not exist: "{}"'.format(meshName))
    selection = om.MSelectionList()
    selection.add(meshName)
    return om.MItMeshVertex(selection.getDagPath(0))


def getVertexPositions(meshName, vertexIds=None, space=om.MSpace.kObject):
    """
    :param meshName: 'myMeshShape'
    :param vertexIds: [2, 3, ...] or all if None
    :param space: om.MSpace.k___
    :return: MPointArray
    """
    vertexIter = getMItMeshVertex(meshName)
    if vertexIds is None:
        vertexIds = range(len(vertexIter))
    vertexPositions = om.MPointArray()
    for vertexId in vertexIds:
        vertexIter.setIndex(vertexId)
        vertexPositions.append(vertexIter.position(space))
    return vertexPositions


def copyVertex(driverMesh, drivenMesh, minDeltaLength, vertexIds, vertexWeights,
               multiplier=None, space=om.MSpace.kObject):
    """
    copy vertex position from driver to driven
    :param driverMesh: 'driverMeshName'
    :param drivenMesh: 'drivenMeshName'
    :param minDeltaLength: float
    :param vertexIds: [0, 1, ...]
    :param vertexWeights: [1.0, 0.5, ...]
    :param multiplier: float or detect if None
    :param space: om.MSpace.k___
    :return:
    """
    multiplier = getEditBlendshapeMultiplier(drivenMesh, multiplier)
    deltas = []
    for vertexId, weight, driverPosition, drivenPosition in izip(
            vertexIds,
            vertexWeights,
            getVertexPositions(driverMesh, vertexIds, space),
            getVertexPositions(drivenMesh, vertexIds, space)):
        deltas.append((driverPosition - drivenPosition) * weight * multiplier)
    mc.prMovePointsCmd(drivenMesh, space, minDeltaLength, vertexIds, *deltas)


def smoothDelta(driverMesh, drivenMesh, minDeltaLength, vertexIds, vertexWeights,
                multiplier=None, space=om.MSpace.kObject):
    """
    average the difference vector (=delta) between the driverMesh and drivenMesh
    vertices with their neighbors deltas
    :param driverMesh: 'driverMeshName'
    :param drivenMesh: 'drivenMeshName'
    :param minDeltaLength: float
    :param vertexIds: [0, 1, ...]
    :param vertexWeights: [1.0, 0.5, ...]
    :param multiplier: float or detect if None
    :param space: om.MSpace.k___
    :return:
    """
    multiplier = getEditBlendshapeMultiplier(drivenMesh, multiplier)

    # get all relevant vertex ids (add neighbors)
    neighborIds = {}
    drivenIter = getMItMeshVertex(drivenMesh)
    allVertexIds = list(vertexIds)
    for vertexId in vertexIds:
        drivenIter.setIndex(vertexId)
        neighborIds[vertexId] = drivenIter.getConnectedVertices()
        for neighbor in neighborIds[vertexId]:
            if neighbor not in allVertexIds:
                allVertexIds.append(neighbor)

    # get all positions and deltas of interest
    driverPositions = om.MPointArray()
    driverIter = getMItMeshVertex(driverMesh)
    drivenPositions = om.MPointArray()
    drivenIter = getMItMeshVertex(drivenMesh)
    allDeltas = {}
    for vertexId in allVertexIds:
        driverIter.setIndex(vertexId)
        drivenIter.setIndex(vertexId)
        driverPosition = driverIter.position(space)
        drivenPosition = drivenIter.position(space)
        driverPositions.append(driverPosition)
        drivenPositions.append(drivenPosition)
        allDeltas[vertexId] = drivenPosition - driverPosition

    # calculate deformation deltas
    deltas = []
    for x, [vertexId, weight] in enumerate(izip(vertexIds, vertexWeights)):
        averageDelta = om.MVector()
        for neighborId in neighborIds[vertexId]:
            averageDelta += allDeltas[neighborId]
        averageDelta /= len(neighborIds[vertexId])
        deltas.append(
            ((driverPositions[x] + averageDelta) - drivenPositions[x]) * weight * multiplier
        )

    # do the deformation
    mc.prMovePointsCmd(drivenMesh, space, minDeltaLength, vertexIds, *deltas)


def averageVertex(drivenMesh, minDeltaLength, vertexIds, vertexWeights,
                  multiplier=None, space=om.MSpace.kObject):
    """
    average ("relax") a vertex, relative to its neighbors.
    this operation is not using the "target" / driver mesh.
    :param drivenMesh: 'drivenMeshName'
    :param minDeltaLength: float
    :param vertexIds: [0, 1, ...]
    :param vertexWeights: [1.0, 0.5, ...]
    :param multiplier: float or detect if None
    :param space: om.MSpace.k___
    :return:
    """
    multiplier = getEditBlendshapeMultiplier(drivenMesh, multiplier)
    drivenIter = getMItMeshVertex(drivenMesh)

    # get all relevant vertex ids and neighbor vertex ids
    allVertexIds = list(vertexIds)
    allNeighborIds = []
    for vertexId in vertexIds:
        drivenIter.setIndex(vertexId)
        neighborIds = drivenIter.getConnectedVertices()
        allNeighborIds.append(neighborIds)
        for neighbor in neighborIds:
            if neighbor not in allVertexIds:
                allVertexIds.append(neighbor)

    # get all relevant positions (as vector for calculations)
    allPositions = om.MVectorArray()
    for vertexId in allVertexIds:
        drivenIter.setIndex(vertexId)
        allPositions.append(drivenIter.position(space))

    # calculate deltas
    deltas = []
    for vertexId, vertexWeight in izip(vertexIds, vertexWeights):
        drivenIter.setIndex(vertexId)
        averagePosition = om.MVector()
        neighborsIds = allNeighborIds[allVertexIds.index(vertexId)]
        for neighborId in neighborsIds:
            averagePosition += allPositions[allVertexIds.index(neighborId)]
        averagePosition /= len(neighborsIds)
        deltas.append(
            (averagePosition - allPositions[allVertexIds.index(vertexId)]) * vertexWeight * multiplier
        )

    # do the deformation
    mc.prMovePointsCmd(drivenMesh, space, minDeltaLength, vertexIds, *deltas)


def closestPoint(driverMesh, drivenMesh, minDeltaLength, vertexIds, vertexWeights,
                 multiplier=None, space=om.MSpace.kObject, closestVertex=False):
    """
    move the drivenMesh vertex to the closestPoint or closestVertex on the
    driverMesh
    :param driverMesh: 'driverMeshName'
    :param drivenMesh: 'drivenMeshName'
    :param minDeltaLength: float
    :param vertexIds: [0, 1, ...]
    :param vertexWeights: [1.0, 0.5, ...]
    :param multiplier: float or detect if None
    :param space: om.MSpace.k___
    :param closestVertex: bool
    :return:
    """
    multiplier = getEditBlendshapeMultiplier(drivenMesh, multiplier)

    drivenIter = getMItMeshVertex(drivenMesh)
    selection = om.MSelectionList()
    selection.add(driverMesh)
    meshFn = om.MFnMesh(selection.getDagPath(0))

    deltas = []
    for vertexId, vertexWeight in izip(vertexIds, vertexWeights):
        drivenIter.setIndex(vertexId)
        startPosition = drivenIter.position(space)
        targetPosition, polygonId = meshFn.getClosestPoint(startPosition, space)
        if closestVertex:
            shortestDistance = None
            for polyVtxId in meshFn.getPolygonVertices(polygonId):
                polyVtxPosition = meshFn.getPoint(polyVtxId, space)
                distance = (polyVtxPosition - startPosition).length()
                if shortestDistance is None or distance < shortestDistance:
                    shortestDistance = distance
                    targetPosition = polyVtxPosition
        deltas.append((targetPosition - startPosition) * vertexWeight * multiplier)

    # do the deformation
    mc.prMovePointsCmd(drivenMesh, space, minDeltaLength, vertexIds, *deltas)

