import maya.cmds as mc
testFile = '/home/prthlein/private/code/prmaya/test/scripts/test_prDeformPaint.ma'
#testFile = r'C:\Users\paz\Documents\git\prmaya\test\scripts\test_prDeformPaint.ma'
mc.file(testFile, open=True, force=True)
mc.file(rename=testFile.replace('.ma', 'TEMP.ma'))
mc.file(renameToSave=True)


import prDeformPaint;reload(prDeformPaint)
ui = prDeformPaint.Ui()
ui.enterTool()
mc.select('half')

prDeformPaint.reinitializeMaya()
#prDeformPaint.initializeMaya('/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py',
#                             '/home/prthlein/private/code/prmaya/prmaya/scripts/prDeformPaintBrush.mel')
#prDeformPaint.reinitializeMaya()

