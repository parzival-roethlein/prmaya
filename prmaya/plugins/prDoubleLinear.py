"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Basic math operations for pairs of numbers (+, -, average, *, /, ^, root)
The purpose of this node is to reduce the number of nodes in the scene by
replacing multiple standard maya nodes with a single node, because the Maya ones
only allow for a limited number of input pairs. Maya node examples:
- addDoubleLinear
- multDoubleLinear
- plusMinusAverage
- multiplyDivide

USE CASES
...

USAGE
(MEL): createNode prDoubleLinear

ATTRIBUTES
prDoubleLinear1.operation: similar to multiplyDivide and plusMinusAverage, except:
- 0, No operation: outputs 0.0
  (plusMinusAverage outputs 0.0)
  (multiplyDivide outputs input1)
- 5, Division: If ZeroDivisionError outputs 0.0
  (multiplyDivide if ZeroDivisionError outputs 100000)
- 6, Power: Negative number with fractional power gives error and outputs 0.0.
  (multiplyDivide node does not error and outputs NaN value)
- 7, Floor division: There is no maya node equivalent?!
- 8, Modulus: There is no maya node equivalent?!
- 9, input1: output input1.
  (multiplyDivide does this when in "No operation")
- 10, input2: output input2

prDoubleLinear1.input[0].input1
prDoubleLinear1.input[0].input2
prDoubleLinear1.output[0]

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- name: scalar, algebra/math, binary operation/pair. prScalarMath, prScalarPairMath, prScalarAlgebra
- node behavior attrs
- custom aeTemplate for prDoubleLinear.input

"""

import sys

import maya.api.OpenMaya as om


class prDoubleLinear(om.MPxNode):
    nodeTypeName = "prDoubleLinear"
    nodeTypeId = om.MTypeId(0x0004C266)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        enumAttr = om.MFnEnumAttribute()

        # output
        prDoubleLinear.output = numericAttr.create('output', 'output', om.MFnNumericData.kDouble)
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prDoubleLinear.addAttribute(prDoubleLinear.output)

        # input
        prDoubleLinear.operation = enumAttr.create('operation', 'operation', 1)
        enumAttr.keyable = True
        # operation names from maya nodes (plusMinusAverage, multiplyDivide)
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Sum +', 1)
        enumAttr.addField('Subtract -', 2)
        enumAttr.addField('Average', 3)
        enumAttr.addField('Multiply *', 4)
        enumAttr.addField('Divide /', 5)
        enumAttr.addField('Power ^', 6)
        enumAttr.addField('Floor division //', 7)
        enumAttr.addField('Modulus %', 8)
        enumAttr.addField('input1', 9)
        enumAttr.addField('input2', 10)
        prDoubleLinear.addAttribute(prDoubleLinear.operation)
        prDoubleLinear.attributeAffects(prDoubleLinear.operation, prDoubleLinear.output)

        prDoubleLinear.input1 = numericAttr.create('input1', 'input1', om.MFnNumericData.kDouble, 0.0)
        numericAttr.keyable = True

        prDoubleLinear.input2 = numericAttr.create('input2', 'input2', om.MFnNumericData.kDouble, 1.0)
        numericAttr.keyable = True

        prDoubleLinear.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prDoubleLinear.input1)
        compoundAttr.addChild(prDoubleLinear.input2)
        compoundAttr.array = True
        prDoubleLinear.addAttribute(prDoubleLinear.input)
        prDoubleLinear.attributeAffects(prDoubleLinear.input1, prDoubleLinear.output)
        prDoubleLinear.attributeAffects(prDoubleLinear.input2, prDoubleLinear.output)

    @staticmethod
    def creator():
        return prDoubleLinear()

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

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()
        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            inputTargetHandle = inputArrayHandle.inputValue()
            in1 = inputTargetHandle.child(self.input1).asDouble()
            in2 = inputTargetHandle.child(self.input2).asDouble()
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
                    self.displayWarning('ZeroDivisionError: {}'.format(er), index)
                    output = 0.0
            elif operation == 6:
                try:
                    output = in1 ** in2
                except ValueError as er:
                    self.displayWarning('ValueError: {}'.format(er), index)
                    output = 0.0
            elif operation == 7:
                try:
                    output = in1 // in2
                except ZeroDivisionError as er:
                    self.displayWarning('ZeroDivisionError: {}'.format(er), index)
                    output = 0.0
            elif operation == 8:
                try:
                    output = in1 % in2
                except ZeroDivisionError as er:
                    self.displayWarning('ZeroDivisionError: {}'.format(er), index)
                    output = 0.0
            elif operation == 9:
                output = in1
            elif operation == 10:
                output = in2
            else:
                raise ValueError('Invalid operation value: {}'.format(operation))
            output_handle.setDouble(output)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prDoubleLinear.nodeTypeName, prDoubleLinear.nodeTypeId,
                              prDoubleLinear.creator, prDoubleLinear.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prDoubleLinear.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prDoubleLinear.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prDoubleLinear.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprDoubleLinearTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prDoubleLinear Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
