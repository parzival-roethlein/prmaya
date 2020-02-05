
import maya.cmds as mc
import maya.api.OpenMaya as om
from prmaya.plugins import prAverageDeltasCmd
reload(prAverageDeltasCmd)

mc.file(newFile=True, force=True)
# mc.unloadPlugin('prAverageDeltasCmd.mll')
# mc.loadPlugin(r'C:\Users\paz\documents\visual studio 2015\Projects\prAverageDeltasCmd\prAverageDeltasCmd\Release\prAverageDeltasCmd.mll')
mc.unloadPlugin('prAverageDeltasCmd.py')
mc.loadPlugin('prAverageDeltasCmd.py')
# mc.file('C:/Users/paz/Documents/git/prmaya/test/plugins/test_prAverageDeltasCmd.ma', open=True, force=True)
mc.file('/home/prthlein/private/code/prmaya/test/plugins/test_prAverageDeltasCmd.ma', open=True, force=True)

mc.prAverageDeltasCmd('base', 'driven', om.MSpace.kObject, [213, 216], [1.0, 1.0], 0.5)

'''
# maya.OpenMaya
# time: 0.08 // 3 * (create iterator, getPos, addVector)
# time: 15.1 // 1 * (create iterator, getPos, addVector), 1 * setPos
# time: 15.7 // 3 * (create iterator, getPos, addVector), 1 * setPos

# maya.api.OpenMaya
# time: 0.04 // 3 * (create iterator, getPos, addVector)
# time: 13.8 // 1 * (create iterator, getPos, addVector), 1 * setPos
# time: 15.3 // 3 * (create iterator, getPos, addVector), 1 * setPos

import maya.OpenMaya as mom
import time

util = mom.MScriptUtil()
intPtr = util.asIntPtr()
start = time.time()

selection = mom.MSelectionList()
selection.add('half')
halfDagPath = mom.MDagPath()

selection.getDagPath(0, halfDagPath)
drivenIter = mom.MItMeshVertex(halfDagPath)
newPos = []
prev = 0
for x in range(drivenIter.count()):
    drivenIter.setIndex(x, intPtr)
    pos = drivenIter.position()
    pos += mom.MVector(0,10,0)
    newPos.append(pos)
    #drivenIter.setPosition(pos)
    
iter2 = mom.MItMeshVertex(halfDagPath)
for x in range(iter2.count()):
    iter2.setIndex(x, intPtr)
    pos = iter2.position()
    newPos[x] += mom.MVector(pos)

iter3 = mom.MItMeshVertex(halfDagPath)
for x in range(iter3.count()):
    iter3.setIndex(x, intPtr)
    pos = iter3.position()
    newPos[x] += mom.MVector(pos)*0.5

poses = []
for x in range(drivenIter.count()):
    drivenIter.setIndex(x, intPtr)
    #drivenIter.setPosition(newPos[x]+mom.MVector(0,1,0))

end = time.time()
print('time: {}'.format(end - start))
'''