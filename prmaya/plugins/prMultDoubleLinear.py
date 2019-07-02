"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Same as multDoubleLinear node, but with array versions of input1, input2, output.
Purpose of this node:
- reduce number of nodes by replacing multiple multDoubleLinear nodes with this one

USE CASES
...

USAGE
(MEL): createNode prMultDoubleLinear

ATTRIBUTES
mdl.input[0].input1
mdl.input[0].input2
mdl.output[0]

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- custom aeTemplate for prMultDoubleLinear.input
- node behavior attrs
- icons

"""

import sys

import maya.api.OpenMaya as om


class prMultDoubleLinear(om.MPxNode):
    nodeTypeName = "prMultDoubleLinear"
    nodeTypeId = om.MTypeId(0x0004C266)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        compoundAttr = om.MFnCompoundAttribute()

        # output
        prMultDoubleLinear.output = numericAttr.create('output', 'output', om.MFnNumericData.kFloat)
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prMultDoubleLinear.addAttribute(prMultDoubleLinear.output)

        # input
        prMultDoubleLinear.input1 = numericAttr.create('input1', 'input1', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True

        prMultDoubleLinear.input2 = numericAttr.create('input2', 'input2', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True

        prMultDoubleLinear.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prMultDoubleLinear.input1)
        compoundAttr.addChild(prMultDoubleLinear.input2)
        compoundAttr.array = True
        prMultDoubleLinear.addAttribute(prMultDoubleLinear.input)
        prMultDoubleLinear.attributeAffects(prMultDoubleLinear.input1, prMultDoubleLinear.output)
        prMultDoubleLinear.attributeAffects(prMultDoubleLinear.input2, prMultDoubleLinear.output)

    @staticmethod
    def creator():
        return prMultDoubleLinear()

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

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()

        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)  # old api: jumpToArrayElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            inputTargetHandle = inputArrayHandle.inputValue()
            in1 = inputTargetHandle.child(self.input1).asFloat()
            in2 = inputTargetHandle.child(self.input2).asFloat()
            output_handle = output_builder.addElement(index)
            output_handle.setFloat(in1 * in2)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prMultDoubleLinear.nodeTypeName, prMultDoubleLinear.nodeTypeId,
                              prMultDoubleLinear.creator, prMultDoubleLinear.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prMultDoubleLinear.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prMultDoubleLinear.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prMultDoubleLinear.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprMultDoubleLinearTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prMultDoubleLinear Attributes" -collapse 0;
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
