"""
# target mesh in scene
prMovePointsCmd.py  (MItMeshVertex) # 10.18
prMovePointsCmd.mll (MFnMesh) # 10.19

# deleted target mesh
prMovePointsCmd.py  (MItMeshVertex) # 6.63
prMovePointsCmd.mll (MFnMesh) # 6.63
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
mc.delete(target)
mc.setAttr(blendshape+'.'+target, 0.5)
joint = mc.createNode('joint')
mc.skinCluster(mesh, joint)
mc.setAttr(joint+'.rx', 90)
mc.sculptTarget(blendshape, e=True, target=0)

vectorIds = range(0, mc.polyEvaluate(mesh, vertex=True), 2)
vectors = [om.MVector(0, 0.5, 0) for x in vectorIds]



times = []
for x in range(5):
    start = time.time()
    mc.prMovePointsCmd(mesh, om.MSpace.kLast, 0.00001, vectorIds, *vectors)
    end = time.time()
    times.append(end-start)
print('time average: {}'.format(round(sum(times)/len(times), 2)))

