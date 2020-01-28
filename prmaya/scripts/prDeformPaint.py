"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Modeling brushes, mainly for blendshape targets (similar to DPK_paintDeform.mel)
Operations:
  - Smooth delta: average the delta (vertex vector from target to painted mesh)
    with its neighbors. Reasons to do so:
      - preserve local surface details
      - stay "on model"
      - skin sliding
      - smooth/relax on compression/extension
  - Copy vertex: move painted mesh vertex to the target vertex position
  - Closest point: move the painted mesh vertex to the closest point on surface
    of the target mesh
  - Closest vertex: move the painted mesh vertex to the closest vertex of the
    target mesh
  - Average vertex: move a vertex to the average position of its neighbors. It's
    the same behavior as Mayas "Relax Tool" and "Average vertices"
Right click popup menus:
  - "Target: [...]" area to help with common target use cases
  - Operations area (Smooth delta, Copy vertex, ...) to toggle settings menuBar
Same deformation strength no matter what the edited blendshape target weight and
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
  - Partially unpredictable deformation when deforming multiple vertices,
    because the deltas are calculated just in time, while vertices are moving
- Is useful in addition to Mayas sculpt brushes because:
  - they do not support flooding vertex selection
  - they do not support viewport "isolate selected" mesh components
  - they are buggy (erase delta not really deleting deltas, ...)
  - missing "average delta" operation
- New operations: Closest point, Closest vertex

TODO
- (maybe) from edge-neighbor-vertices to face-neighbor-vertices ?
- save target with mc.fileInfo (maybe initialization has to be adjusted)
- merge UI into "tool settings" window with "paint scripts tool"
  (+selection context for target, so not tool switch is required)

"""

from itertools import izip
from collections import defaultdict

import maya.cmds as mc
import maya.api.OpenMaya as om
import pymel.core as pm
import maya.mel as mm


class Ui(pm.uitypes.Window):
    _TITLE = 'prDeformPaint_100'

    def __new__(cls):
        """ delete possible old window and create new instance """
        if pm.window(cls._TITLE, exists=True):
            pm.deleteUI(cls._TITLE)
        self = pm.window(cls._TITLE, title=cls._TITLE)
        return pm.uitypes.Window.__new__(cls, self)

    def __init__(self, operation=0, setTargetFromSelection=True,
                 menuBarVisible=True, space=om.MSpace.kObject,
                 minDeltaLength=0.00001, templateDuplicate=True,
                 visibleDuplicate=True):
        """
        :param operation: (int) 0=Smooth delta, 1=Copy vertex, 2=Closest point,
        3=Closest vertex, 4=Average vertex
        :param setTargetFromSelection: (bool) if there is no previous target
        stored (=first time running the UI in the maya instance) use the current
        selection
        :param space: (int) om.MSpace.k___
        :param menuBarVisible: (bool) settings menuBar visibility
        :param minDeltaLength: (float) deltas shorter than this are ignored
        :param templateDuplicate: (bool) duplicate.template=___
        :param visibleDuplicate: (bool) duplicate.visibility=___
        """
        initializeMaya()
        self.minDeltaLengthDefault = minDeltaLength
        with pm.verticalLayout() as mainLayout:
            with pm.menuBarLayout() as self.menuBar:
                self.space = pm.menu(label='Space', tearOff=True)
                pm.radioMenuItemCollection()
                self.spaces = []
                for name, value in self.getSpaceStrings(space):
                    self.spaces.append(
                        pm.menuItem(label=name, radioButton=value,
                                    command=pm.Callback(self.syncMelVariablesWithUi))
                    )

                pm.menu(label='Settings')
                self.templateDuplicate = pm.menuItem(
                    label='template DUPLICATE',
                    checkBox=templateDuplicate)
                self.visibleDuplicate = pm.menuItem(
                    label='visible DUPLICATE',
                    checkBox=visibleDuplicate)
                self.minDeltaLength = pm.menuItem(
                    label='minDeltaLength: {}'.format(minDeltaLength),
                    command=pm.Callback(self.setMinDeltaLengthDialog))
                pm.menu(label='Help')
                # pm.menuItem(label='TODO: demo video (vimeo)')
                # pm.menuItem(label='TODO: latest installer (...)')
                pm.menuItem(label='latest version (github)',
                            command=pm.Callback(self.getLatestVersion))
            self.menuBar.setMenuBarVisible(menuBarVisible)
            with pm.horizontalLayout() as targetLayout:
                pm.button(l='Target:', c=pm.Callback(self.setTargetFromSelection))
                self.target = pm.textField(en=False)
                variableTest = mm.eval('whatIs "$prDP_operation"')
                if variableTest != 'Unknown':
                    self.target.setText(mm.eval('$tempMelVar=$prDP_driver'))
            targetLayout.redistribute(0, 1)
            pm.popupMenu(parent=targetLayout, button=3)
            pm.menuItem(label='intermediate of selection',
                        c=pm.Callback(self.setTargetFromSelectionIntermediate))
            pm.menuItem(label='DUPLICATE of selection',
                        c=pm.Callback(self.setTargetFromDuplicateOfSelection))

            with pm.verticalLayout() as operationLayout:
                self.operation1 = pm.radioButtonGrp(
                        labelArray2=['Smooth delta', 'Copy vertex'],
                        numberOfRadioButtons=2,
                        columnWidth2=[110, 110],
                        columnAlign2=['left', 'left'],
                        changeCommand=pm.Callback(self.syncMelVariablesWithUi))
                self.operation1.setSelect(operation + 1)
                self.operation2 = pm.radioButtonGrp(
                    shareCollection=self.operation1,
                    labelArray2=['Closest point', 'Closest vertex'],
                    numberOfRadioButtons=2,
                    columnWidth2=[110, 110],
                    columnAlign2=['left', 'left'],
                    changeCommand=pm.Callback(self.syncMelVariablesWithUi))
                pm.separator()
                self.operation3 = pm.radioButtonGrp(
                    shareCollection=self.operation1,
                    label1='Average vertex',
                    numberOfRadioButtons=1,
                    columnWidth=[1, 110],
                    columnAlign=[1, 'left'],
                    changeCommand=pm.Callback(self.syncMelVariablesWithUi))
            operationLayout.redistribute(5, 5, 1, 5)

            pm.popupMenu(parent=operationLayout, button=3)
            pm.menuItem(label='toggle menuBar',
                        c=pm.Callback(self.toggleMenuBar))

            with pm.horizontalLayout() as toolLayout:
                pm.button(label='Enter Tool', command=pm.Callback(self.enterTool))
                pm.button(label='Close', command=pm.Callback(self.close))
            toolLayout.redistribute()
        mainLayout.redistribute(0, 0, 0, 1)

        if setTargetFromSelection and not self.target.getText():
            self.setTargetFromSelection()

        self.show()
        self.syncMelVariablesWithUi()

    def syncMelVariablesWithUi(self):
        mm.eval('$prDP_driver = "{}"'.format(self.getTarget()))
        mm.eval('$prDP_operation = {}'.format(self.getOperation()))
        mm.eval('$prDP_space = {}'.format(self.getSpace()))
        mm.eval('$prDP_minDeltaLength = {}'.format(self.getMinDeltaLength()))

    def enterTool(self):
        mm.eval('prDeformPaint_initialize();')
        self.syncMelVariablesWithUi()

    def close(self):
        pm.deleteUI(self._TITLE)

    def toggleMenuBar(self):
        self.menuBar.setMenuBarVisible(not self.menuBar.getMenuBarVisible())

    def getSpace(self):
        for x, space in enumerate(self.spaces):
            if pm.menuItem(space, q=True, radioButton=True):
                return x
        raise ValueError('Invalid space')

    @staticmethod
    def getSpaceStrings(defaultSpace):
        spaceDict = defaultdict(list)
        for attr in dir(om.MSpace):
            if attr.startswith('__'):
                continue
            spaceDict[getattr(om.MSpace, attr)].append(attr)
        spaces = []
        for x, space in enumerate([str(s) for s in spaceDict.values()]):
            space = space.replace("'", "").replace('[', '').replace(']', '')
            spaceValue = False
            if x == defaultSpace:
                space += ' (default)'
                spaceValue = True
            spaces.append([space, spaceValue])
        return spaces

    def getTarget(self):
        return self.target.getText()

    def setTarget(self, mayaObject):
        self.target.setText(mayaObject)
        self.syncMelVariablesWithUi()

    def setTargetFromSelection(self):
        self.setTarget((mc.ls(sl=True, type=['transform', 'mesh']) or [''])[0])

    def setTargetFromSelectionIntermediate(self):
        target = (mc.ls(sl=True, type=['transform', 'mesh']) or [''])[0]
        if mc.ls(target, type='mesh'):
            target = mc.listRelatives(target, parent=True)[0]
        if target:
            children = mc.listRelatives(target, children=True)
            target = (mc.ls(children, intermediateObjects=True) or [''])[-1]
        self.setTarget(target)

    def setTargetFromDuplicateOfSelection(self):
        selection = (mc.ls(sl=True, type=['transform', 'mesh']) or [None])[0]
        if not selection:
            raise ValueError('Nothing selected to duplicate')
        duplicate = mc.duplicate(selection)[0]
        duplicate = mc.rename(duplicate, duplicate+'_prDP_DUPLICATE')
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
        templateValue = pm.menuItem(self.templateDuplicate, q=True, checkBox=True)
        mc.setAttr('{}.template'.format(duplicate), templateValue)
        visibilityValue = pm.menuItem(self.visibleDuplicate, q=True, checkBox=True)
        mc.setAttr('{}.visibility'.format(duplicate), visibilityValue)
        self.setTarget(duplicate)
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

    def setMinDeltaLengthDialog(self):
        result = pm.promptDialog(
            title='minDeltaLength',
            message='Enter new minimum delta length value:\n'
                    'default = "{0}"'.format(self.minDeltaLengthDefault),
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel',
            text=self.getMinDeltaLength())
        if result == 'OK':
            self.setMinDeltaLength(pm.promptDialog(query=True, text=True))

    def setMinDeltaLength(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError('Given length must be a number: "{}"'.format(value))
        if value < 0.0:
            raise ValueError('Given length must be greater or equal to 0.0')
        self.minDeltaLength.setLabel('minDeltaLength: {}'.format(value))
        self.syncMelVariablesWithUi()

    def getMinDeltaLength(self):
        label = self.minDeltaLength.getLabel()
        value = float(label.replace('minDeltaLength: ', ''))
        return value

    @staticmethod
    def getLatestVersion():
        mc.launch(web="https://github.com/parzival-roethlein/prmaya")


def initializeMaya(prMovePointsCmdPath='prMovePointsCmd',
                   prDeformPaintBrushPath='prDeformPaintBrush.mel'):
    """
    load the required plugin and mel script

    manual usage example:
    prDeformPaint.initializeMaya('/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py',
                                 '/home/prthlein/private/code/prmaya/prmaya/scripts/prDeformPaintBrush.mel')

    :param prMovePointsCmdPath: only required if it's not in a MAYA_PLUG_IN_PATH
    :param prDeformPaintBrushPath: only required if it's not in a MAYA_SCRIPT_PATH
    :return:
    """
    if not mc.pluginInfo(prMovePointsCmdPath, q=True, loaded=True):
        mc.loadPlugin(prMovePointsCmdPath)

    if mm.eval('whatIs "$prDP_operation"') == 'Unknown':
        mm.eval('source "{}";'.format(prDeformPaintBrushPath))


def reinitializeMaya(*args, **kwargs):
    """reload plugin and mel script"""
    initializeMaya(*args, **kwargs)
    mc.unloadPlugin('prMovePointsCmd')
    mm.eval('rehash;')
    mm.eval('source prDeformPaintBrush;')
    initializeMaya(*args, **kwargs)


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

