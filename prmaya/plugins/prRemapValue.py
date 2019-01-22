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
import math

import maya.api.OpenMaya as om
import maya.cmds as mc


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

        # input
        prRemapValue.inputValue = numericAttr.create('inputValue', 'inputValue', om.MFnNumericData.kFloat)
        numericAttr.array = True
        prRemapValue.addAttribute(prRemapValue.inputValue)
        prRemapValue.attributeAffects(prRemapValue.inputValue, prRemapValue.outValue)

        # settings
        prRemapValue.value = rampAttr.createCurveRamp('value', 'value')
        prRemapValue.addAttribute(prRemapValue.value)
        prRemapValue.attributeAffects(prRemapValue.value, prRemapValue.outValue)
    
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
        while not inputValue_arrayHandle.isDone():
            v = inputValue_arrayHandle.inputValue().asFloat()
            inputValue_arrayHandle.next()

        outValue_arrayHandle = dataBlock.outputArrayValue(prRemapValue.outValue)
        outValue_builder = outValue_arrayHandle.builder()

        value_handle = om.MRampAttribute(thisNode, prRemapValue.value)
        print value_handle

        for i in range(len(inputValue_arrayHandle)):
            inputValue_arrayHandle.jumpToPhysicalElement(i)
            index = inputValue_arrayHandle.elementLogicalIndex()
            inputValue = inputValue_arrayHandle.inputValue().asFloat()

            outValue_handle = outValue_builder.addElement(index)
            outValue_arrayHandle.set(outValue_builder)
            v = value_handle.getValueAtPosition(inputValue)
            outValue_handle.setFloat(v)
            print v

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
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "output";
    };
    ''')

