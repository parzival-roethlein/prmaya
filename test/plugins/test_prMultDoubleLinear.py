"""

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prMultDoubleLinear
reload(test_prMultDoubleLinear)
test_prMultDoubleLinear.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prMultDoubleLinear.py'
test_prMultDoubleLinear.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prMultDoubleLinear.ma'
test_prMultDoubleLinear.run()

"""

import maya.cmds as mc

from prmaya.plugins import prMultDoubleLinear
reload(prMultDoubleLinear)

SETTINGS = {'plugin_name': 'prMultDoubleLinear.py',
            'plugin_path': '/home/prthlein/private/code/prmaya/prmaya/plugins/prMultDoubleLinear.py',
            'file': '/home/prthlein/private/code/prmaya/test/plugins/test_prMultDoubleLinear.ma',
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)
    mc.file(rename='asdf')
    mc.file(renameToSave=True)

    prMdl = mc.createNode('prMultDoubleLinear')
    mc.setAttr(prMdl + '.input[0].input1', 1.5)
    mc.setAttr(prMdl + '.input[1].input2', 3.33)

    loc = 'locator'
    mc.connectAttr(loc + '.ty', prMdl + '.input[0].input2')
    mc.connectAttr(loc + '.ty', prMdl + '.input[1].input1')

    mc.connectAttr(prMdl + '.output[0]', 'cube_prMultDoubleLinear_0.ty')
    mc.connectAttr(prMdl + '.output[1]', 'cube_prMultDoubleLinear_1.ty')
