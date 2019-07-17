"""

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\plugins')
import test_prScalarArithmetic
reload(test_prScalarArithmetic)
test_prScalarArithmetic.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prScalarArithmetic.py'
test_prScalarArithmetic.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prScalarArithmetic.ma'
test_prScalarArithmetic.run()

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prScalarArithmetic
reload(test_prScalarArithmetic)
test_prScalarArithmetic.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prScalarArithmetic.py'
test_prScalarArithmetic.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prScalarArithmetic.ma'
test_prScalarArithmetic.run()

"""

import maya.cmds as mc

from prmaya.plugins import prScalarArithmetic
reload(prScalarArithmetic)

SETTINGS = {'plugin_name': 'prScalarArithmetic.py',
            'plugin_path': 'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prScalarArithmetic.py',
            'file': 'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prScalarArithmetic.ma',
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
    createTempFile()
    loc = 'locator'
    driverValue = mc.getAttr(loc+'.ty')
    for value, operation in enumerate(['noOperation',
                                       'sum', 'subtract', 'average',
                                       'multiply', 'divide', 'power',
                                       'root', 'floorDivision', 'modulo']):
        prNode = mc.createNode('prScalarArithmetic',
                                           name=operation + '_prScalarArithmetic')
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
    mc.select(loc)