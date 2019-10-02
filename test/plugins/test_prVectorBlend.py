"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prVectorBlend
reload(test_prVectorBlend)
test_prVectorBlend.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorBlend.py'
test_prVectorBlend.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorBlend.ma'
test_prVectorBlend.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prVectorBlend
reload(test_prVectorBlend)
test_prVectorBlend.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prVectorBlend.py'
test_prVectorBlend.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prVectorBlend.ma'
test_prVectorBlend.run()

"""

import maya.cmds as mc

from prmaya.plugins import prVectorBlend
reload(prVectorBlend)

SETTINGS = {'plugin_name': 'prVectorBlend.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorBlend.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorBlend.ma',
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

    input1, input2, output = 'input1.t', 'input2.t', 'output.t'
    prNode = mc.createNode('prVectorBlend')

    mc.connectAttr('output.blender', prNode + '.blender')
    mc.connectAttr(input1, prNode + '.input[1].input1')
    mc.connectAttr(input2, prNode + '.input[1].input2')
    mc.connectAttr(prNode + '.output[1]', output)
    mc.setAttr(prNode + '.input[0].input1', 0.1, 0.2, 0.3)

    # TODO: proper test

    createTempFile()
