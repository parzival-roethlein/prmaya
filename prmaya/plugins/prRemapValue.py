"""
DESCRIPTION
array version of maya default remapValue node.
Everything should be the same except inputValue and outValue are arrays

USE CASES
...

USAGE
...

ATTRIBUTES
...

LINKS
...

TODO
...

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
        prRemapValue.inputValue = numericAttr.create('inputValue', 'inputValue', om.MFnNumericData.kFloat)
        numericAttr.array = True
        prRemapValue.addAttribute(prRemapValue.inputValue)
        prRemapValue.attributeAffects(prRemapValue.inputValue, prRemapValue.outValue)
        
        prRemapValue.inputMin = numericAttr.create('inputMin', 'inputMin', om.MFnNumericData.kFloat, 0.0)
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.inputMin)
        prRemapValue.attributeAffects(prRemapValue.inputMin, prRemapValue.outValue)
        
        prRemapValue.inputMax = numericAttr.create('inputMax', 'inputMax', om.MFnNumericData.kFloat, 1.0)
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.inputMax)
        prRemapValue.attributeAffects(prRemapValue.inputMax, prRemapValue.outValue)

        prRemapValue.outputMin = numericAttr.create('outputMin', 'outputMin', om.MFnNumericData.kFloat, 0.0)
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.outputMin)
        prRemapValue.attributeAffects(prRemapValue.outputMin, prRemapValue.outValue)

        prRemapValue.outputMax = numericAttr.create('outputMax', 'outputMax', om.MFnNumericData.kFloat, 1.0)
        numericAttr.setSoftMin(0.0)
        numericAttr.setSoftMax(1.0)
        prRemapValue.addAttribute(prRemapValue.outputMax)
        prRemapValue.attributeAffects(prRemapValue.outputMax, prRemapValue.outValue)
        
        prRemapValue.value = rampAttr.createCurveRamp('value', 'value')
        prRemapValue.addAttribute(prRemapValue.value)
        prRemapValue.attributeAffects(prRemapValue.value, prRemapValue.outValue)

        prRemapValue.color = rampAttr.createColorRamp('color', 'color')
        prRemapValue.addAttribute(prRemapValue.color)
        prRemapValue.attributeAffects(prRemapValue.color, prRemapValue.outColor)

    @staticmethod
    def creator():
        return prRemapValue()
    
    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug, dataBlock):
        thisNode = self.thisMObject()
        if plug not in [self.outValue]:
            print 'unknown plug: {}'.format(plug)
            return

        inputValue_arrayHandle = dataBlock.inputArrayValue(prRemapValue.inputValue)

        value_handle = om.MRampAttribute(thisNode, prRemapValue.value)

        outValue_arrayHandle = dataBlock.outputArrayValue(prRemapValue.outValue)
        outValue_builder = outValue_arrayHandle.builder()

        values = []
        for i in range(len(inputValue_arrayHandle)):
            inputValue_arrayHandle.jumpToPhysicalElement(i)
            index = inputValue_arrayHandle.elementLogicalIndex()
            inputValue = inputValue_arrayHandle.inputValue().asFloat()

            outValue_handle = outValue_builder.addElement(index)
            outValue = value_handle.getValueAtPosition(inputValue)
            outValue_handle.setFloat(outValue)
            values.append([inputValue, outValue])
        print(values)

        outValue_arrayHandle.set(outValue_builder)
        outValue_arrayHandle.setAllClean()
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
        editorTemplate -suppress "output";
        editorTemplate -suppress "outColor";
    };
    ''')

