"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Creates a list of scalars between two values with even spacing.

USE CASES
- Evenly distribute transforms nodes on a curve (motionPath1.uValue, ...)

USAGE
...

ATTRIBUTES
prScalarArithmetic1.inputMin
prScalarArithmetic1.inputMax
prScalarArithmetic1.inputSampleCount
prScalarArithmetic1.output[0]

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
...

"""

import sys

import maya.api.OpenMaya as om


class prRange(om.MPxNode):
    nodeTypeName = "prRange"
    nodeTypeId = om.MTypeId(0x0004C264)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()

        # output
        prRange.output = numericAttr.create('output', 'output', om.MFnNumericData.kFloat)
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prRange.addAttribute(prRange.output)

        # input
        prRange.inputMin = numericAttr.create('inputMin', 'inputMin', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prRange.addAttribute(prRange.inputMin)
        prRange.attributeAffects(prRange.inputMin, prRange.output)

        prRange.inputMax = numericAttr.create('inputMax', 'inputMax', om.MFnNumericData.kFloat, 1.0)
        numericAttr.keyable = True
        prRange.addAttribute(prRange.inputMax)
        prRange.attributeAffects(prRange.inputMax, prRange.output)

        prRange.inputSampleCount = numericAttr.create('inputSampleCount', 'inputSampleCount', om.MFnNumericData.kInt)
        numericAttr.keyable = True
        numericAttr.setMin(0)
        numericAttr.setSoftMax(20)
        prRange.addAttribute(prRange.inputSampleCount)
        prRange.attributeAffects(prRange.inputSampleCount, prRange.output)

    @staticmethod
    def creator():
        return prRange()

    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug, dataBlock):
        if plug not in [self.output]:
            print 'unknown plug: {}'.format(plug)
            return

        inputMin = dataBlock.inputValue(prRange.inputMin).asFloat()
        inputMax = dataBlock.inputValue(prRange.inputMax).asFloat()

        output_arrayHandle = dataBlock.outputArrayValue(prRange.output)
        output_builder = output_arrayHandle.builder()

        inputSampleCount = dataBlock.inputValue(prRange.inputSampleCount).asShort()
        for index in range(inputSampleCount):
            output_handle = output_builder.addElement(index)
            output = inputMin + ((inputMax - inputMin) / ((inputSampleCount - 1) or 1)) * index
            output_handle.setFloat(output)

        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()

        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prRange.nodeTypeName, prRange.nodeTypeId,
                              prRange.creator, prRange.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prRange.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prRange.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prRange.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprRangeTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prRange Attributes" -collapse 0;
                editorTemplate -label "inputMin" -addControl "inputMin";
                editorTemplate -label "inputMax" -addControl "inputMax";
                editorTemplate -label "inputSampleCount" -addControl "inputSampleCount";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
