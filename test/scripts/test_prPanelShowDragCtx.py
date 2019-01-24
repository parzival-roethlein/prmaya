"""

import maya.cmds as cmds
cmds.file("/home/prthlein/private/code/prmaya/test/scripts/prPanelShowDragCtx.ma", open=True, force=True)
import sys
sys.path.append('/home/prthlein/private/code/prmaya/')
from prmaya.scripts import prPanelShowDragCtx
prPanelShowDragCtx.disable()
reload(prPanelShowDragCtx)
prPanelShowDragCtx.logger.setLevel(10)

prPanelShowDragCtx.enable()
prPanelShowDragCtx.getManipCtx()
prPanelShowDragCtx.disable()

prPanelShowDragCtx.enable(nurbsCurves=False, manipulators=False)
prPanelShowDragCtx.disable()

prPanelShowDragCtx.enable(polymeshes=False)
prPanelShowDragCtx.disable()

prPanelShowDragCtx.enable(withFocus=True)
prPanelShowDragCtx.disable()

"""