"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Same as multiplyDivide node, but with array versions of input1, input2, output.
The only difference is errors result in output 0.0 instead of NaN:
- zero division
- negative numbers with a fractional power
Purpose of this node:
- reduce number of nodes by replacing multiple multiplyDivide nodes with this one

USE CASES
...

USAGE
(MEL): createNode prMultiplyDivide

ATTRIBUTES
prMultiplyDivide1.input[0].input1.input1X
prMultiplyDivide1.input[0].input1.input1Y
prMultiplyDivide1.input[0].input1.input1Z
prMultiplyDivide1.input[0].input2.input2X
prMultiplyDivide1.input[0].input2.input2Y
prMultiplyDivide1.input[0].input2.input2Z
prMultiplyDivide1.output[0].outputX
prMultiplyDivide1.output[0].outputY
prMultiplyDivide1.output[0].outputZ

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- custom aeTemplate for prMultiplyDivide.input
- node behavior attrs
- icons

"""

import sys

import maya.api.OpenMaya as om


class prMultiplyDivide(om.MPxNode):
    nodeTypeName = "prMultiplyDivide"
    nodeTypeId = om.MTypeId(0x0004C265)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()

        # output
        prMultiplyDivide.output = numericAttr.createPoint('output', 'output')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prMultiplyDivide.addAttribute(prMultiplyDivide.output)

        # input
        prMultiplyDivide.operation = enumAttr.create('operation', 'operation', 1)
        enumAttr.keyable = True
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Multiply', 1)
        enumAttr.addField('Divide', 2)
        enumAttr.addField('Power', 3)
        prMultiplyDivide.addAttribute(prMultiplyDivide.operation)
        prMultiplyDivide.attributeAffects(prMultiplyDivide.operation, prMultiplyDivide.output)
        
        prMultiplyDivide.input1 = numericAttr.createPoint('input1', 'input1')
        numericAttr.keyable = True

        prMultiplyDivide.input2 = numericAttr.createPoint('input2', 'input2')
        numericAttr.keyable = True

        prMultiplyDivide.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prMultiplyDivide.input1)
        compoundAttr.addChild(prMultiplyDivide.input2)
        compoundAttr.array = True
        prMultiplyDivide.addAttribute(prMultiplyDivide.input)
        prMultiplyDivide.attributeAffects(prMultiplyDivide.input1, prMultiplyDivide.output)
        prMultiplyDivide.attributeAffects(prMultiplyDivide.input2, prMultiplyDivide.output)

    @staticmethod
    def creator():
        return prMultiplyDivide()

    def __init__(self):
        om.MPxNode.__init__(self)

    def displayError(self, index, error):
        nodeName = om.MFnDependencyNode(self.thisMObject()).name()
        message = '{0}: "{1}.input[{2}]"'.format(error, nodeName, index)
        om.MGlobal.displayError(message)

    def compute(self, plug, dataBlock):
        if plug not in [self.output]:
            print 'unknown plug: {}'.format(plug)
            return
        operation = dataBlock.inputValue(self.operation).asShort()

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()

        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)  # old api: jumpToArrayElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            inputTargetHandle = inputArrayHandle.inputValue()
            in1 = inputTargetHandle.child(self.input1).asFloat3()
            in2 = inputTargetHandle.child(self.input2).asFloat3()
            if operation == 0:
                output = in1
            elif operation == 1:
                output = [in1[0] * in2[0], in1[1] * in2[1], in1[2] * in2[2]]
            elif operation == 2:
                output = []
                er = None
                for input1, input2 in zip(in1, in2):
                    try:
                        output.append(input1 / input2)
                    except ZeroDivisionError as er:
                        output.append(0.0)
                if er:
                    self.displayError(index, er)
            elif operation == 3:
                output = []
                er = None
                for input1, input2 in zip(in1, in2):
                    try:
                        output.append(input1 ** input2)
                    except ValueError as er:
                        output.append(0.0)
                if er:
                    self.displayError(index, er)
            else:
                raise ValueError('operation: {}'.format(operation))
            output_handle = output_builder.addElement(index)
            output_handle.set3Float(*output)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prMultiplyDivide.nodeTypeName, prMultiplyDivide.nodeTypeId,
                              prMultiplyDivide.creator, prMultiplyDivide.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prMultiplyDivide.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prMultiplyDivide.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prMultiplyDivide.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprMultiplyDivideTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prMultiplyDivide Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
