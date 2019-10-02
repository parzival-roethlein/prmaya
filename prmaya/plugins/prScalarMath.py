"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Binary (pair) math operators for array of scalars that return a scalar.
Similar to Maya nodes:
- addDoubleLinear
- multDoubleLinear
- plusMinusAverage
- multiplyDivide

USE CASES
Reduce the number of nodes in the scene by replacing multiple Maya math utility
nodes with fewer prScalarMath nodes.
Added missing operators: Modulus, floor division, ...

USAGE
(MEL): createNode prScalarMath

ATTRIBUTES
prScalarMath1.input[0].input1 (double)
prScalarMath1.input[0].input2 (double)
prScalarMath1.output[0] (double)
prScalarMath1.operation (enum)
- 0, No operation: forward input1. Same as multiplyDivide
- 1, Sum +: Same as plusMinusAverage / addDoubleLinear
- 2, Subtract -: Same as plusMinusAverage
- 3, Average: Same as plusMinusAverage
- 4, Multiply *: Same as multiplyDivide / multDoubleLinear
- 5, Division: Same as multiplyDivide, except:
               If ZeroDivisionError outputs 0.0, multiplyDivide outputs 100000
- 6, Power: Same as multiplyDivide, except:
            Negative number with fractional power gives error and outputs 0.0.
            multiplyDivide node does not error and outputs NaN value
- 7, Root: input1 ** (1.0/input2)
- 8, Floor division //: input1 // input2
- 9, Modulus: input1 % input2

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- custom aeTemplate for prScalarMath.input
- node behavior attrs
- name alternatives: scalar/double, linear / math>algebra>arithmetic, binary operation
  -> prDoubleLinear, prDoubleArithmetic
  -> prScalarAlgebra, prScalarMath, prScalarBinaryOp

"""

import sys

import maya.api.OpenMaya as om


class prScalarMath(om.MPxNode):
    nodeTypeName = "prScalarMath"
    nodeTypeId = om.MTypeId(0x0004C266)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        enumAttr = om.MFnEnumAttribute()

        # output
        prScalarMath.output = numericAttr.create('output', 'output', om.MFnNumericData.kDouble)
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prScalarMath.addAttribute(prScalarMath.output)

        # input
        prScalarMath.operation = enumAttr.create('operation', 'operation', 3)
        enumAttr.keyable = True
        # operation names from maya nodes (plusMinusAverage, multiplyDivide)
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Sum +', 1)
        enumAttr.addField('Subtract -', 2)
        enumAttr.addField('Average', 3)
        enumAttr.addField('Multiply *', 4)
        enumAttr.addField('Divide /', 5)
        enumAttr.addField('Power ^', 6)
        enumAttr.addField('Root', 7)
        enumAttr.addField('Floor division //', 8)
        enumAttr.addField('Modulus %', 9)
        prScalarMath.addAttribute(prScalarMath.operation)
        prScalarMath.attributeAffects(prScalarMath.operation, prScalarMath.output)

        prScalarMath.input1 = numericAttr.create('input1', 'input1', om.MFnNumericData.kDouble, 0.0)
        numericAttr.keyable = True

        prScalarMath.input2 = numericAttr.create('input2', 'input2', om.MFnNumericData.kDouble, 1.0)
        numericAttr.keyable = True

        prScalarMath.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prScalarMath.input1)
        compoundAttr.addChild(prScalarMath.input2)
        compoundAttr.array = True
        prScalarMath.addAttribute(prScalarMath.input)
        prScalarMath.attributeAffects(prScalarMath.input1, prScalarMath.output)
        prScalarMath.attributeAffects(prScalarMath.input2, prScalarMath.output)

    @staticmethod
    def creator():
        return prScalarMath()

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
                output = in1
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
                output = in1 ** (1.0/in2)
            elif operation == 8:
                try:
                    output = in1 // in2
                except ZeroDivisionError as er:
                    self.displayWarning('ZeroDivisionError: {}'.format(er), index)
                    output = 0.0
            elif operation == 9:
                try:
                    output = in1 % in2
                except ZeroDivisionError as er:
                    self.displayWarning('ZeroDivisionError: {}'.format(er), index)
                    output = 0.0
            else:
                raise ValueError('Invalid operation value: {}'.format(operation))
            output_handle.setDouble(output)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prScalarMath.nodeTypeName, prScalarMath.nodeTypeId,
                              prScalarMath.creator, prScalarMath.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prScalarMath.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prScalarMath.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prScalarMath.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprScalarMathTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prScalarMath Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
