"""
Parallel Transport Approach to Curve Framing

paper:
https://pdfs.semanticscholar.org/7e65/2313c1f8183a0f43acce58ae8d8caf370a6b.pdf

algorithm explanation and houdini implementation tutorial:
https://vimeo.com/251091418


TODO:
- outTranslate array
- make upMatrix upVector perpendicular to first tangent
- fix unstable twist when rotations are zero
- user defined up vector
- maybe user defined aim vector

TODO LATER:
- check outputMatrix to MFnData.kMatrixArray ?
- createDecomposeMatrixFromOutputMatrix split off transform creation in separate function
- aetemplate outputMatrix scroll layout
"""

import sys
import math

import maya.api.OpenMaya as om
import maya.cmds as mc


class prCurveFrame(om.MPxNode):
    nodeTypeName = "prCurveFrame"
    nodeTypeId = om.MTypeId(0x0004C261)  # local, not save

    @staticmethod
    def initialize():
        typedAttr = om.MFnTypedAttribute()
        matrixAttr = om.MFnMatrixAttribute()
        numericAttr = om.MFnNumericAttribute()
        
        # OUTPUT
        prCurveFrame.outputMatrix = matrixAttr.create("outputMatrix", "outputMatrix", matrixAttr.kDouble)
        matrixAttr.array = True
        matrixAttr.usesArrayDataBuilder = True
        matrixAttr.readable = True
        matrixAttr.writable = False
        prCurveFrame.addAttribute(prCurveFrame.outputMatrix)

        # INPUT
        prCurveFrame.inputCurve = typedAttr.create('inputCurve', 'inputCurve', om.MFnNurbsCurveData.kNurbsCurve)
        prCurveFrame.addAttribute(prCurveFrame.inputCurve)
        prCurveFrame.attributeAffects(prCurveFrame.inputCurve, prCurveFrame.outputMatrix)

        prCurveFrame.points = numericAttr.create("points", "points", om.MFnNumericData.kInt, 5)
        numericAttr.keyable = True
        prCurveFrame.addAttribute(prCurveFrame.points)
        prCurveFrame.attributeAffects(prCurveFrame.points, prCurveFrame.outputMatrix)
        
        prCurveFrame.worldUpMatrix = matrixAttr.create("worldUpMatrix", "worldUpMatrix", matrixAttr.kDouble)
        prCurveFrame.addAttribute(prCurveFrame.worldUpMatrix)
        prCurveFrame.attributeAffects(prCurveFrame.worldUpMatrix, prCurveFrame.outputMatrix)

    @staticmethod
    def creator():
        return prCurveFrame()

    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug, data):
        if plug != prCurveFrame.outputMatrix:
            return None
        inputCurve = om.MFnNurbsCurve(data.inputValue(prCurveFrame.inputCurve).asNurbsCurve())
        points = data.inputValue(prCurveFrame.points).asInt()
        worldUpMatrix = data.inputValue(prCurveFrame.worldUpMatrix).asMatrix()

        stepLength = inputCurve.length() / (points-1)
        positions = []
        tangents = []
        for x in range(points):
            parameter = inputCurve.findParamFromLength(x*stepLength)
            positions.append(inputCurve.getPointAtParam(parameter, space=om.MSpace.kWorld))
            tangents.append(inputCurve.tangent(parameter, space=om.MSpace.kWorld))

        normals = [om.MVector(list(worldUpMatrix)[4:7])]  # TODO: temp code
        bitangents = [om.MVector(list(worldUpMatrix)[7:10])]
        for x in range(points-1):
            bitangent = tangents[x] ^ tangents[x+1]
            if bitangent.length() == 0:
                normal = normals[x]
            else:
                bitangent.normalize()
                angle = math.radians(math.acos(tangents[x] * tangents[x+1]))
                normal = normals[x].rotateBy(om.MQuaternion(angle, bitangent))
                # normal = normal[x] * getRotationMatrix(angle, bitangent)
            normals.append(normal)
            bitangents.append(bitangent)

        outputMatrixArrayHandle = data.outputArrayValue(prCurveFrame.outputMatrix)
        outputMatrixBuilder = outputMatrixArrayHandle.builder()
        for x in range(points):
            matrix = om.MMatrix((list(tangents[x]) + [0], list(normals[x]) + [0], list(bitangents[x]) + [0], list(positions[x])))
            outputMatrixHandle = outputMatrixBuilder.addElement(x)
            outputMatrixHandle.setMMatrix(matrix)
        outputMatrixArrayHandle.set(outputMatrixBuilder)

        data.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prCurveFrame.nodeTypeName, prCurveFrame.nodeTypeId, prCurveFrame.creator, prCurveFrame.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prCurveFrame.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prCurveFrame.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prCurveFrame.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprCurveFrameTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prPyMath Attributes" -collapse 0;
                editorTemplate -label "points" -addControl "points";
                editorTemplate -label "worldUpMatrix" -addControl "worldUpMatrix";
                editorTemplate -label "outputMatrix" -addControl "outputMatrix";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')


def createFromCurve(curve=None):
    curve = curve or mc.ls(sl=True, type=['transform', 'nurbsCurve'])[0]
    curveFrame = mc.createNode('prCurveFrame')
    mc.connectAttr('{0}.worldSpace'.format(curve), '{0}.inputCurve'.format(curveFrame))
    return curveFrame


def createDecomposeMatrixFromOutputMatrix(curveFrame=None, createTransformType='locator', toggleLocalAxis=True):
    mc.getAttr('{0}.outputMatrix[0]'.format(curveFrame))
    selectionList = om.MSelectionList()
    selectionList.add('{0}.outputMatrix'.format(curveFrame))
    transforms = []
    for x in range(selectionList.getPlug(0).numElements()):
        decomposeMatrix = mc.createNode('decomposeMatrix')
        decomposeMatrix = mc.rename(decomposeMatrix, '{0}_{1}_decomposeMatrix'.format(curveFrame, x))
        mc.connectAttr('{0}.outputMatrix[{1}]'.format(curveFrame, x), '{0}.inputMatrix'.format(decomposeMatrix))
        if createTransformType:
            transform = mc.createNode(createTransformType)
            if mc.ls(transform, type='shape'):
                transform = mc.listRelatives(transform, parent=True)[0]
            mc.connectAttr('{0}.outputTranslate'.format(decomposeMatrix), '{0}.translate'.format(transform))
            mc.connectAttr('{0}.outputRotate'.format(decomposeMatrix), '{0}.rotate'.format(transform))
            transforms.append(transform)
    if toggleLocalAxis:
        mc.toggle(transforms, localAxis=True)
    return transforms

