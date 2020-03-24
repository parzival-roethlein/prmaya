import sys
import maya.cmds as mc

from prmaya.plugins import prUpCurveSpline
reload(prUpCurveSpline)

DATA = {'path': r'C:\Users\paz\Documents\git\prmaya\test\plugins',
        'plugin': r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prUpCurveSpline.py',
        'file': r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prUpCurveSpline.ma'}
# DATA = {'path': '/home/prthlein/private/code/prmaya/test/plugins',
#         'plugin': '/home/prthlein/private/code/prmaya/prmaya/plugins/prUpCurveSpline.py',
#         'file': '/home/prthlein/private/code/prmaya/test/plugins/test_prUpCurveSpline.ma'}


sys.path.append(DATA['path'])

mc.file(newFile=True, force=True)
mc.unloadPlugin('prUpCurveSpline.py')
mc.loadPlugin(DATA['plugin'])
mc.file(DATA['file'], open=True, force=True)

# setup
locators = ['locator1', 'locator2', 'locator3', 'locator4', 'locator5']
node = mc.createNode('prUpCurveSpline', name='test_prUpCurveSpline')
mc.connectAttr('curve1.worldSpace', node+'.curve', force=True)
mc.connectAttr('curve2.worldSpace', node+'.upCurve', force=True)
for x in range(5):
    mc.setAttr('{}.parameter[{}]'.format(node, x), x/4.0)
    decomp = mc.createNode('decomposeMatrix')
    mc.connectAttr('{}.outputMatrix[{}]'.format(node, x),
                   '{}.inputMatrix'.format(decomp))
    mc.connectAttr('{}.outputTranslate'.format(decomp),
                   '{}.translate'.format(locators[x]))
    mc.connectAttr('{}.outputRotate'.format(decomp),
                   '{}.rotate'.format(locators[x]))


def createTempFile():
    """create and reopen TEMP scene"""
    TEMP_FILE = mc.file(q=True, sceneName=True).replace('.ma', 'TEMP.ma')
    mc.file(rename=TEMP_FILE)
    mc.file(save=True, force=True)
    mc.file(new=True, force=True)
    mc.file(TEMP_FILE, open=True, force=True)
    mc.file(renameToSave=True)


createTempFile()
