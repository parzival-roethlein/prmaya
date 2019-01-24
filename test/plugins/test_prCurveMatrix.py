"""

import sys
sys.path.append('C:/Users/paz/Documents/git/prmaya/test/plugins')
import test_prCurveMatrix
reload(test_prCurveMatrix)
test_prCurveMatrix.run()


import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prCurveMatrix
reload(test_prCurveMatrix)
test_prCurveMatrix.SETTINGS['plugin_path'] = '/home/prthlein/private/code/prmaya/prmaya/plugins/prCurveMatrix.py',
test_prCurveMatrix.SETTINGS['file'] = '/home/prthlein/private/code/prmaya/test/plugins/test_prCurveMatrix_scene.ma',
test_prCurveMatrix.run()

"""


import maya.cmds as mc
from prmaya.plugins import prCurveMatrix
reload(prCurveMatrix)


SETTINGS = {'plugin_name': 'prCurveMatrix.py',
            'plugin_path': 'C:/Users/paz/Documents/git/prmaya/prmaya/plugins/prCurveMatrix.py',
            'file': 'C:/Users/paz/Documents/git/prmaya/test/plugins/test_prCurveMatrix.ma',
            'outputPositionCurve': 'outputPositionCurve',
            'outputPositionCurve1': 'outputPositionCurve1',
            'outputMatrixCurve': 'outputMatrixCurve',
            'matrixUpTransform': 'up_locator'
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)

    positionFrame = prCurveMatrix.fromCurves([SETTINGS['outputPositionCurve'],
                                              SETTINGS['outputPositionCurve1']])
    prCurveMatrix.transformFromOutputTranslate(positionFrame)
    
    mc.select(SETTINGS['outputMatrixCurve'])
    matrixFrame = prCurveMatrix.fromCurves()
    mc.select(matrixFrame)
    prCurveMatrix.transformFromOutputMatrix()
    mc.connectAttr('{0}.worldMatrix'.format(SETTINGS['matrixUpTransform']),
                   '{0}.input[0].worldUpMatrix'.format(matrixFrame))
    mc.select([positionFrame, matrixFrame])

