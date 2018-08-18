"""
the python math module as maya node

1. DATA
math.e = prPyMath1.e
math.pi = prPyMath1.pi

2. FUNCTIONS
functions = prPyMath1.func : which function should evaluate
arguments = prPyMath1.x, prPyMath1.y, prPyMath1.i, prPyMath1.base, prPyMath1.iterable
return = prPyMath1.result, prPyMath1.result1 (used for second element of tuple return values of functions math.modf, math.frexp)

# TODO
- make DEFAULT_RESULT_VALUE and DEFAULT_RESULT_VALUE1 maya attributes
- detect new index when pressing "Delete item:" and index does not exist set to closest existing index (higher one if same distance to two indices)
  this always happens, also when deleting existing item, so it will not require double click every time
- option to convert input arguments from degrees to radians (maybe only relevant for x arg for all trig functions?)
- "iterable > node name" should not be shown in attribute editor. save node name as global variable?

# TODO MAYBE
- pi / e should not be settable and not be affected by other attributes but still show up as output (possible?)
- create docstring: copy from math module help?
- check why maya result attribute value is so inaccurate round(x, 6) or round(x, 5) needed to match math module
- generalized AEtemplate array build and update function, the textfield names have to be built from nodetype and attr name
- generalized MPxNode wrapper to easily make any python class a maya node?
  maybe better to just use an eval node http://around-the-corner.typepad.com/adn/2012/08/a-mathematical-dg-node.html

"""

import math
import sys

import maya.api.OpenMaya as om

DEFAULT_RESULT_VALUE = 0.0
DEFAULT_RESULT1_VALUE = 0.0
FUNCTION_DATA = None


class prPyMath(om.MPxNode):
    kPluginNodeTypeName = "prPyMath"
    prPyMathId = om.MTypeId(0x0010A51A)  # not save

    @staticmethod
    def initialize():
        numeric_attribute = om.MFnNumericAttribute()
        enum_attribute = om.MFnEnumAttribute()
        compound_attribute = om.MFnCompoundAttribute()

        # OUTPUT
        prPyMath.result = numeric_attribute.create("result", "result", om.MFnNumericData.kFloat, 0.0)
        numeric_attribute.writable = False
        prPyMath.addAttribute(prPyMath.result)

        prPyMath.result1 = numeric_attribute.create("result1", "result1", om.MFnNumericData.kFloat, 0.0)
        numeric_attribute.writable = False
        prPyMath.addAttribute(prPyMath.result1)

        # DATA
        prPyMath.e = numeric_attribute.create('e', 'e', om.MFnNumericData.kFloat, math.e)
        numeric_attribute.keyable = False
        prPyMath.addAttribute(prPyMath.e)

        prPyMath.pi = numeric_attribute.create('pi', 'pi', om.MFnNumericData.kFloat, math.pi)
        numeric_attribute.keyable = False
        prPyMath.addAttribute(prPyMath.pi)

        # FUNCTIONS
        prPyMath.func = enum_attribute.create("function", "function", 0)
        for index, data in get_math_function_data().iteritems():
            enum_attribute.addField(data['name'], index)
        enum_attribute.keyable = True
        prPyMath.addAttribute(prPyMath.func)
        prPyMath.attributeAffects(prPyMath.func, prPyMath.result)
        prPyMath.attributeAffects(prPyMath.func, prPyMath.result1)

        # ARGUMENTS
        prPyMath.x = numeric_attribute.create('x', 'x', om.MFnNumericData.kFloat, 0.0)
        numeric_attribute.keyable = True
        prPyMath.addAttribute(prPyMath.x)
        prPyMath.attributeAffects(prPyMath.x, prPyMath.result)
        prPyMath.attributeAffects(prPyMath.x, prPyMath.result1)

        prPyMath.y = numeric_attribute.create('y', 'y', om.MFnNumericData.kFloat, 0.0)
        numeric_attribute.keyable = True
        prPyMath.addAttribute(prPyMath.y)
        prPyMath.attributeAffects(prPyMath.y, prPyMath.result)

        prPyMath.i = numeric_attribute.create('i', 'i', om.MFnNumericData.kInt, 0.0)
        numeric_attribute.keyable = True
        prPyMath.addAttribute(prPyMath.i)
        prPyMath.attributeAffects(prPyMath.i, prPyMath.result)

        prPyMath.base = numeric_attribute.create('base', 'base', om.MFnNumericData.kFloat, math.e)
        numeric_attribute.keyable = True
        prPyMath.addAttribute(prPyMath.base)
        prPyMath.attributeAffects(prPyMath.base, prPyMath.result)

        prPyMath.iterable = numeric_attribute.create('iterable', 'iterable', om.MFnNumericData.kFloat)
        numeric_attribute.array = True
        numeric_attribute.keyable = True
        prPyMath.addAttribute(prPyMath.iterable)
        prPyMath.attributeAffects(prPyMath.iterable, prPyMath.result)

        prPyMath.arguments = compound_attribute.create('arguments', 'arguments')
        compound_attribute.addChild(prPyMath.x)
        compound_attribute.addChild(prPyMath.y)
        compound_attribute.addChild(prPyMath.i)
        compound_attribute.addChild(prPyMath.base)
        compound_attribute.addChild(prPyMath.iterable)
        prPyMath.addAttribute(prPyMath.arguments)

        # UTILITY
        prPyMath.ignore_errors = numeric_attribute.create('ignore_errors', 'ignore_errors', om.MFnNumericData.kBoolean, False)
        numeric_attribute.keyable = True
        prPyMath.addAttribute(prPyMath.ignore_errors)

    @staticmethod
    def creator():
        return prPyMath()

    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug, data_block):
        if plug == prPyMath.e:
            e_handle = data_block.outputValue(prPyMath.e)
            e_handle.setFloat(math.e)
            data_block.setClean(plug)
            return
        elif plug == prPyMath.pi:
            pi_handle = data_block.outputValue(prPyMath.pi)
            pi_handle.setFloat(math.pi)
            data_block.setClean(plug)
            return
        elif plug != prPyMath.result and plug != prPyMath.result1:
            raise ValueError('Unknown plug request : {0}'.format(plug))

        ignore_errors = data_block.inputValue(prPyMath.ignore_errors).asBool()

        func_index = data_block.inputValue(prPyMath.func).asChar()
        func = get_math_function_data()[func_index]

        args = []
        for kwarg in func['kwargs']:
            if kwarg == 'x':
                args.append(data_block.inputValue(prPyMath.x).asFloat())
            elif kwarg == 'y':
                args.append(data_block.inputValue(prPyMath.y).asFloat())
            elif kwarg == 'i':
                args.append(data_block.inputValue(prPyMath.i).asInt())
            elif kwarg == 'base':
                args.append(data_block.inputValue(prPyMath.base).asFloat())
            elif kwarg == 'iterable':
                arg = []
                array_data_handle = data_block.inputArrayValue(prPyMath.iterable)
                while not array_data_handle.isDone():
                    arg.append(array_data_handle.inputValue().asFloat())
                    array_data_handle.next()
                args.append(arg)
            else:
                raise ValueError('Unknown argument: {0}'.format(kwarg))

        try:
            result = func['function'](*args)
            if isinstance(result, tuple):
                result, result1 = result
            else:
                result1 = DEFAULT_RESULT1_VALUE
        except ValueError as error:
            result = DEFAULT_RESULT_VALUE
            result1 = DEFAULT_RESULT1_VALUE
        else:
            error = None
        if plug == prPyMath.result:
            result_handle = data_block.outputValue(prPyMath.result)
            result_handle.setFloat(result)
        elif plug == prPyMath.result1:
            result1_handle = data_block.outputValue(prPyMath.result1)
            result1_handle.setFloat(result1)
        data_block.setClean(plug)

        if error and not ignore_errors:
            raise ValueError('{0} : {1}({2})'.format(error, func['name'], dict(zip(func['kwargs'], args))))


def initializePlugin(mobject):
    mplugin = om.MFnPlugin(mobject)
    try:
        mplugin.registerNode(prPyMath.kPluginNodeTypeName, prPyMath.prPyMathId, prPyMath.creator, prPyMath.initialize)
    except:
        sys.stderr.write("Failed to register node: %s" % prPyMath.kPluginNodeTypeName)
        raise
    eval_AE_template()


def uninitializePlugin(mobject):
    mplugin = om.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(prPyMath.prPyMathId)
    except:
        sys.stderr.write("Failed to deregister node: %s" % prPyMath.kPluginNodeTypeName)
        raise


def maya_useNewAPI():
    pass


def get_math_function_data():
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


def eval_AE_template():
    import maya.mel as mm
    mm.eval('''
    global proc AEprPyMathTemplate_iterable_create_element()
    {
        string $node = `textField -q -text "AEprPyMathTemplate_iterable_node_textField"`;
        string $attribute = $node+".iterable";
        int $indices[] = `getAttr -multiIndices $attribute`;
        int $index_size = size($indices);
        int $new_index = 0;
        if ($index_size != 0){
            $new_index = $indices[$index_size-1]+1;
        }
        setAttr ($attribute+"["+$new_index+"]") 0;
    };
    
    global proc AEprPyMathTemplate_iterable_delete_element()
    {
        string $node = `textField -q -text "AEprPyMathTemplate_iterable_node_textField"`;
        int $index = `intField -q -value "AEprPyMathTemplate_iterable_delete_item_intField"`;
        string $attribute = $node+".iterable";
        removeMultiInstance ($attribute+"["+$index+"]");

    };
    
    global proc AEprPyMathTemplate_iterable_build(string $plug)
    {
        rowLayout -numberOfColumns 4 -columnWidth4 100 100 100 100;
        textField -editable 0 "AEprPyMathTemplate_iterable_node_textField";
        button -l "Create new item" -c "AEprPyMathTemplate_iterable_create_element";
        button -l "Delete item:" -c "AEprPyMathTemplate_iterable_delete_element";
        intField -minValue 0 -value 0 "AEprPyMathTemplate_iterable_delete_item_intField";
        setParent ..;
        AEprPyMathTemplate_iterable_update($plug);
    };
    
    global proc AEprPyMathTemplate_iterable_update(string $plug)
    {
        string $node_attr[];
        tokenize($plug, ".", $node_attr);
        textField -e -text $node_attr[0] "AEprPyMathTemplate_iterable_node_textField";
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
                    editorTemplate -beginLayout "iterable" -collapse 1;
                        editorTemplate -callCustom "AEprPyMathTemplate_iterable_build" "AEprPyMathTemplate_iterable_update" "iterable";
                        editorTemplate -addControl "iterable";
                    editorTemplate -endLayout;
                editorTemplate -endLayout;
            editorTemplate -endLayout;
        AEdependNodeTemplate $nodeName;
        editorTemplate -suppress "arguments";
        editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')

