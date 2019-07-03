"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prBinaryOperation
reload(test_prBinaryOperation)
test_prBinaryOperation.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prBinaryOperation.py'
test_prBinaryOperation.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prBinaryOperation.ma'
test_prBinaryOperation.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prBinaryOperation
reload(test_prBinaryOperation)
test_prBinaryOperation.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prBinaryOperation.py'
test_prBinaryOperation.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prBinaryOperation.ma'
test_prBinaryOperation.run()

"""

import maya.cmds as mc

from prmaya.plugins import prBinaryOperation
reload(prBinaryOperation)

SETTINGS = {'plugin_name': 'prBinaryOperation.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prBinaryOperation.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prBinaryOperation.ma',
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)
    mc.file(rename='asdf')
    mc.file(renameToSave=True)

    loc = 'locator'
    for value, operation in enumerate(['noOperation',
                                  'sum', 'subtract', 'average',
                                  'multiply', 'divide', 'power']):
        cube0, cube1 = operation+'_pr_0', operation+'_pr_1',
        prBinary = mc.createNode('prBinaryOperation')
        prBinary = mc.rename(prBinary, operation+'_'+prBinary)
        mc.setAttr(prBinary + '.operation', value)

        mc.setAttr(prBinary + '.input[0].input2', 0.5)
        mc.setAttr(prBinary + '.input[1].input2', 1.1)

        mc.connectAttr(loc + '.ty', prBinary + '.input[0].input1')
        mc.connectAttr(loc + '.ty', prBinary + '.input[1].input1')

        mc.connectAttr(prBinary + '.output[0]', cube0+'.ty')
        mc.connectAttr(prBinary + '.output[1]', cube1+'.ty')
