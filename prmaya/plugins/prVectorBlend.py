"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
array version of maya blendColors node.
difference: vector naming (input1X, ..) instead of color (color1R, ..)

USE CASES
...

USAGE
(MEL): createNode prVectorBlend

ATTRIBUTES
prBlendColors1.blender
prBlendColors1.normalizeOutput
prBlendColors1.input[0].input1
prBlendColors1.input[0].input1.input1X
prBlendColors1.input[0].input1.input1Y
prBlendColors1.input[0].input1.input1Z
prBlendColors1.input[0].input2
prBlendColors1.input[0].input2.input1X
prBlendColors1.input[0].input2.input1Y
prBlendColors1.input[0].input2.input1Z
prBlendColors1.output[0]
prBlendColors1.output[0].outputX
prBlendColors1.output[0].outputY
prBlendColors1.output[0].outputZ

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


class prVectorBlend(om.MPxNode):
    nodeTypeName = "prVectorBlend"
    nodeTypeId = om.MTypeId(0x0004C267)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()

        # output
        prVectorBlend.output = numericAttr.createPoint('output', 'output')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prVectorBlend.addAttribute(prVectorBlend.output)

        # input
        prVectorBlend.blender = numericAttr.create('blender', 'blender', om.MFnNumericData.kFloat, defaultValue=0.5)
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        numericAttr.keyable = True
        prVectorBlend.addAttribute(prVectorBlend.blender)
        prVectorBlend.attributeAffects(prVectorBlend.blender, prVectorBlend.output)

        prVectorBlend.normalizeOutput = numericAttr.create('normalizeOutput', 'normalizeOutput', om.MFnNumericData.kBoolean, False)
        numericAttr.keyable = True
        prVectorBlend.addAttribute(prVectorBlend.normalizeOutput)
        prVectorBlend.attributeAffects(prVectorBlend.normalizeOutput, prVectorBlend.output)

        prVectorBlend.input1 = numericAttr.createPoint('input1', 'input1')
        numericAttr.keyable = True

        prVectorBlend.input2 = numericAttr.createPoint('input2', 'input2')
        numericAttr.keyable = True

        prVectorBlend.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prVectorBlend.input1)
        compoundAttr.addChild(prVectorBlend.input2)
        compoundAttr.array = True
        prVectorBlend.addAttribute(prVectorBlend.input)
        prVectorBlend.attributeAffects(prVectorBlend.input1, prVectorBlend.output)
        prVectorBlend.attributeAffects(prVectorBlend.input2, prVectorBlend.output)

    @staticmethod
    def creator():
        return prVectorBlend()

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
        blender = dataBlock.inputValue(self.blender).asFloat()
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

            out = [in2[0] + blender * (in1[0] - in2[0]),
                   in2[1] + blender * (in1[1] - in2[1]),
                   in2[2] + blender * (in1[2] - in2[2])]
            if normalizeOutput:
                length = math.sqrt(out[0]**2 + out[1]**2 + out[2]**2)
                try:
                    out = [out[0] / length, out[1] / length, out[2] / length]
                except ZeroDivisionError:
                    out = [0.0, 0.0, 0.0]
            output_handle.set3Float(*out)
        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prVectorBlend.nodeTypeName, prVectorBlend.nodeTypeId,
                              prVectorBlend.creator, prVectorBlend.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prVectorBlend.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prVectorBlend.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prVectorBlend.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprVectorBlendTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prVectorBlend Attributes" -collapse 0;
                editorTemplate -label "blender" -addControl "blender";
                editorTemplate -label "normalizeOutput" -addControl "normalizeOutput";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
