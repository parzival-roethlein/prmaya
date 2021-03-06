"""
# home
time average (with live target): 9.61
time average (without live target): 6.57

"""
import time
import maya.api.OpenMaya as om
import maya.cmds as mc
mc.file(newFile=True, force=True)
mc.unloadPlugin('prMovePointsCmd')
mc.loadPlugin(r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prMovePointsCmd.py')
#mc.loadPlugin(r'C:\Users\paz\documents\visual studio 2015\Projects\prMovePointsCmd\prMovePointsCmd\Release\prMovePointsCmd.mll')

mesh = mc.polySphere(radius=10, ch=False, subdivisionsAxis=130, subdivisionsHeight=80)[0]
target = mc.polySphere(radius=12, ch=False, subdivisionsAxis=130, subdivisionsHeight=80)[0]
blendshape = mc.blendShape([target, mesh])[0]

mc.setAttr(blendshape+'.'+target, 0.5)
joint = mc.createNode('joint')
mc.skinCluster(mesh, joint)
mc.setAttr(joint+'.rx', 90)
mc.sculptTarget(blendshape, e=True, target=0)

vectorIds = range(0, mc.polyEvaluate(mesh, vertex=True), 2)
vectors = [om.MVector(0, 0.5, 0) for x in vectorIds]

times = []
for x in range(2):
    start = time.time()
    mc.prMovePointsCmd(mesh, om.MSpace.kObject, 0.00001, vectorIds, *vectors)
    end = time.time()
    times.append(end-start)
print('time average (with live target): {}'.format(round(sum(times)/len(times), 2)))
mc.delete(target)
times = []
for x in range(2):
    start = time.time()
    mc.prMovePointsCmd(mesh, om.MSpace.kObject, 0.00001, vectorIds, *vectors)
    end = time.time()
    times.append(end-start)
print('time average (without live target): {}'.format(round(sum(times)/len(times), 2)))
