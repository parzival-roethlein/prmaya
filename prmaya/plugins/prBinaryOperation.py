"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Binary operation for array of scalar pairs.
The purpose of this node is to reduce the number of nodes in the scene by
replacing multiple plusMinusAverage and multiplyDivide nodes with one

USE CASES
...

USAGE
(MEL): createNode prBinaryOperation

ATTRIBUTES
prBinaryOperation1.operation
prBinaryOperation1.input[0].input1
prBinaryOperation1.input[0].input2
prBinaryOperation1.output[0]

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- node behavior attrs
- custom aeTemplate for prBinaryOperation.input

"""

import sys

import maya.api.OpenMaya as om


class prBinaryOperation(om.MPxNode):
    nodeTypeName = "prBinaryOperation"
    nodeTypeId = om.MTypeId(0x0004C266)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        enumAttr = om.MFnEnumAttribute()

        # output
        prBinaryOperation.output = numericAttr.create('output', 'output', om.MFnNumericData.kFloat)
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prBinaryOperation.addAttribute(prBinaryOperation.output)

        # input
        prBinaryOperation.operation = enumAttr.create('operation', 'operation', 1)
        enumAttr.keyable = True
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Sum', 1)
        enumAttr.addField('Subtract', 2)
        enumAttr.addField('Average', 3)
        enumAttr.addField('Multiply', 4)
        enumAttr.addField('Divide', 5)
        enumAttr.addField('Power', 6)
        prBinaryOperation.addAttribute(prBinaryOperation.operation)
        prBinaryOperation.attributeAffects(prBinaryOperation.operation, prBinaryOperation.output)

        prBinaryOperation.input1 = numericAttr.create('input1', 'input1', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True

        prBinaryOperation.input2 = numericAttr.create('input2', 'input2', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True

        prBinaryOperation.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prBinaryOperation.input1)
        compoundAttr.addChild(prBinaryOperation.input2)
        compoundAttr.array = True
        prBinaryOperation.addAttribute(prBinaryOperation.input)
        prBinaryOperation.attributeAffects(prBinaryOperation.input1, prBinaryOperation.output)
        prBinaryOperation.attributeAffects(prBinaryOperation.input2, prBinaryOperation.output)

    @staticmethod
    def creator():
        return prBinaryOperation()

    def __init__(self):
        om.MPxNode.__init__(self)

    def displayError(self, error, index=None):
        nodeName = om.MFnDependencyNode(self.thisMObject()).name()
        if index is None:
            message = '{0}: "{1}"'.format(error, nodeName)
        else:
            message = '{0}: "{1}.input[{2}]"'.format(error, nodeName, index)
        om.MGlobal.displayError(message)

    def compute(self, plug, dataBlock):
        if plug not in [self.output]:
            self.displayError(error='Unknown plug: {}'.format(plug))
            return
        operation = dataBlock.inputValue(self.operation).asShort()

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()
        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            inputTargetHandle = inputArrayHandle.inputValue()
            in1 = inputTargetHandle.child(self.input1).asFloat()
            in2 = inputTargetHandle.child(self.input2).asFloat()
            output_handle = output_builder.addElement(index)
            if operation == 0:
                output = 0.0
            elif operation == 1:
                output = in1 + in2
            elif operation == 2:
                output = in1 - in2
            elif operation == 3:
                output = (in1 + in2) / 2
            elif operation == 4:
                output = in1 * in2
            elif operation == 5:
                try:
                    output = in1 / in2
                except ZeroDivisionError as er:
                    self.displayError(er, index)
                    output = 0.0
            elif operation == 6:
                try:
                    output = in1 ** in2
                except ValueError as er:
                    self.displayError(er, index)
                    output = 0.0
            else:
                raise ValueError('Invalid operation value: {}'.format(operation))
            output_handle.setFloat(output)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prBinaryOperation.nodeTypeName, prBinaryOperation.nodeTypeId,
                              prBinaryOperation.creator, prBinaryOperation.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prBinaryOperation.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prBinaryOperation.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prBinaryOperation.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprBinaryOperationTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prBinaryOperation Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
