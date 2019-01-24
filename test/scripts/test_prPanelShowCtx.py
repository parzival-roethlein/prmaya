"""

import maya.cmds as cmds
cmds.file("/home/prthlein/private/code/prmaya/test/scripts/prPanelShowCtx.ma", open=True, force=True)
import sys
sys.path.append('/home/prthlein/private/code/prmaya/')
from prmaya.scripts import prPanelShowCtx
prPanelShowCtx.disable()
reload(prPanelShowCtx)
prPanelShowCtx.logger.setLevel(10)

prPanelShowCtx.enable()
prPanelShowCtx.getManipCtx()
prPanelShowCtx.disable()

prPanelShowCtx.enable(nurbsCurves=False, manipulators=False)
prPanelShowCtx.disable()

prPanelShowCtx.enable(polymeshes=False)
prPanelShowCtx.disable()

prPanelShowCtx.enable(withFocus=True)
prPanelShowCtx.disable()

"""