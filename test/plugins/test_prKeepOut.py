"""

mc.file(new=True, force=True)
mc.unloadPlugin('prKeepOut')
mc.file(new=True, force=True)
mc.loadPlugin(r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prKeepOut.py')
mc.file(r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prKeepOut.ma', open=True, force=True)
mc.select('prKeepOut1')

r'/home/prthlein/private/code/prmaya/test/plugins/test_prClosestPoint.ma'

mc.file(new=True, force=True)
mc.unloadPlugin('prKeepOut')
mc.file(new=True, force=True)
mc.loadPlugin(r'/home/prthlein/private/code/prmaya/prmaya/plugins/prKeepOut.py')
mc.file('/home/prthlein/private/code/prmaya/test/plugins/test_prKeepOut.ma', open=True, force=True)
mc.select('prKeepOut1')


"""