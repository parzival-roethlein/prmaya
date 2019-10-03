"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prMotionPath
reload(test_prMotionPath)
test_prMotionPath.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prMotionPath.py'
test_prMotionPath.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prMotionPath.ma'
test_prMotionPath.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prMotionPath
reload(test_prMotionPath)
test_prMotionPath.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prMotionPath.py'
test_prMotionPath.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prMotionPath.ma'
test_prMotionPath.run()

"""

import maya.cmds as mc

from prmaya.plugins import prMotionPath
reload(prMotionPath)

SETTINGS = {'plugin_name': 'prMotionPath.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prMotionPath.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prMotionPath.ma',
            }


def createTempFile():
    """create and reopen TEMP scene"""
    TEMP_FILE = mc.file(q=True, sceneName=True).replace('.ma', 'TEMP.ma')
    mc.file(rename=TEMP_FILE)
    mc.file(save=True, force=True)
    mc.file(new=True, force=True)
    mc.file(TEMP_FILE, open=True, force=True)
    mc.file(renameToSave=True)


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)

    prNode = mc.createNode('prMotionPath', name='prnode_output_prMotionPath')
    mc.connectAttr('curve1.worldSpace', prNode+'.inputCurve', force=True)
    mc.connectAttr('uValue_locator.fractionMode', prNode+'.fractionMode', force=True)

    for x in range(11):
        mc.connectAttr('uValue_locator.uValue'+str(x), '{}.uValue[{}]'.format(prNode, x), force=True)
        mc.connectAttr('{0}.output[{1}].outTranslate'.format(prNode, x), 'prnode_output_{}.t'.format(x), force=True)
    createTempFile()
