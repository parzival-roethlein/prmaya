import maya.cmds as mc
import prDeformPaint;reload(prDeformPaint)
prDeformPaint.Ui()
mc.file('/home/prthlein/private/code/prmaya/test/scripts/test_prDeformPaint.ma', open=True, force=True)
mc.file(renameToSave=True)
prDeformPaint.reinitializeMaya()

#prDeformPaint.initializeMaya('/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py',
#                             '/home/prthlein/private/code/prmaya/prmaya/scripts/prDeformPaintBrush.mel')
prDeformPaint.reinitializeMaya()


# pr  flood = 17sec (undo 14)
# dpk flood = 12sec (undo 19)