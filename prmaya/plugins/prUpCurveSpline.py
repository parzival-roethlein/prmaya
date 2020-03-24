"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
...

USE CASES
...

USAGE
(MEL): createNode prUpCurveSpline

ATTRIBUTES
prUpCurveSpline.curve
prUpCurveSpline.upCurve
prUpCurveSpline.startOrientMatrix
prUpCurveSpline.endOrientMatrix
prUpCurveSpline.parameter[0]
prUpCurveSpline.parameterType (parameter, parameter normalized, length, fractionMode)
prUpCurveSpline.aimAxis (x, y, z, -x, -y, -z)
prUpCurveSpline.upAxis (x, y, z, -x, -y, -z)
prUpCurveSpline.enableStartOrientMatrix
prUpCurveSpline.enableEndOrientMatrix
prUpCurveSpline.outputMatrix[0]

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
...

"""


import sys

import maya.api.OpenMaya as om


class prUpCurveSpline(om.MPxNode):
    nodeTypeName = "prUpCurveSpline"
    nodeTypeId = om.MTypeId(0x0004C272)  # local, not save

    @staticmethod
    def initialize():
        matrixAttr = om.MFnMatrixAttribute()
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        typedAttr = om.MFnTypedAttribute()

        # OUTPUT
        prUpCurveSpline.outputMatrix = matrixAttr.create('outputMatrix', 'outputMatrix')
        matrixAttr.array = True
        matrixAttr.usesArrayDataBuilder = True
        matrixAttr.writable = False
        prUpCurveSpline.addAttribute(prUpCurveSpline.outputMatrix)

        # INPUTS
        prUpCurveSpline.curve = typedAttr.create(
            'curve', 'curve', om.MFnNurbsCurveData.kNurbsCurve)
        prUpCurveSpline.addAttribute(prUpCurveSpline.curve)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.curve,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.upCurve = typedAttr.create(
            'upCurve', 'upCurve', om.MFnNurbsCurveData.kNurbsCurve)
        prUpCurveSpline.addAttribute(prUpCurveSpline.upCurve)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.upCurve,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.startOrientMatrix = matrixAttr.create(
            'startOrientMatrix', 'startOrientMatrix')
        prUpCurveSpline.addAttribute(prUpCurveSpline.startOrientMatrix)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.startOrientMatrix,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.endOrientMatrix = matrixAttr.create(
            'endOrientMatrix', 'endOrientMatrix')
        prUpCurveSpline.addAttribute(prUpCurveSpline.endOrientMatrix)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.endOrientMatrix,
                                         prUpCurveSpline.outputMatrix)

        # SETTINGS
        prUpCurveSpline.parameter = numericAttr.create('parameter', 'parameter',
                                                       om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        prUpCurveSpline.addAttribute(prUpCurveSpline.parameter)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.parameter,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.parameterType = enumAttr.create('parameterType', 'parameterType', 0)
        enumAttr.addField('normalized parameter', 0)
        enumAttr.addField('parameter', 1)
        enumAttr.addField('fractionMode', 2)
        enumAttr.addField('length', 3)
        enumAttr.keyable = True
        prUpCurveSpline.addAttribute(prUpCurveSpline.parameterType)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.parameterType,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.aimAxis = enumAttr.create('aimAxis', 'aimAxis', 0)
        enumAttr.addField('x', 0)
        enumAttr.addField('y', 1)
        enumAttr.addField('z', 2)
        enumAttr.addField('-x', 3)
        enumAttr.addField('-y', 4)
        enumAttr.addField('-z', 5)
        enumAttr.keyable = True
        prUpCurveSpline.addAttribute(prUpCurveSpline.aimAxis)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.aimAxis,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.upAxis = enumAttr.create('upAxis', 'upAxis', 0)
        enumAttr.addField('x', 0)
        enumAttr.addField('y', 1)
        enumAttr.addField('z', 2)
        enumAttr.addField('-x', 3)
        enumAttr.addField('-y', 4)
        enumAttr.addField('-z', 5)
        enumAttr.keyable = True
        prUpCurveSpline.addAttribute(prUpCurveSpline.upAxis)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.upAxis,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.enableStartOrientMatrix = numericAttr.create(
            'enableStartOrientMatrix', 'enableStartOrientMatrix',
            om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prUpCurveSpline.addAttribute(prUpCurveSpline.enableStartOrientMatrix)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.enableStartOrientMatrix,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.enableEndOrientMatrix = numericAttr.create(
            'enableEndOrientMatrix', 'enableEndOrientMatrix',
            om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prUpCurveSpline.addAttribute(prUpCurveSpline.enableEndOrientMatrix)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.enableEndOrientMatrix,
                                         prUpCurveSpline.outputMatrix)

    @staticmethod
    def creator():
        return prUpCurveSpline()

    def __init__(self):
        om.MPxNode.__init__(self)

    def displayWarning(self, error, index=None):
        nodeName = om.MFnDependencyNode(self.thisMObject()).name()
        if index is None:
            message = '"{0}": {1}'.format(nodeName, error)
        else:
            message = '"{0}.input[{1}]": {2}'.format(nodeName, index, error)
        om.MGlobal.displayWarning(message)

    def compute(self, plug, dataBlock):
        if plug not in [self.outputMatrix]:
            self.displayWarning(error='Unknown plug: {}'.format(plug))
            return

        # INPUTS
        curveHandle = dataBlock.inputValue(self.curve)
        upCurveHandle = dataBlock.inputValue(self.upCurve)
        curveData = curveHandle.data()
        upCurveData = upCurveHandle.data()
        if curveData.isNull() or upCurveData.isNull():
            return
        curveFn = om.MFnNurbsCurve(curveData)
        upCurveFn = om.MFnNurbsCurve(upCurveData)

        startOrientMatrix = dataBlock.inputValue(self.startOrientMatrix).asMatrix()
        endOrientMatrix = dataBlock.inputValue(self.endOrientMatrix).asMatrix()

        # SETTINGS
        parameterType = dataBlock.inputValue(self.parameterType).asShort()
        aimAxis = dataBlock.inputValue(self.aimAxis).asShort()
        upAxis = dataBlock.inputValue(self.upAxis).asShort()
        enableStartOrientMatrix = dataBlock.inputValue(self.enableStartOrientMatrix).asBool()
        enableEndOrientMatrix = dataBlock.inputValue(self.enableEndOrientMatrix).asBool()

        # GET PARAMETER POSITIONS
        indices = []
        positions = om.MPointArray()
        upPositions = om.MPointArray()

        parameterArrayHandle = dataBlock.inputArrayValue(self.parameter)
        for x in range(len(parameterArrayHandle)):
            parameterArrayHandle.jumpToPhysicalElement(x)
            indices.append(parameterArrayHandle.elementLogicalIndex())
            parameter = parameterArrayHandle.inputValue().asFloat()

            positions.append(curveFn.getPointAtParam(parameter))
            upPositions.append(upCurveFn.getPointAtParam(parameter))

        # OUTPUT
        outputMatrixArrayHandle = dataBlock.outputArrayValue(self.outputMatrix)
        outputMatrixBuilder = outputMatrixArrayHandle.builder()
        for x, (index, position, upPosition) in enumerate(
                zip(indices, positions, upPositions)):
            outputMatrixHandle = outputMatrixBuilder.addElement(index)
            matrix = om.MMatrix()
            # vector
            if x == 0:
                aimVector = positions[x+1] - position
            else:
                aimVector = om.MVector(1, 0, 0)
            upVector = upPosition - position  # angle 90 degrees to aimVector

            # X
            matrix[0] = aimVector[0]
            matrix[1] = aimVector[1]
            matrix[2] = aimVector[2]
            # Y
            matrix[4] = upVector[0]
            matrix[5] = upVector[1]
            matrix[6] = upVector[2]
            # Z
            # cross product

            # position
            matrix[12] = position[0]
            matrix[13] = position[1]
            matrix[14] = position[2]

            outputMatrixHandle.setMMatrix(matrix)

        outputMatrixArrayHandle.set(outputMatrixBuilder)
        outputMatrixArrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prUpCurveSpline.nodeTypeName, prUpCurveSpline.nodeTypeId,
                              prUpCurveSpline.creator, prUpCurveSpline.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prUpCurveSpline.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prUpCurveSpline.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prUpCurveSpline.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprUpCurveSplineTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prUpCurveSpline Attributes" -collapse 0;
                editorTemplate -label "parameter" -addControl "parameter";
                editorTemplate -label "parameterType" -addControl "parameterType";
                editorTemplate -label "aimAxis" -addControl "aimAxis";
                editorTemplate -label "upAxis" -addControl "upAxis";
                editorTemplate -label "enableStartOrientMatrix" -addControl "enableStartOrientMatrix";
                editorTemplate -label "enableEndOrientMatrix" -addControl "enableEndOrientMatrix";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "output";
    };
    ''')
