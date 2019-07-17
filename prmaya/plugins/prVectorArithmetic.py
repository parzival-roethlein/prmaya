"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Basic math for array of vector pairs.
Similar to Maya utility nodes, but for array. Same as multiplyDivide node, but with array versions of input1, input2, output.

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

import maya.api.OpenMaya as om


class prVector(om.MPxNode):
    nodeTypeName = "prVector"
    nodeTypeId = om.MTypeId(0x0004C265)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()

        # output
        prVector.output = numericAttr.createPoint('output', 'output')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prVector.addAttribute(prVector.output)

        # input
        prVector.operation = enumAttr.create('operation', 'operation', 3)
        enumAttr.keyable = True
        enumAttr.addField('No operation', 0)
        enumAttr.addField('Sum +', 1)
        enumAttr.addField('Subtract -', 2)
        enumAttr.addField('Average', 3)
        enumAttr.addField('Cross product X', 4)
        enumAttr.addField('Projection', 5)

        prVector.addAttribute(prVector.operation)
        prVector.attributeAffects(prVector.operation, prVector.output)
        
        prVector.input1 = numericAttr.createPoint('input1', 'input1')
        numericAttr.keyable = True

        prVector.input2 = numericAttr.createPoint('input2', 'input2')
        numericAttr.keyable = True

        prVector.inputScalar = numericAttr.create('inputScalar', 'inputScalar', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True

        prVector.inputMatrix = numericAttr.create('inputMatrix', 'inputMatrix', om.MFnNumericData.kMatrix)
        numericAttr.keyable = True

        prVector.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prVector.input1)
        compoundAttr.addChild(prVector.input2)
        compoundAttr.addChild(prVector.inputScalar)
        compoundAttr.addChild(prVector.inputMatrix)
        compoundAttr.array = True
        prVector.addAttribute(prVector.input)
        prVector.attributeAffects(prVector.input1, prVector.output)
        prVector.attributeAffects(prVector.input2, prVector.output)
        prVector.attributeAffects(prVector.inputScalar, prVector.output)
        prVector.attributeAffects(prVector.inputMatrix, prVector.output)

    @staticmethod
    def creator():
        return prVector()

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
                    self.displayWarning(index, er)
            elif operation == 3:
                output = []
                er = None
                for input1, input2 in zip(in1, in2):
                    try:
                        output.append(input1 ** input2)
                    except ValueError as er:
                        output.append(0.0)
                if er:
                    self.displayWarning(index, er)
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
        pluginFn.registerNode(prVector.nodeTypeName, prVector.nodeTypeId,
                              prVector.creator, prVector.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prVector.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prVector.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prVector.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprVectorTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prVector Attributes" -collapse 0;
                editorTemplate -label "operation" -addControl "operation";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
