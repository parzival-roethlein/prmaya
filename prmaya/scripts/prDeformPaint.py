"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
modeling brushes for blendshape targets (similar to DPK_paintDeform.mel)

USAGE
import prDeformPaint
prDeformPaint.Ui()

INSTALLATION
Your Maya environment has to be able to access:
(MAYA_PLUG_IN_PATH:)
prmaya/plugins/prMovePointsCmd.py
(MAYA_SCRIPT_PATH:)
prmaya/scripts/prDeformPaint.mel
prmaya/scripts/prDeformPaint.py

FEATURES
- average delta operation that including all deformation. This helps to preserve
  local surface shapes (staying "on model")
- Same deformation strength no matter what the blendshape envelope and target
  weight is

MOTIVATION
- Replace DPK_paintDeform.mel, because:
  - It permanently breaks meshes that are in edit blendshape target mode
  - It crashes Maya when flooding the same vertex selection twice
  - It is slow (MEL)
- Is useful in addition to the maya sculpt brushes because:
  - missing "average delta"
  - they are buggy (erase delta not really deleting deltas, ...)
  - they do not support flooding vertex selection
  - they do not support viewport "isolate selected" mesh components
"""

from itertools import izip

import maya.cmds as mc
import maya.api.OpenMaya as om
import pymel.core as pm
import maya.mel as mm


def reinitializeMaya(*args, **kwargs):
    initializeMaya(*args, **kwargs)
    mc.unloadPlugin('prMovePointsCmd.py')
    initializeMaya(*args, **kwargs)
    mm.eval('rehash;')


def initializeMaya(prMovePointsCmdPath=None, prDeformPaintBrushPath=None):
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

    def __init__(self):
        """create UI elements (layouts, buttons) and show window"""
        if not self.isMayaInitialized:
            initializeMaya()
        with pm.verticalLayout() as mainLayout:
            with pm.horizontalLayout() as targetLayout:
                pm.button(l='Set target:', c=pm.Callback(self.setTarget))
                # right click menu
                # load orig
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

            with pm.horizontalLayout() as toolLayout:
                pm.button(label='Enter Tool', command=pm.Callback(self.enterTool))
                pm.button(label='Close', command=pm.Callback(self.close))
            toolLayout.redistribute()

        mainLayout.redistribute()
        self.show()
        self.syncUiSettings()

    def syncUiSettings(self):
        mm.eval('$prDP_driver = "{}"'.format(self.target.getText()))
        mm.eval('$prDP_operation = {}'.format(self.operation.getSelect()-1))

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


def getMItMeshVertex(mesh):
    selection = om.MSelectionList()
    selection.add(mesh)
    return om.MItMeshVertex(selection.getDagPath(0))


def getMFnMesh(mesh):
    selection = om.MSelectionList()
    selection.add(mesh)
    return om.MFnMesh(selection.getDagPath(0))


def getEditBlendshapeMultiplier(mesh, cacheValue=None):
    """get a deformation multiplier that allows for the deformation to be the
    same, no matter what the edited target and envelope values are"""
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
        return 1.0 / envelope
    weights = mc.getAttr('{}.weight'.format(blendshape))[0]
    weightIndices = mc.getAttr('{}.weight'.format(blendshape), multiIndices=True)
    weight = weights[weightIndices.index(targetIndex)]
    if weight < 0.001:
        raise ValueError('Edit blendshape weight is too small: {}'.format(weight))
    return 1.0/(weight*envelope)


def getVertexPositions(vertexIter, vertexIds, space=om.MSpace.kObject):
    """
    get vertex positions as MPointArray
    :param vertexIter:
    :param vertexIds:
    :param space:
    :return: MPointArray
    """
    vertexPositions = om.MPointArray()
    for vertexId in vertexIds:
        vertexIter.setIndex(vertexId)
        vertexPositions.append(vertexIter.position(space=space))
    return vertexPositions


def copyPosition(driverMesh, drivenMesh, vertexIds, vertexWeights,
                 deformMultiplier=None, space=om.MSpace.kObject):
    """
    :param driverMesh:
    :param drivenMesh:
    :param vertexIds: [0, 1, ...]
    :param vertexWeights: [1.0, 0.5, ...]
    :param deformMultiplier:
    :param space:
    :return:
    """
    deformMultiplier = getEditBlendshapeMultiplier(drivenMesh, deformMultiplier)
    driverIter = getMItMeshVertex(driverMesh)
    drivenIter = getMItMeshVertex(drivenMesh)

    deltas = []
    for vertexId, weight, driverPosition, drivenPosition in izip(
            vertexIds,
            vertexWeights,
            getVertexPositions(driverIter, vertexIds),
            getVertexPositions(drivenIter, vertexIds)):
        deltas.append((driverPosition - drivenPosition) * weight * deformMultiplier)
    mc.prMovePointsCmd(drivenMesh, space, vertexIds, *deltas)


def averageDeltas(driverMesh, drivenMesh, vertexIds, vertexWeights,
                  deformMultiplier=None, space=om.MSpace.kObject):
    """
    :param driverMesh:
    :param drivenMesh:
    :param vertexIds: [0, 1, ...]
    :param vertexWeights: [1.0, 0.5, ...]
    :param deformMultiplier:
    :param space:
    :return:
    """
    deformMultiplier = getEditBlendshapeMultiplier(drivenMesh, deformMultiplier)
    driverIter = getMItMeshVertex(driverMesh)
    drivenIter = getMItMeshVertex(drivenMesh)

    deltas = []
    for vertexId, weight in izip(vertexIds, vertexWeights):
        drivenIter.setIndex(vertexId)
        allVertexIds = drivenIter.getConnectedVertices()
        allVertexIds.insert(vertexId, 0)
        driverPositions = getVertexPositions(driverIter, allVertexIds)
        drivenPositions = getVertexPositions(drivenIter, allVertexIds)
        averageDelta = om.MVector()
        for driverPos, drivenPos in izip(driverPositions[1:], drivenPositions[1:]):
            averageDelta += drivenPos - driverPos
        averageDelta *= 1.0/(len(allVertexIds)-1)
        deltas.append(((driverPositions[0] + averageDelta) - drivenPositions[0]) * weight * deformMultiplier)
    mc.prMovePointsCmd(drivenMesh, space, vertexIds, *deltas)

