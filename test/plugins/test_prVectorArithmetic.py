"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prVectorArithmetic
reload(test_prVectorArithmetic)
test_prVectorArithmetic.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorArithmetic.py'
test_prVectorArithmetic.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorArithmetic.ma'
test_prVectorArithmetic.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prVectorArithmetic
reload(test_prVectorArithmetic)
test_prVectorArithmetic.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prVectorArithmetic.py'
test_prVectorArithmetic.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prVectorArithmetic.ma'
test_prVectorArithmetic.run()

"""

import maya.cmds as mc

from prmaya.plugins import prVectorArithmetic
reload(prVectorArithmetic)

SETTINGS = {'plugin_name': 'prVectorArithmetic.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prVectorArithmetic.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prVectorArithmetic.ma',
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
    for value, operation in enumerate(['noOperation',
                                       'sum', 'subtract', 'average',
                                       'crossProduct', 'projection']):
        prNode = mc.createNode('prVectorArithmetic', name=operation + '_prVectorArithmetic')
        #mc.setAttr(prNode+'.operation', value)
        mc.connectAttr(input1, prNode+'.input[0].input1')
        mc.connectAttr(input2, prNode+'.input[0].input2')
        mc.connectAttr(prNode+'.output[0]', output)

        return  # TODO: proper test

        mc.setAttr(prNode + '.operation', value)
        mc.setAttr(prNode + '.input[1].input1', driverValue)
        mc.setAttr(prNode + '.input[1].input2', driverValue)
        mc.setAttr(prNode + '.input[2].input2', driverValue)

        prCube = operation+'_pr'
        if mc.objExists(prCube):
            mc.connectAttr(loc + '.ty', prNode + '.input[2].input1')
            mc.connectAttr(prNode + '.output[2]', prCube + '.ty')
        else:
            print('missing: {}'.format(prCube))

        prCubeStatic = prCube+'_static'
        if mc.objExists(prCubeStatic):
            mc.connectAttr(prNode + '.output[1]', prCubeStatic + '.ty')
        else:
            print('missing: {}'.format(prCubeStatic))
    createTempFile()
    mc.select(loc)
