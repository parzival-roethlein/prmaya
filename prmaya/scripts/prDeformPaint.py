"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
modeling brushes for blendshape targets (similar to DPK_paintDeform.mel)
- average delta (any deformation)
    - preserve local surface details
    - stay "on model"
    - skin sliding
    - smooth/relax on compression/extension
- copy position
    - delete some deformation
    - blend between different meshes

FEATURES
- right click menus for "Set target" and "minDeltaLength" for extra options
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
  - It crashes Maya when flooding the same vertex selection twice (workaround is
    re-enter tool between each flood)
  - It is slow (MEL)
  - It is sometimes incredibly extra slow for no apparent reason (on linux)
- Is useful in addition to the maya sculpt brushes because:
  - missing "average delta"
  - they are buggy (erase delta not really deleting deltas, ...)
  - they do not support flooding vertex selection
  - they do not support viewport "isolate selected" mesh components
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

    Ui.isMayaInitialized = True


class Ui(pm.uitypes.Window):
    _TITLE = 'prDeformPaintUi_001'
    isMayaInitialized = False

    target = None
    operation = None

    def __new__(cls):
        """ delete possible old window and create new instance """
        if pm.window(cls._TITLE, exists=True):
            pm.deleteUI(cls._TITLE)
        self = pm.window(cls._TITLE, title=cls._TITLE)
        return pm.uitypes.Window.__new__(cls, self)

    def __init__(self, minDeltaLengthDefault=0.00001,
                 spaceDefault=om.MSpace.kObject):
        """create UI elements (layouts, buttons) and show window"""
        if not self.isMayaInitialized:
            initializeMaya()
        with pm.verticalLayout() as mainLayout:
            with pm.horizontalLayout() as targetLayout:
                pm.button(l='Set target:', c=pm.Callback(self.setTarget))
                # right click menu
                # - load orig
                # - create copy with current edit blendshape target disabled (->smooth/delete target)
                # - create copy of current
                self.target = pm.textField(en=False)
                existingDriver = mm.eval('whatIs "$prDP_driver"')
                if existingDriver != 'Unknown':
                    self.target.setText(mm.eval('$tempMelVar=$prDP_driver'))

            targetLayout.redistribute(0, 1)

            with pm.horizontalLayout() as operationLayout:
                self.operation = pm.radioButtonGrp(
                        label='Operation:',
                        labelArray2=['Average deltas', 'Copy'],
                        numberOfRadioButtons=2,
                        columnWidth3=[70, 120, 120],
                        columnAlign3=['left', 'left', 'left'],
                        changeCommand=pm.Callback(self.syncUiSettings))
                self.operation.setSelect(1)
            operationLayout.redistribute()

            with pm.frameLayout('settings', collapsable=True, collapse=True):
                with pm.verticalLayout() as settingsLayout:
                    with pm.horizontalLayout() as minDeltaLayout:
                        pm.text('minDeltaLength:')
                        self.minDeltaLength = pm.floatField(
                                precision=8, value=minDeltaLengthDefault,
                                changeCommand=pm.Callback(self.syncUiSettings))
                        # right click menu with presets: 0.1, 0.01, 0.001, ...
                    minDeltaLayout.redistribute(0, 1)

                    with pm.formLayout() as spacesLayout:
                        self.space = pm.optionMenu(
                                label='space',
                                changeCommand=pm.Callback(self.syncUiSettings))
                        spaces = defaultdict(list)
                        for attr in dir(om.MSpace):
                            if attr.startswith('__'):
                                continue
                            spaces[getattr(om.MSpace, attr)].append(attr)
                        self.space.addItems([str(v) for v in spaces.values()])
                        self.space.setSelect(spaceDefault+1)

                    spacesLayout.redistribute()
                settingsLayout.redistribute()

            with pm.horizontalLayout() as toolLayout:
                pm.button(label='Enter Tool', command=pm.Callback(self.enterTool))
                pm.button(label='Close', command=pm.Callback(self.close))
            toolLayout.redistribute()
        mainLayout.redistribute(0, 0, 0, 1)
        self.show()
        self.syncUiSettings()

    def syncUiSettings(self):
        mm.eval('$prDP_driver = "{}"'.format(self.target.getText()))
        mm.eval('$prDP_operation = {}'.format(self.operation.getSelect()-1))
        mm.eval('$prDP_minDeltaLength = {}'.format(self.minDeltaLength.getValue()))
        mm.eval('$prDP_space = {}'.format(self.space.getSelect()-1))

    def setTarget(self):
        selection = (pm.ls(sl=True, type=['transform', 'mesh']) or [''])[0]
        if pm.ls(selection, type='transform'):
            selection = (selection.getChildren() or [''])[0]
        self.target.setText(selection)
        self.syncUiSettings()

    def enterTool(self):
        mm.eval('prDeformPaint_initialize();')
        self.syncUiSettings()

    def close(self):
        pm.deleteUI(self._TITLE)


def getEditBlendshapeMultiplier(mesh, cacheValue=None):
    """get a multiplier to normalize the deformation (same amount no matter what
    the edited target and envelope values are)"""
    if cacheValue is not None:
        return cacheValue
    parent = mc.listRelatives(mesh, parent=True)
    children = mc.listRelatives(parent, children=True)
    orig = mc.ls(children, intermediateObjects=True)
    if not orig:
        return 1.0
    history = mc.listHistory(orig, future=True, groupLevels=True, pruneDagObjects=True)
    blendshape = (mc.ls(history, type='blendShape') or [None])[0]
    if not blendshape:
        return 1.0
    envelope = mc.getAttr('{}.envelope'.format(blendshape))
    targetIndex = mc.getAttr('{}.inputTarget[0].sculptTargetIndex'.format(blendshape))
    if targetIndex == -1:
        return 1.0
    weights = mc.getAttr('{}.weight'.format(blendshape))[0]
    weightIndices = mc.getAttr('{}.weight'.format(blendshape), multiIndices=True)
    weight = weights[weightIndices.index(targetIndex)]
    if weight < 0.001:
        raise ValueError('Edit blendshape weight is too small: {}'.format(weight))
    return 1.0/(weight*envelope)


def getMItMeshVertex(meshName):
    selection = om.MSelectionList()
    selection.add(meshName)
    return om.MItMeshVertex(selection.getDagPath(0))


def getVertexPositions(meshName, vertexIds=None, space=om.MSpace.kObject):
    """
    :param meshName: 'myMeshShape'
    :param vertexIds: [2, 3, ...] or all if None
    :param space: om.MSpace...
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


def copyPosition(driverMesh, drivenMesh, minDeltaLength, vertexIds, vertexWeights,
                 deformMultiplier=None, space=om.MSpace.kObject):
    """
    :param driverMesh: 'driverMeshName'
    :param drivenMesh: 'drivenMeshName'
    :param minDeltaLength: float
    :param vertexIds: [0, 1, ...]
    :param vertexWeights: [1.0, 0.5, ...]
    :param deformMultiplier: float or detect if None
    :param space: om.MSpace...
    :return: deformMultiplier
    """
    deformMultiplier = getEditBlendshapeMultiplier(drivenMesh, deformMultiplier)
    deltas = []
    for vertexId, weight, driverPosition, drivenPosition in izip(
            vertexIds,
            vertexWeights,
            getVertexPositions(driverMesh, vertexIds, space),
            getVertexPositions(drivenMesh, vertexIds, space)):
        deltas.append((driverPosition - drivenPosition) * weight * deformMultiplier)
    mc.prMovePointsCmd(drivenMesh, space, minDeltaLength, vertexIds, *deltas)


def averageDeltas(driverMesh, drivenMesh, minDeltaLength, vertexIds, vertexWeight,
                  multiplier=None, space=om.MSpace.kObject):
    """
    :param driverMesh: 'driverMeshName'
    :param drivenMesh: 'drivenMeshName'
    :param minDeltaLength: float
    :param vertexIds: [0, 1, ...]
    :param vertexWeight: [1.0, 0.5, ...]
    :param multiplier: float or detect if None
    :param space: om.MSpace...
    :return:
    """
    deformMultiplier = getEditBlendshapeMultiplier(drivenMesh, multiplier)

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
    for x, [vertexId, weight] in enumerate(izip(vertexIds, vertexWeight)):
        averageDelta = om.MVector()
        for neighborId in neighborIds[vertexId]:
            averageDelta += allDeltas[neighborId]
        averageDelta *= 1.0/len(neighborIds[vertexId])
        deltas.append(
            ((driverPositions[x] + averageDelta) - drivenPositions[x]) * weight * deformMultiplier
        )

    # do the deformation
    mc.prMovePointsCmd(drivenMesh, space, minDeltaLength, vertexIds, *deltas)

