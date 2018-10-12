"""

import sys
sys.path.append('C:/Users/paz/Documents/git/prmaya/test/plugins')
import test_prCurveFrame
reload(test_prCurveFrame)
test_prCurveFrame.run()

"""


import maya.cmds as mc
from prmaya.plugins import prCurveFrame
reload(prCurveFrame)


SETTINGS = {'plugin_name': 'prCurveFrame.py',
            'plugin_path': 'C:/Users/paz/Documents/git/prmaya/prmaya/plugins/prCurveFrame.py',
            'file': 'C:/Users/paz/Documents/git/prmaya/test/plugins/test_prCurveFrame_scene.mb',
            'curve1': 'curve1',
            'curve2': 'curve2',
            'upMatrixTransform': 'up_locator'
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True)
    mc.select(SETTINGS['curve1'])
    curveFrame1 = prCurveFrame.createFromCurve()
    mc.connectAttr('{0}.worldMatrix'.format(SETTINGS['upMatrixTransform']), '{0}.worldUpMatrix'.format(curveFrame1))
    prCurveFrame.createDecomposeMatrixFromOutputMatrix(curveFrame=curveFrame1)

    curveFrame2 = prCurveFrame.createFromCurve(curve=SETTINGS['curve2'])
    mc.setAttr('{0}.points'.format(curveFrame2), 30)
    mc.connectAttr('{0}.worldMatrix'.format(SETTINGS['upMatrixTransform']), '{0}.worldUpMatrix'.format(curveFrame2))
    prCurveFrame.createDecomposeMatrixFromOutputMatrix(curveFrame=curveFrame2)

    mc.select(curveFrame1, curveFrame2)

