"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prDecomposeMatrix
reload(test_prDecomposeMatrix)
test_prDecomposeMatrix.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prDecomposeMatrix.py'
test_prDecomposeMatrix.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prDecomposeMatrix.ma'
test_prDecomposeMatrix.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prDecomposeMatrix
reload(test_prDecomposeMatrix)
test_prDecomposeMatrix.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prDecomposeMatrix.py'
test_prDecomposeMatrix.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prDecomposeMatrix.ma'
test_prDecomposeMatrix.run()

"""

import maya.cmds as mc

from prmaya.plugins import prDecomposeMatrix
reload(prDecomposeMatrix)

SETTINGS = {'plugin_name': 'prDecomposeMatrix.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prDecomposeMatrix.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prDecomposeMatrix.ma',
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

    prNode = mc.createNode('prDecomposeMatrix', name='prnode_output_prDecomposeMatrix')
    mc.connectAttr('inputMatrix.matrix', prNode+'.input[0].inputMatrix', force=True)
    mc.connectAttr(prNode+'.output[0].outTranslate', 'prnode_output.translate', force=True)

    createTempFile()
