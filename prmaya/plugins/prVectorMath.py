"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Array version of Mayas "vectorProduct" with added operations and features.
New operations:
- Sum, Subtract, Average (similar to Mayas plusMinusAverage)
- Project (in1 on in2), Project (in2 on in1)
New features:
- .input[0].scalar to multiply each output with
- .globalScalar to multiply all outputs with
- .globalMatrix attr to multiply all outputs with (Matrix Product operations)

USE CASES
- Replace multiple Maya nodes (vectorProduct, plusMinusAverage) with fewer
  prVectorMath nodes
- New operations/features missing in Maya

USAGE
(MEL): createNode prVectorMath

ATTRIBUTES
prVectorMath1.normalizeOutput
prVectorMath1.globalScalar
prVectorMath1.globalMatrix
prVectorMath1.input[0].input1
prVectorMath1.input[0].input1.input1X
prVectorMath1.input[0].input1.input1Y
prVectorMath1.input[0].input1.input1Z
prVectorMath1.input[0].input2
prVectorMath1.input[0].input2.input2X
prVectorMath1.input[0].input2.input2Y
prVectorMath1.input[0].input2.input2Z
prVectorMath1.input[0].scalar
prVectorMath1.input[0].matrix
prVectorMath1.output[0]
prVectorMath1.output[0].outputX
prVectorMath1.output[0].outputY
prVectorMath1.output[0].outputZ
prVectorMath1.operation
- 0, No operation: forward input1. Same as vectorProduct
- 1, Sum: Same as plusMinusAverage
- 2, Subtract: Same as plusMinusAverage
- 3, Average: Same as plusMinusAverage
- 4, Dot Product: Same as vectorProduct
- 5, Cross Product: Same as vectorProduct
- 6, Vector Matrix Product: Same as vectorProduct
- 7, Point Matrix Product: Same as vectorProduct
- 8, Project (in1 on in2): new
- 9, Project (in2 on in1): new

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- optional cleanup (icon, aeTemplate array attr, nodeBehavior attr)
"""

import sys

import maya.api.OpenMaya as om


class prVectorMath(om.MPxNode):
    nodeTypeName = "prVectorMath"
    nodeTypeId = om.MTypeId(0x0004C269)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        matrixAttr = om.MFnMatrixAttribute()

        # output
        prVectorMath.output = numericAttr.createPoint('output', 'output')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prVectorMath.addAttribute(prVectorMath.output)

        # input
        prVectorMath.operation = enumAttr.create('operation', 'operation', 1)
        enumAttr.keyable = True
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Sum +', 1)
        enumAttr.addField('Subtract -', 2)
        enumAttr.addField('Average', 3)
        enumAttr.addField('Dot Product *', 4)
        enumAttr.addField('Cross Product x', 5)
        enumAttr.addField('Vector Matrix Product *', 6)
        enumAttr.addField('Point Matrix Product *', 7)
        enumAttr.addField('Project in1 on in2', 8)
        enumAttr.addField('Project in2 on in1', 9)
        prVectorMath.addAttribute(prVectorMath.operation)
        prVectorMath.attributeAffects(prVectorMath.operation, prVectorMath.output)

        prVectorMath.normalizeOutput = numericAttr.create('normalizeOutput', 'normalizeOutput', om.MFnNumericData.kBoolean, False)
        numericAttr.keyable = True
        prVectorMath.addAttribute(prVectorMath.normalizeOutput)
        prVectorMath.attributeAffects(prVectorMath.normalizeOutput, prVectorMath.output)

        prVectorMath.globalScalar = numericAttr.create('globalScalar', 'globalScalar', om.MFnNumericData.kFloat, 1.0)
        numericAttr.keyable = True
        prVectorMath.addAttribute(prVectorMath.globalScalar)
        prVectorMath.attributeAffects(prVectorMath.globalScalar, prVectorMath.output)

        prVectorMath.globalMatrix = matrixAttr.create('globalMatrix', 'globalMatrix')
        matrixAttr.keyable = True
        prVectorMath.addAttribute(prVectorMath.globalMatrix)
        prVectorMath.attributeAffects(prVectorMath.globalMatrix, prVectorMath.output)

        prVectorMath.input1 = numericAttr.createPoint('input1', 'input1')
        numericAttr.keyable = True

        prVectorMath.input2 = numericAttr.createPoint('input2', 'input2')
        numericAttr.keyable = True

        prVectorMath.matrix = matrixAttr.create('matrix', 'matrix')
        matrixAttr.keyable = True

        prVectorMath.scalar = numericAttr.create('scalar', 'scalar', om.MFnNumericData.kFloat, 1.0)
        numericAttr.keyable = True

        prVectorMath.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prVectorMath.input1)
        compoundAttr.addChild(prVectorMath.input2)
        compoundAttr.addChild(prVectorMath.scalar)
        compoundAttr.addChild(prVectorMath.matrix)
        compoundAttr.array = True
        prVectorMath.addAttribute(prVectorMath.input)
        prVectorMath.attributeAffects(prVectorMath.input1, prVectorMath.output)
        prVectorMath.attributeAffects(prVectorMath.input2, prVectorMath.output)
        prVectorMath.attributeAffects(prVectorMath.scalar, prVectorMath.output)
        prVectorMath.attributeAffects(prVectorMath.matrix, prVectorMath.output)

    @staticmethod
    def creator():
        return prVectorMath()

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
            in1 = om.MVector(inputTargetHandle.child(self.input1).asFloat3())
            in2 = om.MVector(inputTargetHandle.child(self.input2).asFloat3())
            scalar = inputTargetHandle.child(self.scalar).asFloat()

            output_handle = output_builder.addElement(index)

            if operation == 0:  # No operation
                out = in1
            elif operation == 1:  # Sum
                out = in1 + in2
            elif operation == 2:  # Subtract
                out = in1 - in2
            elif operation == 3:  # Average
                out = (in1 + in2) * 0.5
            elif operation == 4:  # Dot Product
                if normalizeOutput:
                    in1.normalize()
                    in2.normalize()
                dotProduct = in1 * in2
                out = om.MVector(dotProduct, dotProduct, dotProduct)
            elif operation == 5:  # Cross Product
                out = in1 ^ in2
            elif operation in [6, 7]:  # Vector / Point Matrix Product
                matrix = inputTargetHandle.child(self.matrix).asMatrix()
                m = globalMatrix * matrix
                out = in1 * m
                if operation == 7:  # Point Matrix Product
                    out += om.MVector(m[12], m[13], m[14])
            elif operation == 8:  # Projection in1 on in2
                out = in2 * (in1 * in2 / in2.length() ** 2)
            elif operation == 9:  # Projection in2 on in1
                out = in1 * (in1 * in2 / in1.length() ** 2)
            else:
                raise ValueError('operation: {}'.format(operation))

            if scalar * globalScalar != 1.0:
                out *= globalScalar * scalar
            if normalizeOutput and operation != 4:
                out.normalize()
            output_handle.set3Float(*out)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prVectorMath.nodeTypeName, prVectorMath.nodeTypeId,
                              prVectorMath.creator, prVectorMath.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prVectorMath.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prVectorMath.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prVectorMath.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprVectorMathTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prVectorMath Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "normalizeOutput" -addControl "normalizeOutput";
                editorTemplate -label "globalScalar" -addControl "globalScalar";
                editorTemplate -label "globalMatrix" -addControl "globalMatrix";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
