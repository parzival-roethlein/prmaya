"""
# home
time average (with live target): 9.85
time average (without live target): 6.66

"""

import time
import maya.api.OpenMaya as om
import maya.cmds as mc

mc.file(newFile=True, force=True)
mc.unloadPlugin('prSetPointsCmd')
mc.loadPlugin(r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prSetPointsCmd.py')

mesh = mc.polySphere(radius=10, ch=False, subdivisionsAxis=130, subdivisionsHeight=80)[0]
target = mc.polySphere(radius=12, ch=False, subdivisionsAxis=130, subdivisionsHeight=80)[0]
blendshape = mc.blendShape([target, mesh])[0]
mc.setAttr(blendshape+'.'+target, 0.5)
joint = mc.createNode('joint')
mc.skinCluster(mesh, joint)
mc.setAttr(joint+'.rx', 90)
mc.sculptTarget(blendshape, e=True, target=0)

vectorIds = range(0, mc.polyEvaluate(mesh, vertex=True), 2)
startPositions = om.MPointArray()
for vectorId in vectorIds:
    startPositions.append(
        om.MPoint(
            mc.xform('{0}.vtx[{1}]'.format(mesh, vectorId),
                     q=True, t=True, ws=True)))

targetPositions = [p+om.MVector(0, 0.5, 0) for x, p in zip(vectorIds, startPositions)]

times = []
for x in range(2):
    start = time.time()
    mc.prSetPointsCmd(mesh, om.MSpace.kObject, vectorIds, *targetPositions)
    end = time.time()
    times.append(end-start)
print('time average (with live target): {}'.format(round(sum(times)/len(times), 2)))
mc.delete(target)
times = [] 
for x in range(2):
    start = time.time()
    mc.prSetPointsCmd(mesh, om.MSpace.kObject, vectorIds, *targetPositions)
    end = time.time()
    times.append(end-start)
print('time average (without live target): {}'.format(round(sum(times)/len(times), 2)))

