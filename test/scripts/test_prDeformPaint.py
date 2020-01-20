import maya.cmds as mc
import prDeformPaint;reload(prDeformPaint)
prDeformPaint.Ui()

testFile = '/home/prthlein/private/code/prmaya/test/scripts/test_prDeformPaint.ma'

mc.file(testFile, open=True, force=True)
mc.file(rename=testFile.replace('.ma', 'TEMP.ma'))
mc.file(renameToSave=True)
prDeformPaint.reinitializeMaya()

#prDeformPaint.initializeMaya('/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py',
#                             '/home/prthlein/private/code/prmaya/prmaya/scripts/prDeformPaintBrush.mel')
#prDeformPaint.reinitializeMaya()


# dpk = 12 (19 undo)
# pr  = 17 (14 undo) deformation cmd for each vertex
# pr  = 13 (15 undo) one deformation call for all vertices collected by setValueCmd
# pr  = 14 (13 undo) without vertexId multi call check
# pr  flood = 17sec (undo 14)