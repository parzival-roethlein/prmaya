"""

import sys
sys.path.append('C:/Users/paz/Documents/git/prmaya/test/plugins')
import test_prMovePointsCmd
reload(test_prMovePointsCmd)
test_prMovePointsCmd.run()
mc.prMovePointsCmd('pSphereShape1', om.MSpace.kObject, [294, 297, 280],
                   om.MVector(0, 0.25, 0), om.MVector(0, 0.5, 0), om.MVector(0, 1, 0))

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prMovePointsCmd
reload(test_prMovePointsCmd)
test_prMovePointsCmd.SETTINGS['plugin_path'] = r'/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py'
test_prMovePointsCmd.SETTINGS['file'] = r'/home/prthlein/private/code/prmaya/test/plugins/test_prMovePointsCmd.ma'
test_prMovePointsCmd.run()
mc.prMovePointsCmd('pSphereShape1', om.MSpace.kObject, [294, 297, 280],
                   om.MVector(0, 0.25, 0), om.MVector(0, 0.5, 0), om.MVector(0, 1, 0))
"""


import maya.cmds as mc
import maya.api.OpenMaya as om
from prmaya.plugins import prMovePointsCmd
reload(prMovePointsCmd)


SETTINGS = {'plugin_name': 'prMovePointsCmd.py',
            'plugin_path': 'C:/Users/paz/Documents/git/prmaya/prmaya/plugins/prMovePointsCmd.py',
            'file': 'C:/Users/paz/Documents/git/prmaya/test/plugins/test_prMovePointsCmd.ma',
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)
    mc.prMovePointsCmd('pSphereShape1', om.MSpace.kObject, [296, 298], om.MVector(0, 1, 0), om.MVector(0, 0.5, 0))
