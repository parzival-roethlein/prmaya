"""

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prRange
reload(test_prRange)
test_prRange.run()

import sys
sys.path.append('C:/Users/paz/Documents/git/prmaya/test/plugins')
import test_prRange
reload(test_prRange)
test_prRange.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prRange.py'
test_prRange.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prRange.ma'
test_prRange.run()

"""

import maya.cmds as mc

from prmaya.plugins import prRange

reload(prRange)

SETTINGS = {'plugin_name': 'prRange.py',
            'plugin_path': '/home/prthlein/private/code/prmaya/prmaya/plugins/prRange.py',
            'file': '/home/prthlein/private/code/prmaya/test/plugins/test_prRange.ma',
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)
    mc.file(rename='asdf')
    mc.file(renameToSave=True)

    mc.createNode('prRange')
    mc.connectAttr('inputMin.tx', 'prRange1.inputMin')
    mc.connectAttr('inputMax.tx', 'prRange1.inputMax')
    mc.setAttr("prRange1.inputStepCount", 5)

    for x in range(5):
        transform = 'cube{}'.format(x)
        mc.connectAttr('prRange1.output[{}]'.format(x), '{}.tx'.format(transform))

    print(mc.getAttr('prRange1.output'))
