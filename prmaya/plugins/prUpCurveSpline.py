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
prUpCurveSpline.startOrientMatrixWeight
prUpCurveSpline.endOrientMatrixWeight
prUpCurveSpline.outputMatrix[0]

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- axis functionality

TODO LATER
- performance comparison
- test: automatically flip backVector if dotproduct > 0 ?
- optimize
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
        prUpCurveSpline.parameterType = enumAttr.create('parameterType', 'parameterType', 1)
        enumAttr.addField('param', 0)
        enumAttr.addField('param normalized', 1)
        enumAttr.addField('length', 2)
        enumAttr.addField('fractionMode', 3)
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

        prUpCurveSpline.upAxis = enumAttr.create('upAxis', 'upAxis', 1)
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

        prUpCurveSpline.startOrientMatrixWeight = numericAttr.create(
            'startOrientMatrixWeight', 'startOrientMatrixWeight',
            om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        prUpCurveSpline.addAttribute(prUpCurveSpline.startOrientMatrixWeight)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.startOrientMatrixWeight,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.endOrientMatrixWeight = numericAttr.create(
            'endOrientMatrixWeight', 'endOrientMatrixWeight',
            om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        prUpCurveSpline.addAttribute(prUpCurveSpline.endOrientMatrixWeight)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.endOrientMatrixWeight,
                                         prUpCurveSpline.outputMatrix)

        prUpCurveSpline.parameter = numericAttr.create('parameter', 'parameter',
                                                       om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        prUpCurveSpline.addAttribute(prUpCurveSpline.parameter)
        prUpCurveSpline.attributeAffects(prUpCurveSpline.parameter,
                                         prUpCurveSpline.outputMatrix)

    @staticmethod
    def creator():
        return prUpCurveSpline()

    def __init__(self):
        om.MPxNode.__init__(self)

    def shouldSave(self, plug):
        """has to be overwritten, else parameter[..] with value 0.0 get lost"""
        if plug in [self.parameter]:
            return True
        return om.MPxNode.shouldSave(self, plug)  # == None

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

        # SETTINGS
        parameterType = dataBlock.inputValue(self.parameterType).asShort()
        aimAxis = dataBlock.inputValue(self.aimAxis).asShort()
        upAxis = dataBlock.inputValue(self.upAxis).asShort()
        if aimAxis % 3 == upAxis % 3:
            self.displayWarning(error='Skipped evaluation. aimAxis and upAxis have to be different axes')
            return
        startOrientMatrixWeight = dataBlock.inputValue(self.startOrientMatrixWeight).asFloat()
        endOrientMatrixWeight = dataBlock.inputValue(self.endOrientMatrixWeight).asFloat()
        startOrientMatrix = dataBlock.inputValue(self.startOrientMatrix).asMatrix()
        endOrientMatrix = dataBlock.inputValue(self.endOrientMatrix).asMatrix()

        # GET PARAMETER POSITIONS
        indices = []
        positions = om.MPointArray()
        upPositions = om.MPointArray()

        if parameterType == 3:
            curveLength = curveFn.length()
            upCurveLength = upCurveFn.length()
        parameterArrayHandle = dataBlock.inputArrayValue(self.parameter)
        parameterLength = len(parameterArrayHandle)
        if parameterLength < 3:
            self.displayWarning('Skipped evaluation. At least 3 parameters must be given')
            return
        for x in range(parameterLength):
            parameterArrayHandle.jumpToPhysicalElement(x)
            indices.append(parameterArrayHandle.elementLogicalIndex())
            parameter = parameterArrayHandle.inputValue().asFloat()

            if parameterType == 0:
                position = curveFn.getPointAtParam(parameter)
                upPosition = upCurveFn.getPointAtParam(parameter)
            elif parameterType == 1:
                minParam, maxParam = curveFn.knotDomain
                # TODO: check if minParam can be non-zero
                position = curveFn.getPointAtParam(parameter * maxParam)
                upPosition = upCurveFn.getPointAtParam(parameter * maxParam)
            elif parameterType == 2:
                baseParameter = curveFn.findParamFromLength(parameter)
                upParameter = upCurveFn.findParamFromLength(parameter)
                position = curveFn.getPointAtParam(baseParameter)
                upPosition = upCurveFn.getPointAtParam(upParameter)
            elif parameterType == 3:
                baseParameter = curveFn.findParamFromLength(parameter * curveLength)
                upParameter = upCurveFn.findParamFromLength(parameter * upCurveLength)
                position = curveFn.getPointAtParam(baseParameter)
                upPosition = upCurveFn.getPointAtParam(upParameter)
            positions.append(position)
            upPositions.append(upPosition)

        # OUTPUT
        outputMatrixArrayHandle = dataBlock.outputArrayValue(self.outputMatrix)
        outputMatrixBuilder = outputMatrixArrayHandle.builder()
        for x, (index, position, upPosition) in enumerate(
                zip(indices, positions, upPositions)):
            outputMatrixHandle = outputMatrixBuilder.addElement(index)

            # get orientated matrix
            if x == 0:
                matrix = getAimMatrixFromPoints(startPoint=position,
                                                aimPoint=positions[x + 1],
                                                upPoint=upPosition)
                if startOrientMatrixWeight:
                    matrix = getOrientedMatrix(startMatrix=matrix,
                                               targetMatrix=startOrientMatrix,
                                               factor=startOrientMatrixWeight)
            elif x == len(indices)-1:
                matrix = getAimMatrixFromPoints(startPoint=position,
                                                aimPoint=positions[x - 1],
                                                upPoint=upPosition,
                                                flipAim=True)
                if endOrientMatrixWeight:
                    matrix = getOrientedMatrix(startMatrix=matrix,
                                               targetMatrix=endOrientMatrix,
                                               factor=endOrientMatrixWeight)
            else:
                matrix = getAimMatrixFromPoints(startPoint=position,
                                                aimPoint=positions[x + 1],
                                                upPoint=upPosition)
                aimBackMatrix = getAimMatrixFromPoints(startPoint=position,
                                                       aimPoint=positions[x - 1],
                                                       upPoint=upPosition,
                                                       flipAim=True)
                matrix = getOrientedMatrix(startMatrix=matrix,
                                           targetMatrix=aimBackMatrix)

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
                editorTemplate -label "startOrientMatrixWeight" -addControl "startOrientMatrixWeight";
                editorTemplate -label "endOrientMatrixWeight" -addControl "endOrientMatrixWeight";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "output";
    };
    ''')


def getAimMatrixFromPoints(startPoint, aimPoint, upPoint, flipAim=False):
    # vectors
    if flipAim:
        aimVector = (startPoint - aimPoint).normalize()
    else:
        aimVector = (aimPoint - startPoint).normalize()
    upVector = upPoint - startPoint
    crossVector = (upVector ^ aimVector).normalize()
    upVector = (aimVector ^ crossVector).normalize()

    # matrix
    matrix = om.MMatrix()
    # X
    matrix[0] = aimVector[0]
    matrix[1] = aimVector[1]
    matrix[2] = aimVector[2]
    # Y
    matrix[4] = upVector[0]
    matrix[5] = upVector[1]
    matrix[6] = upVector[2]
    # Z
    matrix[8] = crossVector[0]
    matrix[9] = crossVector[1]
    matrix[10] = crossVector[2]

    return matrix


def getOrientedMatrix(startMatrix, targetMatrix, factor=0.5):
    startTransMatrix = om.MTransformationMatrix(startMatrix)
    startQuaternion = startTransMatrix.rotation(asQuaternion=True)

    targetTransMatrix = om.MTransformationMatrix(targetMatrix)
    targetQuaternion = targetTransMatrix.rotation(asQuaternion=True)

    resultQuaternion = om.MQuaternion.slerp(startQuaternion, targetQuaternion, factor)
    startTransMatrix.setRotation(resultQuaternion)
    return startTransMatrix.asMatrix()
