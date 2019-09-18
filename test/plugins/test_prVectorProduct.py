"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prVectorProduct
reload(test_prVectorProduct)
test_prVectorProduct.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorProduct.py'
test_prVectorProduct.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorProduct.ma'
test_prVectorProduct.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prVectorProduct
reload(test_prVectorProduct)
test_prVectorProduct.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prVectorProduct.py'
test_prVectorProduct.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prVectorProduct.ma'
test_prVectorProduct.run()

"""

import maya.cmds as mc

from prmaya.plugins import prVectorProduct
reload(prVectorProduct)

SETTINGS = {'plugin_name': 'prVectorProduct.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorProduct.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorProduct.ma',
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
    globalMatrix, globalScalar = 'input2.worldMatrix', 'input2.scalar'
    for value, operation in enumerate(['noOperation',
                                       'dotProduct', 'crossProduct',
                                       'vectorMatrixProduct', 'pointMatrixProduct']):
        prNode = mc.createNode('prVectorProduct', name=operation + '_prVectorProduct')
        mayaNode = prNode.replace('prVectorProduct', 'vectorProduct')
        if mc.objExists(mayaNode):
            mc.connectAttr(prNode+'.operation', mayaNode+'.operation', force=True)
            mc.connectAttr(prNode+'.normalizeOutput', mayaNode+'.normalizeOutput', force=True)
        mc.setAttr(prNode+'.operation', value)
        mc.connectAttr(input1, prNode+'.input[0].input1')
        mc.connectAttr(input2, prNode+'.input[0].input2')
        mc.connectAttr(globalScalar, prNode+'.globalScalar')
        mc.connectAttr(globalMatrix, prNode+'.globalMatrix')
        mc.connectAttr(prNode+'.output[0]', output, force=True)
        # TODO: other operations
        break

    createTempFile()
    mc.select(prNode)

