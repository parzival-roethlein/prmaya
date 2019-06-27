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

import maya.cmds as mc
mc.file(new=True, force=True)
mc.file(rename='/home/prthlein/private/Documents/asdf.ma')
mc.createNode('prRange')
mc.createNode('prRange')
#mc.getAttr('prRange1.outValue')
mc.connectAttr('prRange1.outValue', 'prRange2.inputValue')
mc.file(save=True, typ='mayaAscii')
mc.file(new=True, force=True)
mc.file('/home/prthlein/private/Documents/asdf.ma', open=True, force=True)

"""

import maya.cmds as mc
import pymel.core as pm

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
    mc.setAttr("prRange1.inputSampleCount", 5)

    for x in range(5):
        transform = 'cube{}'.format(x)
        mc.connectAttr('prRange1.output[{}]'.format(x), '{}.tx'.format(transform))

    #for panel in mc.getPanel(type='modelPanel'):
    #    mc.modelEditor(panel, e=True, displayTextures=True)

    print(mc.getAttr('prRange1.output'))

