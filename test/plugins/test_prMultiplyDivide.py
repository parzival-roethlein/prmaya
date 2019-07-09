"""

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prMultiplyDivide
reload(test_prMultiplyDivide)
test_prMultiplyDivide.run()

import sys
sys.path.append('C:/Users/paz/Documents/git/prmaya/test/plugins')
import test_prMultiplyDivide
reload(test_prMultiplyDivide)
test_prMultiplyDivide.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prMultiplyDivide.py'
test_prMultiplyDivide.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prMultiplyDivide.ma'
test_prMultiplyDivide.run()


"""

import maya.cmds as mc

from prmaya.plugins import prBinaryOperationVec
reload(prBinaryOperationVec)

SETTINGS = {'plugin_name': 'prBinaryOperationVec.py',
            'plugin_path': '/home/prthlein/private/code/prmaya/prmaya/plugins/prBinaryOperationVec.py',
            'file': '/home/prthlein/private/code/prmaya/test/plugins/test_prMultiplyDivide.ma',
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)
    mc.file(rename='asdf')
    mc.file(renameToSave=True)
    operations = {0: 'noOperation',
                  1: 'multiply',
                  2: 'divide',
                  3: 'power'}
    for x, operation in operations.items():
        loc, cube0, cube1 = 'locator', 'pr_{}_0'.format(operation), 'pr_{}_1'.format(operation)
        prMd = mc.createNode('prMultiplyDivide')
        prMd = mc.rename(prMd, '{}_{}'.format(prMd, operation))
        mc.setAttr(prMd + '.input[0].input2', 1.5, 1.5, 1.5)
        mc.setAttr(prMd + '.input[1].input2', 2, 2, 2)
        mc.setAttr(prMd + '.operation', x)
        mc.connectAttr(loc+'.t', prMd+'.input[0].input1')
        mc.connectAttr(loc+'.t', prMd+'.input[1].input1')
        mc.connectAttr(prMd+'.output[0]', cube0+'.t')
        mc.connectAttr(prMd+'.output[1]', cube1+'.t')
        #print(mc.getAttr(prMd+'.output'))

