"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')

import test_prPyMath
reload(test_prPyMath)
test_prPyMath.run()

"""

import math

import maya.cmds as mc
import pymel.core as pm
from prmaya.plugins import prPyMath
reload(prPyMath)


def run(plugin_path='C:/Users/paz/Documents/git/prmaya/prmaya/plugins/prPyMath.py'):
    mc.file(newFile=True, force=True)
    mc.unloadPlugin('prPyMath.py')
    mc.loadPlugin(plugin_path)
    manual_node_test()
    full_node_test()


def is_equal(a, b):
    return round(a, 5) == round(b, 5)


def full_node_test():
    FUNCTION_DATA = prPyMath.getMathFunctionData()
    node = pm.createNode('prPyMath')

    errors = 0
    # DATA
    for attr in ['e', 'pi']:
        module_value = getattr(math, attr)
        node_value = node.attr(attr).get()
        if not is_equal(module_value, node_value):
            print('attribute "{0}" value error module != node : {1} != {2}'.format(attr, module_value, node_value))
            errors += 1

    # FUNCTIONS
    for index, data in FUNCTION_DATA.iteritems():
        args = []
        if data['function'].__name__ in ['frexp', 'modf']:
            continue
        for kwarg in data['kwargs']:
            if kwarg == 'x':
                x_value = 0.987
                if data['function'].__name__ in ['acosh']:
                    x_value = 1.234
                elif data['function'].__name__ in ['factorial']:
                    x_value = 4
                node.x.set(x_value)
                args.append(x_value)
            elif kwarg == 'y':
                node.y.set(0.654)
                args.append(0.654)
            elif kwarg == 'i':
                node.i.set(3)
                args.append(3)
            elif kwarg == 'base':
                node.base.set(0.321)
                args.append(0.321)
            elif kwarg == 'iterable':
                node.iterable[0].set(0.1)
                node.iterable[1].set(0.2)
                node.iterable[2].set(0.3)
                args.append([0.1, 0.2, 0.3])
        node.function.set(index)
        if data['function'].__name__ == 'frexp':
            node_result = node.result_frexp.get()
        else:
            node_result = node.result.get()
        module_result = data['function'](*args)
        if not is_equal(module_result, node_result):
            errors += 1
            print('{0} module != node: {1} != {2}'.format(data['function'], module_result, node_result))
    print('=== {0} errors in {1} tests : full_node_test() ==='.format(errors, len(FUNCTION_DATA)))


def manual_node_test():
    node = pm.createNode('prPyMath')
    enums = node.function.getEnums()

    tests = [['sin', {'x': 0.0}, 0.0],
             ['sin', {'x': 1.57075}, 1.0],
             ['sin', {'x': -1.57075}, -1.0],
             ['cos', {'x': 0}, 1.0],
             ['cos', {'x': 180}, -0.59846],
             ['cos', {'x': 180, 'xDegreesToRadians': True}, -1.0],
             ['cos', {'x': 3.1415, 'xDegreesToRadians': False}, -1.0],
             ['pow', {'x': 3, 'y': 0}, 1],
             ['pow', {'x': 4, 'y': 1}, 4],
             ['pow', {'x': 2, 'y': 5}, 32],
             ['atan2', {'y': 2, 'x': 0}, 1.570796],
             ['atan2', {'y': 0, 'x': 2}, 0.0],
             ['ldexp', {'x': 2, 'i': 5}, 64],
             ['ldexp', {'x': 5, 'i': 2}, 20],
             ['fsum', {'iterable[0]': 1.1, 'iterable[2]': 2.2, 'iterable[3]': 3.3}, 6.6],
             # ERROR TEST
             ['acos', {'x': 2, 'resultDefault': 3.33}, 3.33],
             # FINISH
             ['sin', {'x': 1.57075}, 1.0],
             ]
    errors = 0

    for name, args, should_result in tests:
        for a, v in args.items():
            node.attr(a).set(v)
        node.function.set(enums[name])
        result = node.result.get()
        func_string = '{0}({1}) : {2}'.format(name, args, result)
        if is_equal(result, should_result):
            print('OK {}'.format(func_string))
        else:
            print('ERROR {0} != {1}'.format(func_string, should_result))
            errors += 1
    print('=== {0} errors in {1} tests : node_test_manual() ==='.format(errors, len(tests)))
    pm.select(node)

