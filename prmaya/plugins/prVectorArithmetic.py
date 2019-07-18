"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Basic math for array of vector pairs.
Similar to Maya utility nodes, but for array.

USE CASES
...

USAGE
(MEL): createNode prVector

ATTRIBUTES
prVector1.operation
prVector1.normalizeOutput
prVector1.input[0].input1
prVector1.input[0].input1.input1X
prVector1.input[0].input1.input1Y
prVector1.input[0].input1.input1Z
prVector1.input[0].input2
prVector1.input[0].input2.input2X
prVector1.input[0].input2.input2Y
prVector1.input[0].input2.input2Z
prVector1.output[0]
prVector1.output[0].outputX
prVector1.output[0].outputY
prVector1.output[0].outputZ

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- names: prVectorMath, prVectorBinaryOp
- custom aeTemplate for array input attr
- node behavior attrs
- icons
"""

import sys
import math

import maya.api.OpenMaya as om


class prVectorArithmetic(om.MPxNode):
    nodeTypeName = "prVectorArithmetic"
    nodeTypeId = om.MTypeId(0x0004C265)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()

        # output
        prVectorArithmetic.output = numericAttr.createPoint('output', 'output')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prVectorArithmetic.addAttribute(prVectorArithmetic.output)

        # input
        prVectorArithmetic.operation = enumAttr.create('operation', 'operation', 1)
        enumAttr.keyable = True
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Sum +', 1)
        enumAttr.addField('Subtract -', 2)
        enumAttr.addField('Average', 3)
        enumAttr.addField('Cross product X', 4)
        enumAttr.addField('Projection', 5)
        prVectorArithmetic.addAttribute(prVectorArithmetic.operation)
        prVectorArithmetic.attributeAffects(prVectorArithmetic.operation, prVectorArithmetic.output)

        prVectorArithmetic.normalizeOutput = numericAttr.create('normalizeOutput', 'normalizeOutput', om.MFnNumericData.kBoolean, False)
        numericAttr.keyable = True
        prVectorArithmetic.addAttribute(prVectorArithmetic.normalizeOutput)
        prVectorArithmetic.attributeAffects(prVectorArithmetic.normalizeOutput, prVectorArithmetic.output)

        prVectorArithmetic.input1 = numericAttr.createPoint('input1', 'input1')
        numericAttr.keyable = True

        prVectorArithmetic.input2 = numericAttr.createPoint('input2', 'input2')
        numericAttr.keyable = True

        prVectorArithmetic.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prVectorArithmetic.input1)
        compoundAttr.addChild(prVectorArithmetic.input2)
        compoundAttr.array = True
        prVectorArithmetic.addAttribute(prVectorArithmetic.input)
        prVectorArithmetic.attributeAffects(prVectorArithmetic.input1, prVectorArithmetic.output)
        prVectorArithmetic.attributeAffects(prVectorArithmetic.input2, prVectorArithmetic.output)

    @staticmethod
    def creator():
        return prVectorArithmetic()

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

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()

        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)  # old api: jumpToArrayElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            inputTargetHandle = inputArrayHandle.inputValue()
            in1 = inputTargetHandle.child(self.input1).asFloat3()
            in2 = inputTargetHandle.child(self.input2).asFloat3()
            output_handle = output_builder.addElement(index)
            if operation == 0:
                out = in1
            elif operation == 1:
                out = [in1[0] + in2[0], in1[1] + in2[1], in1[2] + in2[2]]
            elif operation == 2:
                out = [in1[0] - in2[0], in1[1] - in2[1], in1[2] - in2[2]]
            elif operation == 3:
                out = [(in1[0] + in2[0]) / 2,
                       (in1[1] + in2[1]) / 2,
                       (in1[2] + in2[2]) / 2]
            elif operation == 4:
                out = [in1[1] * in2[2] - in1[2] * in2[1],
                       in1[2] * in2[0] - in1[0] * in2[2],
                       in1[0] * in2[1] - in1[1] * in2[0]]
            elif operation == 5:
                dot = in1[0] * in2[0] + in1[1] * in2[1] + in1[2] * in2[2]
                in2_length = math.sqrt(in2[0]**2 + in2[1]**2 + in2[2]**2)
                mult = dot / in2_length ** 2
                out = [in2[0] * mult, in2[1] * mult, in2[2] * mult]
            else:
                raise ValueError('operation: {}'.format(operation))
            if normalizeOutput:
                length = math.sqrt(out[0]**2 + out[1]**2 + out[2]**2)
                out = [out[0] / length, out[1] / length, out[2] / length]
            output_handle.set3Float(*out)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prVectorArithmetic.nodeTypeName, prVectorArithmetic.nodeTypeId,
                              prVectorArithmetic.creator, prVectorArithmetic.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prVectorArithmetic.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prVectorArithmetic.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prVectorArithmetic.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprVectorArithmeticTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prVectorArithmetic Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "normalizeOutput" -addControl "normalizeOutput";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
