"""

mc.file(new=True, force=True)
mc.unloadPlugin('prKeepOut')
mc.file(new=True, force=True)
mc.loadPlugin(r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prKeepOut')
mc.file(open=r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prKeepOut.ma', open=True, force=True)
mc.select('prKeepOut1')

"""