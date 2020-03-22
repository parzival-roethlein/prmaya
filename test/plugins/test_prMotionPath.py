import sys
import maya.cmds as mc

from prmaya.plugins import prMotionPath
reload(prMotionPath)

DATA = {'path': r'C:\Users\paz\Documents\git\prmaya\test\plugins',
        'plugin': r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prMotionPath.py',
        'file': r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prMotionPath.ma'}
# DATA = {'path': '/home/prthlein/private/code/prmaya/test/plugins',
#         'plugin': '/home/prthlein/private/code/prmaya/prmaya/plugins/prMotionPath.py',
#         'file': '/home/prthlein/private/code/prmaya/test/plugins/test_prMotionPath.ma'}


sys.path.append(DATA['path'])

mc.file(newFile=True, force=True)
mc.unloadPlugin('prMotionPath.py')
mc.loadPlugin(DATA['plugin'])
mc.file(DATA['file'], open=True, force=True)

# setup
prNode = mc.createNode('prMotionPath', name='prnode_output_prMotionPath')
mc.connectAttr('curve1.worldSpace', prNode+'.inputCurve', force=True)
mc.connectAttr('uValue_locator.fractionMode', prNode+'.fractionMode', force=True)

for x in range(11):
    mc.connectAttr('uValue_locator.uValue'+str(x), '{}.uValue[{}]'.format(prNode, x), force=True)
    mc.connectAttr('{0}.output[{1}].outTranslate'.format(prNode, x), 'prnode_output_{}.t'.format(x), force=True)


def createTempFile():
    """create and reopen TEMP scene"""
    TEMP_FILE = mc.file(q=True, sceneName=True).replace('.ma', 'TEMP.ma')
    mc.file(rename=TEMP_FILE)
    mc.file(save=True, force=True)
    mc.file(new=True, force=True)
    mc.file(TEMP_FILE, open=True, force=True)
    mc.file(renameToSave=True)


createTempFile()
