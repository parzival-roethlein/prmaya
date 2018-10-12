"""

import sys
sys.path.append('C:/Users/paz/Documents/git/prmaya/test/plugins')
import test_prClosestPoint
reload(test_prClosestPoint)
test_prClosestPoint.run()

"""


import maya.cmds as mc
from prmaya.plugins import prClosestPoint
reload(prClosestPoint)


SETTINGS = {'plugin_name': 'prClosestPoint.py',
            'plugin_path': 'C:/Users/paz/Documents/git/prmaya/prmaya/plugins/prClosestPoint.py',
            'file': 'C:/Users/paz/Documents/git/prmaya/test/plugins/test_prClosestPoint_scene.ma',
            'selection': ['driverMesh', 'driverMesh1',
                          'driverCurve', 'driverCurve1',
                          'driverSurface', 'driverSurface1',
                          'driverLocator', 'driverLocator1',
                          'driverTransform', 'driverTransform1',
                          'driven']
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True)
    mc.select(SETTINGS['selection'])
    prClosestPoint.fromSelection()
    mc.select(SETTINGS['selection'][-1])
