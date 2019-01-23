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

        prRemapValue.isNodeInitialized = numericAttr.create('isNodeInitialized', 'isNodeInitialized', om.MFnNumericData.kBoolean, False)
        numericAttr.hidden = True
        numericAttr.connectable = False
        #numericAttr.writable = False
        #numericAttr.storable = True
        prRemapValue.addAttribute(prRemapValue.isNodeInitialized)

    @staticmethod
    def creator():
        return prRemapValue()
    
    def __init__(self):
        om.MPxNode.__init__(self)

    '''
    def postConstructor(self, *args, **kwargs):
        print('postConstructor: {} {}'.format(self, prRemapValue.isNodeInitialized))
        thisNode = self.thisMObject()
        plug = om.MPlug(thisNode, prRemapValue.isNodeInitialized)
        isNodeInitialized = plug.asBool()
        print plug.asBool()
        if not isNodeInitialized:
            print('initializing')
            plug.setBool(True)
        else:
            print 'did not initialize'
        print plug.asBool()
    '''

    def postConstructor(self, *args, **kwargs):

        def initialize_ramp():
            print('initialize_ramp: {} {}'.format(self, prRemapValue.isNodeInitialized))
            thisNode = self.thisMObject()
            plug = om.MPlug(thisNode, prRemapValue.isNodeInitialized)
            isNodeInitialized = plug.asBool()
            print plug.asBool()
            if not isNodeInitialized:
                print('initializing')
                plug.setBool(True)
            else:
                print 'did not initialize'
            print plug.asBool()
        mc.evalDeferred(initialize_ramp, evaluateNext=True)

    def compute(self, plug, dataBlock):
        thisNode = self.thisMObject()
        if plug not in [self.outValue]:
            print 'unknown plug: {}'.format(plug)
            return

        '''
        isNodeInitialized_handle = dataBlock.outputValue(prRemapValue.isNodeInitialized)
        print '\ncompute'
        print isNodeInitialized_handle.asBool()
        if not isNodeInitialized_handle.asBool():
            print('compute initialize')
            isNodeInitialized_handle.setBool(True)
        else:
            print('compute did not initialize')
        print isNodeInitialized_handle.asBool()
        '''

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


# CALLBACK_ID = None
def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prRemapValue.nodeTypeName, prRemapValue.nodeTypeId,
                              prRemapValue.creator, prRemapValue.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prRemapValue.nodeTypeName))
        raise
    evalAETemplate()

    '''def bla(*args, **kwargs):
        print('\n\n ----- args: {}\n ----- kwargs: // {}\n\n'.format(args, kwargs))
        mObject, none = args
        plug = om.MPlug(mObject, prRemapValue.isNodeInitialized)
        print 'before: {}'.format(plug.asBool())
        if not plug.asBool():
            print('initializing')
            plug.setBool(True)
        else:
            print 'did not initialize'
        print 'after: {}'.format(plug.asBool())
    global CALLBACK_ID
    CALLBACK_ID = om.MDGMessage.addNodeAddedCallback(bla, 'prRemapValue')
    '''


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prRemapValue.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prRemapValue.nodeTypeName))
        raise
    #global CALLBACK_ID
    #om.MMessage.removeCallback(CALLBACK_ID)


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

