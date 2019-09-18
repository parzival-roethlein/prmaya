"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
array version of mayas "vectorProduct" node.
added features:
- new .input[0].scalar to multiply output with
- new .globalScalar to multiply all outputs with
- new .globalMatrix attr to multiply all outputs with for Matrix Product operations

USE CASES
...

USAGE
(MEL): createNode prVectorProduct

ATTRIBUTES
prVectorProduct1.operation
prVectorProduct1.normalizeOutput
prVectorProduct1.globalScalar
prVectorProduct1.globalMatrix
prVectorProduct1.input[0].input1
prVectorProduct1.input[0].input1.input1X
prVectorProduct1.input[0].input1.input1Y
prVectorProduct1.input[0].input1.input1Z
prVectorProduct1.input[0].input2
prVectorProduct1.input[0].input2.input2X
prVectorProduct1.input[0].input2.input2Y
prVectorProduct1.input[0].input2.input2Z
prVectorProduct1.input[0].scalar
prVectorProduct1.input[0].matrix
prVectorProduct1.output[0]
prVectorProduct1.output[0].outputX
prVectorProduct1.output[0].outputY
prVectorProduct1.output[0].outputZ

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- custom aeTemplate for array input attr
- node behavior attrs
- icons
"""


import sys
import math

import maya.api.OpenMaya as om


def multiply_matrix_with_matrix(m1, m2):
    return m1


class prVectorProduct(om.MPxNode):
    nodeTypeName = "prVectorProduct"
    nodeTypeId = om.MTypeId(0x0004C269)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        matrixAttr = om.MFnMatrixAttribute()

        # output
        prVectorProduct.output = numericAttr.createPoint('output', 'output')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prVectorProduct.addAttribute(prVectorProduct.output)

        # input
        prVectorProduct.operation = enumAttr.create('operation', 'operation', 1)
        enumAttr.keyable = True
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Dot Product', 1)
        enumAttr.addField('Cross Product', 2)
        enumAttr.addField('Vector Matrix Product', 3)
        enumAttr.addField('Point Matrix Product', 4)
        prVectorProduct.addAttribute(prVectorProduct.operation)
        prVectorProduct.attributeAffects(prVectorProduct.operation, prVectorProduct.output)

        prVectorProduct.normalizeOutput = numericAttr.create('normalizeOutput', 'normalizeOutput', om.MFnNumericData.kBoolean, False)
        numericAttr.keyable = True
        prVectorProduct.addAttribute(prVectorProduct.normalizeOutput)
        prVectorProduct.attributeAffects(prVectorProduct.normalizeOutput, prVectorProduct.output)

        prVectorProduct.globalScalar = numericAttr.create('globalScalar', 'globalScalar', om.MFnNumericData.kFloat, 1.0)
        numericAttr.keyable = True
        prVectorProduct.addAttribute(prVectorProduct.globalScalar)
        prVectorProduct.attributeAffects(prVectorProduct.globalScalar, prVectorProduct.output)

        prVectorProduct.globalMatrix = matrixAttr.create('globalMatrix', 'globalMatrix')
        matrixAttr.keyable = True
        prVectorProduct.addAttribute(prVectorProduct.globalMatrix)
        prVectorProduct.attributeAffects(prVectorProduct.globalMatrix, prVectorProduct.output)

        prVectorProduct.input1 = numericAttr.createPoint('input1', 'input1')
        numericAttr.keyable = True

        prVectorProduct.input2 = numericAttr.createPoint('input2', 'input2')
        numericAttr.keyable = True

        prVectorProduct.matrix = matrixAttr.create('matrix', 'matrix')
        matrixAttr.keyable = True

        prVectorProduct.scalar = numericAttr.create('scalar', 'scalar', om.MFnNumericData.kFloat, 1.0)
        numericAttr.keyable = True

        prVectorProduct.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prVectorProduct.input1)
        compoundAttr.addChild(prVectorProduct.input2)
        compoundAttr.addChild(prVectorProduct.scalar)
        compoundAttr.addChild(prVectorProduct.matrix)
        compoundAttr.array = True
        prVectorProduct.addAttribute(prVectorProduct.input)
        prVectorProduct.attributeAffects(prVectorProduct.input1, prVectorProduct.output)
        prVectorProduct.attributeAffects(prVectorProduct.input2, prVectorProduct.output)
        prVectorProduct.attributeAffects(prVectorProduct.scalar, prVectorProduct.output)
        prVectorProduct.attributeAffects(prVectorProduct.matrix, prVectorProduct.output)

    @staticmethod
    def creator():
        return prVectorProduct()

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
        if plug not in [self.output]:
            self.displayWarning(error='Unknown plug: {}'.format(plug))
            return
        operation = dataBlock.inputValue(self.operation).asShort()
        normalizeOutput = dataBlock.inputValue(self.normalizeOutput).asBool()
        globalScalar = dataBlock.inputValue(self.globalScalar).asFloat()
        globalMatrix = dataBlock.inputValue(self.globalMatrix).asMatrix()

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()

        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            inputTargetHandle = inputArrayHandle.inputValue()
            in1 = inputTargetHandle.child(self.input1).asFloat3()
            in2 = inputTargetHandle.child(self.input2).asFloat3()
            scalar = inputTargetHandle.child(self.scalar).asFloat()

            output_handle = output_builder.addElement(index)
            if operation == 0:  # No operation
                out = in1
            elif operation == 1:  # Dot Product
                dotProduct = in1[0] * in2[0] + in1[1] * in2[1] + in1[2] * in2[2]
                out = [dotProduct, dotProduct, dotProduct]
            elif operation == 2:  # Cross Product
                outX = in1[1] * in2[2] - in1[2] * in2[1]
                outY = in1[2] * in2[0] - in1[0] * in2[2]
                outZ = in1[0] * in2[1] - in1[1] * in2[0]
                out = [outX, outY, outZ]
            elif operation == 3:  # Vector Matrix Product
                matrix = inputTargetHandle.child(self.matrix).asMatrix()
                m = multiply_matrix_with_matrix(globalMatrix, matrix)
                out = [in1[0] * m[0] + in1[1] * m[4] + in1[2] * m[8],
                       in1[0] * m[1] + in1[1] * m[5] + in1[2] * m[9],
                       in1[0] * m[2] + in1[1] * m[6] + in1[2] * m[10]]
            elif operation == 4:  # Point Matrix Product
                matrix = inputTargetHandle.child(self.matrix).asMatrix()
                m = multiply_matrix_with_matrix(globalMatrix, matrix)
                out = [in1[0] * m[0] + in1[1] * m[4] + in1[2] * m[8] + m[12],
                       in1[0] * m[1] + in1[1] * m[5] + in1[2] * m[9] + m[13],
                       in1[0] * m[2] + in1[1] * m[6] + in1[2] * m[10] + m[14]]
            else:
                raise ValueError('operation: {}'.format(operation))

            if scalar * globalScalar != 1.0:
                out = [o * globalScalar * scalar for o in out]
            if normalizeOutput and operation in [0, 1, 2, 3]:
                # TODO: fix dot product normalization
                length = math.sqrt(out[0]**2 + out[1]**2 + out[2]**2)
                out = [out[0] / length, out[1] / length, out[2] / length]
            output_handle.set3Float(*out)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prVectorProduct.nodeTypeName, prVectorProduct.nodeTypeId,
                              prVectorProduct.creator, prVectorProduct.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prVectorProduct.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prVectorProduct.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prVectorProduct.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprVectorProductTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prVectorProduct Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "normalizeOutput" -addControl "normalizeOutput";
                editorTemplate -label "globalScalar" -addControl "globalScalar";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
