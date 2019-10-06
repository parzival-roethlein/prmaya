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
    mc.connectAttr('inputMatrix.cubeRotateOrder', prNode+'.input[1].inputRotateOrder', force=True)
    mc.connectAttr('inputMatrix.worldMatrix', prNode+'.input[1].inputMatrix', force=True)
    mc.connectAttr('prnode_output.parentInverseMatrix', prNode+'.input[1].inputInverseMatrix', force=True)
    mc.connectAttr(prNode+'.output[1].outTranslate', 'prnode_output.translate', force=True)
    mc.connectAttr(prNode+'.output[1].outRotate', 'prnode_output.rotate', force=True)
    mc.connectAttr(prNode+'.output[1].outScale', 'prnode_output.scale', force=True)
    mc.connectAttr(prNode+'.output[1].outShear', 'prnode_output.shear', force=True)
    mc.connectAttr(prNode+'.output[1].outQuatX', 'prnode_outQuat.tx', force=True)
    mc.connectAttr(prNode+'.output[1].outQuatY', 'prnode_outQuat.ty', force=True)
    mc.connectAttr(prNode+'.output[1].outQuatZ', 'prnode_outQuat.tz', force=True)
    mc.connectAttr(prNode+'.output[1].outQuatW', 'prnode_outQuat.sy', force=True)

    createTempFile()

    mc.select('inputMatrix')
