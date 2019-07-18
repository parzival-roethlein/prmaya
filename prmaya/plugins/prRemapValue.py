"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Array version of Mayas remapValue node: inputValue[], outValue[], outColor[]
Purpose: Scalable, procedural, convenient, simplify

USE CASES
...

USAGE
...

ATTRIBUTES
...

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- improved custom aetemplate inputValue
- node behavior attrs
- icon

"""

import sys

import maya.api.OpenMaya as om


class prRemapValue(om.MPxNode):
    nodeTypeName = "prRemapValue"
    nodeTypeId = om.MTypeId(0x0004C263)  # local, not save
    
    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        rampAttr = om.MRampAttribute()

        # output
        prRemapValue.outValue = numericAttr.create('outValue', 'outValue', om.MFnNumericData.kFloat)
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prRemapValue.addAttribute(prRemapValue.outValue)

        prRemapValue.outColor = numericAttr.createColor('outColor', 'outColor')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prRemapValue.addAttribute(prRemapValue.outColor)
        
        # input
        prRemapValue.inputMin = numericAttr.create('inputMin', 'inputMin', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.inputMin)
        prRemapValue.attributeAffects(prRemapValue.inputMin, prRemapValue.outValue)
        prRemapValue.attributeAffects(prRemapValue.inputMin, prRemapValue.outColor)

        prRemapValue.inputMax = numericAttr.create('inputMax', 'inputMax', om.MFnNumericData.kFloat, 1.0)
        numericAttr.keyable = True
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.inputMax)
        prRemapValue.attributeAffects(prRemapValue.inputMax, prRemapValue.outValue)
        prRemapValue.attributeAffects(prRemapValue.inputMax, prRemapValue.outColor)

        prRemapValue.outputMin = numericAttr.create('outputMin', 'outputMin', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.outputMin)
        prRemapValue.attributeAffects(prRemapValue.outputMin, prRemapValue.outValue)
        prRemapValue.attributeAffects(prRemapValue.outputMin, prRemapValue.outColor)

        prRemapValue.outputMax = numericAttr.create('outputMax', 'outputMax', om.MFnNumericData.kFloat, 1.0)
        numericAttr.keyable = True
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.outputMax)
        prRemapValue.attributeAffects(prRemapValue.outputMax, prRemapValue.outValue)
        prRemapValue.attributeAffects(prRemapValue.outputMax, prRemapValue.outColor)

        prRemapValue.inputValue = numericAttr.create('inputValue', 'inputValue', om.MFnNumericData.kFloat)
        numericAttr.array = True
        numericAttr.keyable = True
        prRemapValue.addAttribute(prRemapValue.inputValue)
        prRemapValue.attributeAffects(prRemapValue.inputValue, prRemapValue.outValue)
        prRemapValue.attributeAffects(prRemapValue.inputValue, prRemapValue.outColor)

        prRemapValue.value = rampAttr.createCurveRamp('value', 'value')
        prRemapValue.addAttribute(prRemapValue.value)
        prRemapValue.attributeAffects(prRemapValue.value, prRemapValue.outValue)

        prRemapValue.color = rampAttr.createColorRamp('color', 'color')
        prRemapValue.addAttribute(prRemapValue.color)
        prRemapValue.attributeAffects(prRemapValue.color, prRemapValue.outColor)

    # def shouldSave(self, plug, result):
    #     if plug == self.inputValue:
    #         return True
    #     return om.MPxNode.shouldSave(self, plug, result)
    
    @staticmethod
    def creator():
        return prRemapValue()
    
    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug, dataBlock):
        thisNode = self.thisMObject()
        if plug not in [self.outValue, self.outColor]:
            print 'unknown plug: {}'.format(plug)
            return

        inputMin = dataBlock.inputValue(prRemapValue.inputMin).asFloat()
        inputMax = dataBlock.inputValue(prRemapValue.inputMax).asFloat()
        outputMin = dataBlock.inputValue(prRemapValue.outputMin).asFloat()
        outputMax = dataBlock.inputValue(prRemapValue.outputMax).asFloat()

        value_handle = om.MRampAttribute(thisNode, prRemapValue.value)
        outValue_arrayHandle = dataBlock.outputArrayValue(prRemapValue.outValue)
        outValue_builder = outValue_arrayHandle.builder()

        color_handle = om.MRampAttribute(thisNode, prRemapValue.color)
        outColor_arrayHandle = dataBlock.outputArrayValue(prRemapValue.outColor)
        outColor_builder = outColor_arrayHandle.builder()
        
        sampleValues = {}
        inputValue_arrayHandle = dataBlock.inputArrayValue(prRemapValue.inputValue)
        for i in range(len(inputValue_arrayHandle)):
            inputValue_arrayHandle.jumpToPhysicalElement(i)
            index = inputValue_arrayHandle.elementLogicalIndex()
            inputValue = inputValue_arrayHandle.inputValue().asFloat()
            sampleValues[index] = inputValue

        for index, value in sampleValues.iteritems():
            outValue_handle = outValue_builder.addElement(index)
            outColor_handle = outColor_builder.addElement(index)
            
            if inputMin == inputMax:
                rampPosition = 0.0
            else:
                rampPosition = (value - inputMin) / (inputMax - inputMin)

            valueRampValue = value_handle.getValueAtPosition(rampPosition)
            outValue = outputMin * (1 - valueRampValue) + outputMax * valueRampValue
            outValue_handle.setFloat(outValue)

            colorRampValue = color_handle.getValueAtPosition(rampPosition)
            for x, colorValue in enumerate(colorRampValue):
                colorRampValue[x] = outputMin * (1 - colorValue) + outputMax * colorValue

            outColor_handle.set3Float(colorRampValue[0],
                                      colorRampValue[1],
                                      colorRampValue[2])

        outValue_arrayHandle.set(outValue_builder)
        outValue_arrayHandle.setAllClean()
        outColor_arrayHandle.set(outColor_builder)
        outColor_arrayHandle.setAllClean()

        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prRemapValue.nodeTypeName, prRemapValue.nodeTypeId,
                              prRemapValue.creator, prRemapValue.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prRemapValue.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prRemapValue.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prRemapValue.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprRemapValueTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prRemapValue Attributes" -collapse 0;
                editorTemplate -label "inputValue" -addControl "inputValue";
                AEaddRampControl ($nodeName+".value");
                AEaddRampControl ($nodeName+".color");
            editorTemplate -endLayout;
            editorTemplate -beginLayout "Input and Output Ranges";
                editorTemplate -label "inputMin" -addControl "inputMin";
                editorTemplate -label "inputMax" -addControl "inputMax";
                editorTemplate -label "outputMin" -addControl "outputMin";
                editorTemplate -label "outputMax" -addControl "outputMax";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
