"""
move mesh vertices with the Maya API (MItMeshVertex) for speed
made into MPxCommand for undo support

USAGE:
import maya.cmds as mc
import maya.api.OpenMaya as om
mc.polySphere(ch=False)
mc.prMovePointsCmd('pSphereShape1', om.MSpace.kObject, [294, 297, 280],
                   om.MVector(0, 0.25, 0), om.MVector(0, 0.5, 0), om.MVector(0, 1, 0))

PERFORMANCE TEST (4.3k vertices)
- MFnMesh getPoint(), setPoint()
has similar calculation times as
- MItMeshVertex setIndex(), position(), setPosition()
MFnMesh (doIt) is slower (MFnMesh() initialization?!), but undo/redo is faster.
Because doIt is the most important, i'm sticking with MItMeshVertex

MFnMesh
time: 15.26 // doIt
time: 15.23 // doIt
time: 14.69 // doIt
time: 13.40 // doIt
time: 15.21 // doIt
time: 13.17 // doIt
time: 15.07 // doIt = 14.58
time: 13.20 // undo
time: 12.29 // undo
time: 14.02 // undo
time: 13.48 // undo
time: 13.24 // undo
time: 13.77 // undo
time: 12.61 // undo = 13.23
time: 14.52 // redo
time: 12.21 // redo
time: 12.14 // redo
time: 12.25 // redo
time: 12.47 // redo
time: 12.50 // redo
time: 13.46 // redo = 12.79

# MItMeshFaceVertex
time: 13.91 // doIt
time: 13.33 // doIt
time: 13.21 // doIt
time: 14.05 // doIt
time: 14.13 // doIt
time: 13.88 // doIt
time: 13.53 // doIt = 13.72
time: 14.18 // undo
time: 13.72 // undo
time: 13.59 // undo
time: 13.76 // undo
time: 14.29 // undo
time: 13.80 // undo
time: 14.01 // undo = 13.91
time: 13.90 // redo
time: 14.51 // redo
time: 13.08 // redo
time: 13.69 // redo
time: 13.02 // redo
time: 13.14 // redo
time: 14.17 // redo = 13.64
"""
# import time
import sys
from itertools import izip

import maya.api.OpenMaya as om


class PrMovePointsCmd(om.MPxCommand):

    PLUGIN_NAME = 'prMovePointsCmd'

    def __init__(self):
        om.MPxCommand.__init__(self)
        self.space = None
        self.vertexIterator = None
        self.vertexIds = []
        self.deltas = []

    def doIt(self, args):
        """
        :param args: meshName, space, minDeltaLength (ignore if smaller),
                     vertexIdList (n-length),
                     vector_1, vector_2, ... vector_n
        :return:
        """
        mesh = args.asString(0)
        self.space = args.asInt(1)
        minDeltaLength = args.asDouble(2)
        vertexIds = args.asIntArray(3)
        if len(args)-4 != len(vertexIds):
            raise ValueError('vectorIds size: {0} does not match MVector count: {1}'.format(
                             len(vertexIds), len(args)-4))
        selection = om.MSelectionList()
        selection.add(mesh)
        self.vertexIterator = om.MItMeshVertex(selection.getDagPath(0))
        # self.vertexIterator = om.MFnMesh(selection.getDagPath(0))
        for vertexId, deltaArgPosition in izip(vertexIds, range(4, len(args))):
            delta = args.asVector(deltaArgPosition)
            if delta.length() < minDeltaLength:
                continue
            self.vertexIds.append(vertexId)
            self.deltas.append(delta)

        self.redoIt()

    def redoIt(self):
        self.addDeltas()

    def undoIt(self):
        self.addDeltas(undoCall=True)

    def addDeltas(self, undoCall=False):
        # start = time.time()

        for vertexId, vector in izip(self.vertexIds, self.deltas):
            self.vertexIterator.setIndex(vertexId)
            position = self.vertexIterator.position(self.space)
            # position = self.vertexIterator.getPoint(vertexId, self.space)
            if undoCall:
                position -= vector
            else:
                position += vector
            self.vertexIterator.setPosition(position, self.space)
            # self.vertexIterator.setPoint(vertexId, position, self.space)
        # if undoCall:
        #     print('time: {:.2f} // undo'.format(time.time() - start))
        # else:
        #     print('time: {:.2f} // redo'.format(time.time() - start))

    @staticmethod
    def creator():
        return PrMovePointsCmd()

    def isUndoable(self):
        return True


def maya_useNewAPI():
    pass


def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, "Parzival Roethlein", "0.0.1", "Any")
    try:
        plugin.registerCommand(PrMovePointsCmd.PLUGIN_NAME, PrMovePointsCmd.creator)
    except:
        sys.stderr.write("Failed to register command\n")
        raise


def uninitializePlugin(obj):
    plugin = om.MFnPlugin(obj)
    try:
        plugin.deregisterCommand(PrMovePointsCmd.PLUGIN_NAME)
    except:
        sys.stderr.write("Failed to deregister command\n")
        raise

