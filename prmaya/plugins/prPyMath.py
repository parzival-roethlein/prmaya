"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
The Python math module as Maya node.

USE CASES
Random idea, probably not for production.

ATTRIBUTES
1. data
math.e = prPyMath1.e
math.pi = prPyMath1.pi
2. functions
functions = prPyMath1.func : which function should evaluate
arguments = prPyMath1.x, prPyMath1.y, prPyMath1.i, prPyMath1.base, prPyMath1.iterable
return = prPyMath1.result, prPyMath1.result1 (result1 is only used for second element of the tuple returned by the functions math.modf and math.frexp)
3. extra maya utility
xDegreesToRadians : will convert argument.x value from degrees (maya rotation value for example) to radians (what the math module uses)
ignoreErrors : if enabled will ignore ValueErrors on function calls

LINKS
- Demo:
TODO
- Making-of:
https://pazrot3d.blogspot.com/2018/10/prpymathpy-making-of.html
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- nodeState / frozen
- remove AEprPyMathTemplate_iterableNodeTextField and replace it with something like global mel variable
TODO MAYBE
- is the argument compound attribute maya style?
- check other arguments than x if they could use degreesToRadians option (check functions)
- arguments of MFnUnitAttribute type
- check why maya result attribute value is so inaccurate: round(x, 6) or round(x, 5) is needed to match math module results
- create docstring: copy from math module (?) + new maya utility
"""

import math
import sys

import maya.api.OpenMaya as om

FUNCTION_DATA = None


class prPyMath(om.MPxNode):
    nodeTypeName = "prPyMath"
    nodeTypeId = om.MTypeId(0x0004C260)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()

        # OUTPUT
        prPyMath.result = numericAttr.create('result', 'result', om.MFnNumericData.kFloat, 0.0)
        numericAttr.storable = False
        numericAttr.writable = False
        prPyMath.addAttribute(prPyMath.result)

        prPyMath.result1 = numericAttr.create('result1', 'result1', om.MFnNumericData.kFloat, 0.0)
        numericAttr.storable = False
        numericAttr.writable = False
        prPyMath.addAttribute(prPyMath.result1)

        # DATA
        prPyMath.e = numericAttr.create('e', 'e', om.MFnNumericData.kFloat, math.e)
        numericAttr.storable = False
        numericAttr.writable = False
        prPyMath.addAttribute(prPyMath.e)

        prPyMath.pi = numericAttr.create('pi', 'pi', om.MFnNumericData.kFloat, math.pi)
        numericAttr.storable = False
        numericAttr.writable = False
        prPyMath.addAttribute(prPyMath.pi)

        # FUNCTIONS
        prPyMath.func = enumAttr.create('function', 'function', 0)
        for index, data in getMathFunctionData().iteritems():
            enumAttr.addField(data['name'], index)
        enumAttr.keyable = True
        prPyMath.addAttribute(prPyMath.func)
        prPyMath.attributeAffects(prPyMath.func, prPyMath.result)
        prPyMath.attributeAffects(prPyMath.func, prPyMath.result1)

        # ARGUMENTS
        prPyMath.x = numericAttr.create('x', 'x', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prPyMath.addAttribute(prPyMath.x)
        prPyMath.attributeAffects(prPyMath.x, prPyMath.result)
        prPyMath.attributeAffects(prPyMath.x, prPyMath.result1)

        prPyMath.y = numericAttr.create('y', 'y', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prPyMath.addAttribute(prPyMath.y)
        prPyMath.attributeAffects(prPyMath.y, prPyMath.result)

        prPyMath.i = numericAttr.create('i', 'i', om.MFnNumericData.kInt, 0.0)
        numericAttr.keyable = True
        prPyMath.addAttribute(prPyMath.i)
        prPyMath.attributeAffects(prPyMath.i, prPyMath.result)

        prPyMath.base = numericAttr.create('base', 'base', om.MFnNumericData.kFloat, math.e)
        numericAttr.keyable = True
        prPyMath.addAttribute(prPyMath.base)
        prPyMath.attributeAffects(prPyMath.base, prPyMath.result)

        prPyMath.iterable = numericAttr.create('iterable', 'iterable', om.MFnNumericData.kFloat)
        numericAttr.array = True
        prPyMath.addAttribute(prPyMath.iterable)
        prPyMath.attributeAffects(prPyMath.iterable, prPyMath.result)

        prPyMath.arguments = compoundAttr.create('arguments', 'arguments')
        compoundAttr.addChild(prPyMath.x)
        compoundAttr.addChild(prPyMath.y)
        compoundAttr.addChild(prPyMath.i)
        compoundAttr.addChild(prPyMath.base)
        compoundAttr.addChild(prPyMath.iterable)
        prPyMath.addAttribute(prPyMath.arguments)

        # UTILITY
        prPyMath.xDegreesToRadians = numericAttr.create('xDegreesToRadians', 'xDegreesToRadians', om.MFnNumericData.kBoolean, False)
        prPyMath.addAttribute(prPyMath.xDegreesToRadians)
        prPyMath.attributeAffects(prPyMath.xDegreesToRadians, prPyMath.result)
        prPyMath.attributeAffects(prPyMath.xDegreesToRadians, prPyMath.result1)
        
        prPyMath.ignoreErrors = numericAttr.create('ignoreErrors', 'ignoreErrors', om.MFnNumericData.kBoolean, False)
        prPyMath.addAttribute(prPyMath.ignoreErrors)

        prPyMath.resultDefault = numericAttr.create('resultDefault', 'resultDefault', om.MFnNumericData.kFloat, 0.0)
        prPyMath.addAttribute(prPyMath.resultDefault)
        prPyMath.attributeAffects(prPyMath.resultDefault, prPyMath.result)

        prPyMath.result1Default = numericAttr.create('result1Default', 'result1Default', om.MFnNumericData.kFloat, 0.0)
        prPyMath.addAttribute(prPyMath.result1Default)
        prPyMath.attributeAffects(prPyMath.result1Default, prPyMath.result1)
        
    @staticmethod
    def creator():
        return prPyMath()

    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug, data):
        if plug == prPyMath.e:
            data.outputValue(prPyMath.e).setFloat(math.e)
            data.setClean(plug)
            return
        elif plug == prPyMath.pi:
            data.outputValue(prPyMath.pi).setFloat(math.pi)
            data.setClean(plug)
            return
        elif plug != prPyMath.result and plug != prPyMath.result1:
            return None
        
        resultDefault = data.inputValue(prPyMath.resultDefault).asFloat()
        result1Default = data.inputValue(prPyMath.result1Default).asFloat()
        
        ignoreErrors = data.inputValue(prPyMath.ignoreErrors).asBool()
        
        funcIndex = data.inputValue(prPyMath.func).asChar()
        func = getMathFunctionData()[funcIndex]
        
        args = []
        for kwarg in func['kwargs']:
            if kwarg == 'x':
                x = data.inputValue(prPyMath.x).asFloat()
                if data.inputValue(prPyMath.xDegreesToRadians).asBool():
                    x = math.radians(x)
                args.append(x)
            elif kwarg == 'y':
                args.append(data.inputValue(prPyMath.y).asFloat())
            elif kwarg == 'i':
                args.append(data.inputValue(prPyMath.i).asInt())
            elif kwarg == 'base':
                args.append(data.inputValue(prPyMath.base).asFloat())
            elif kwarg == 'iterable':
                arg = []
                iterableHandle = data.inputArrayValue(prPyMath.iterable)
                while not iterableHandle.isDone():
                    arg.append(iterableHandle.inputValue().asFloat())
                    iterableHandle.next()
                args.append(arg)
            else:
                raise ValueError('Unknown argument: {0}'.format(kwarg))

        try:
            result = func['function'](*args)
            if isinstance(result, tuple):
                result, result1 = result
            else:
                result1 = result1Default
        except ValueError as error:
            result = resultDefault
            result1 = result1Default
        else:
            error = None
        if plug == prPyMath.result:
            resultHandle = data.outputValue(prPyMath.result)
            resultHandle.setFloat(result)
        elif plug == prPyMath.result1:
            result1Handle = data.outputValue(prPyMath.result1)
            result1Handle.setFloat(result1)
        data.setClean(plug)

        if error and not ignoreErrors:
            raise ValueError('{0} : {1}({2})'.format(error, func['name'], dict(zip(func['kwargs'], args))))


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prPyMath.nodeTypeName, prPyMath.nodeTypeId, prPyMath.creator, prPyMath.initialize)
    except:
        sys.stderr.write('Failed to register node: %s' % prPyMath.nodeTypeName)
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prPyMath.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: %s' % prPyMath.nodeTypeName)
        raise


def maya_useNewAPI():
    pass


def getMathFunctionData():
    global FUNCTION_DATA
    if not FUNCTION_DATA:
        FUNCTION_DATA = {}
        index = 0
        for name in dir(math):
            func = getattr(math, name)
            if not str(func).startswith('<built-in function '):
                continue
            d = func.__doc__
            kwargs = d[d.find('(') + 1:d.find(')')]
            for obsolete in ['[', ']', ':Real']:
                kwargs = kwargs.replace(obsolete, '')
            kwargs = kwargs.split(', ')
            FUNCTION_DATA[index] = {'name': name, 'kwargs': kwargs, 'function': func}
            index += 1
    return FUNCTION_DATA


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprPyMathTemplate_iterableCreateElement()
    {
        string $node = `textField -q -text "AEprPyMathTemplate_iterableNodeTextField"`;
        string $attribute = $node+".iterable";
        int $indices[] = `getAttr -multiIndices $attribute`;
        int $indexSize = size($indices);
        int $newIndex = 0;
        if ($indexSize != 0){
            $newIndex = $indices[$indexSize-1]+1;
        }
        setAttr ($attribute+"["+$newIndex+"]") 0;
    };
    
    global proc AEprPyMathTemplate_iterableDeleteElement()
    {
        string $node = `textField -q -text "AEprPyMathTemplate_iterableNodeTextField"`;
        int $index = `intField -q -value "AEprPyMathTemplate_iterableDeleteItemIntField"`;
        string $attribute = $node+".iterable";
        removeMultiInstance ($attribute+"["+$index+"]");

    };
    
    global proc AEprPyMathTemplate_iterableBuild(string $plug)
    {
        rowLayout -numberOfColumns 4 -columnWidth4 1 100 100 100;
        textField -editable 0 "AEprPyMathTemplate_iterableNodeTextField";
        button -l "Create element" -c "AEprPyMathTemplate_iterableCreateElement";
        button -l "Delete element:" -c "AEprPyMathTemplate_iterableDeleteElement";
        intField -minValue 0 -value 0 "AEprPyMathTemplate_iterableDeleteItemIntField";
        setParent ..;
        AEprPyMathTemplate_iterableUpdate($plug);
    };
    
    global proc AEprPyMathTemplate_iterableUpdate(string $plug)
    {
        string $nodeAttr[];
        tokenize($plug, ".", $nodeAttr);
        textField -e -text $nodeAttr[0] "AEprPyMathTemplate_iterableNodeTextField";
    };
    
    global proc AEprPyMathTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prPyMath Attributes" -collapse 0;
                editorTemplate -label "function" -addControl "function";
                //editorTemplate -label "arguments" -addControl "arguments";
                //sadly does not display array iterable indices correctly when deleting/creating
                editorTemplate -beginLayout "arguments" -collapse 0;
                    editorTemplate -label "x" -addControl "x";
                    editorTemplate -label "y" -addControl "y";
                    editorTemplate -label "i" -addControl "i";
                    editorTemplate -label "base" -addControl "base";
                    editorTemplate -beginLayout "iterable" -collapse 0;
                        editorTemplate -callCustom "AEprPyMathTemplate_iterableBuild" "AEprPyMathTemplate_iterableUpdate" "iterable";
                        editorTemplate -label "iterable items" -addControl "iterable";
                    editorTemplate -endLayout;
                editorTemplate -endLayout;
                editorTemplate -beginLayout "maya utility" -collapse 0;
                    editorTemplate -label "xDegreesToRadians" -addControl "xDegreesToRadians";
                    editorTemplate -label "ignoreErrors" -addControl "ignoreErrors";
                    editorTemplate -label "resultDefault" -addControl "resultDefault";
                    editorTemplate -label "result1Default" -addControl "result1Default";
                editorTemplate -endLayout;
            editorTemplate -endLayout;
        AEdependNodeTemplate $nodeName;
        editorTemplate -suppress "arguments";
        editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')

