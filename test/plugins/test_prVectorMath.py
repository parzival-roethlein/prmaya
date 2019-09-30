"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prVectorMath
reload(test_prVectorMath)
test_prVectorMath.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorMath.py'
test_prVectorMath.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorMath.ma'
test_prVectorMath.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prVectorMath
reload(test_prVectorMath)
test_prVectorMath.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prVectorMath.py'
test_prVectorMath.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prVectorMath.ma'
test_prVectorMath.run()

"""

import maya.cmds as mc

from prmaya.plugins import prVectorMath
reload(prVectorMath)

SETTINGS = {'plugin_name': 'prVectorMath.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorMath.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorMath.ma',
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

    input1, input2 = 'input1.translate', 'input2.translate'
    scalar, matrix = 'input2.scalar', 'input2.worldMatrix'
    globalScalar, globalMatrix = 'global_transform.scalar', 'global_transform.worldMatrix'

    for value, operation in enumerate(['noOperation',
                                       'sum', 'subtract', 'average',
                                       'dotProduct', 'crossProduct',
                                       'vectorMatrixProduct', 'pointMatrixProduct',
                                       'project_in1_on_in2', 'project_in2_on_in1']):
        prNode = mc.createNode('prVectorMath', name=operation + '_prVectorMath')
        mayaNode = prNode.replace('prVectorMath', 'vectorProduct')
        if mc.objExists(mayaNode):
            # mc.connectAttr(prNode+'.nodeState', mayaNode+'.nodeState', force=True)
            # mc.connectAttr(prNode+'.frozen', mayaNode+'.frozen', force=True)
            mc.connectAttr(prNode+'.normalizeOutput', mayaNode+'.normalizeOutput', force=True)
        mc.setAttr(prNode+'.operation', value)
        mc.connectAttr(globalScalar, prNode+'.globalScalar')
        mc.connectAttr(globalMatrix, prNode+'.globalMatrix')
        for x in [0, 2]:
            mc.connectAttr(input1, '{0}.input[{1}].input1'.format(prNode, x))
            mc.connectAttr(input2, '{0}.input[{1}].input2'.format(prNode, x))
            mc.connectAttr(scalar, '{0}.input[{1}].scalar'.format(prNode, x))
            mc.connectAttr(matrix, '{0}.input[{1}].matrix'.format(prNode, x))

            outputAttr = '{0}.output[{1}]'.format(prNode, x)
            outputTarget = '{}_output_{}.translate'.format(prNode, x)
            mc.connectAttr(outputAttr, outputTarget, force=True)

    createTempFile()
    mc.select('input1')

