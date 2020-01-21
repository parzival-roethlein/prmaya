
import maya.cmds as mc
import maya.api.OpenMaya as om
from prmaya.plugins import prAverageDeltasCmd
reload(prAverageDeltasCmd)

mc.file(newFile=True, force=True)
mc.unloadPlugin('prAverageDeltasCmd.py')
# mc.loadPlugin('C:/Users/paz/Documents/git/prmaya/prmaya/plugins/prAverageDeltasCmd.py')
# mc.file('C:/Users/paz/Documents/git/prmaya/test/plugins/test_prAverageDeltasCmd.ma', open=True, force=True)
mc.loadPlugin('/home/prthlein/private/code/prmaya/prmaya/plugins/prAverageDeltasCmd.py')
mc.file('/home/prthlein/private/code/prmaya/test/plugins/test_prAverageDeltasCmd.ma', open=True, force=True)

mc.prAverageDeltasCmd('base', 'driven', om.MSpace.kObject, [213, 216], [1.0, 1.0], 0.5)

