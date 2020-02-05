"""
Move mesh vertices (add vectors) with undo/redo support

USAGE:
import maya.cmds as mc
mc.prMovePointsCmd('pSphereShape1',
                   om.MSpace.kObject,
                   [3, ..., 1],
                   om.MVector(1, 0, 0), ..., om.MVector(0, 1, 0))



PERFORMANCE TEST
1. MFnMesh getPoint(), setPoint()
doIt = 14.58
undo = 13.23
redo = 12.79
2. MItMeshVertex setIndex(), position(), setPosition()
doIt = 13.72
undo = 13.91
redo = 13.64
= MFnMesh (doIt) is slower (MFnMesh() initialization?!), but undo/redo is faster.
  Because doIt is the most important, i'm sticking with MItMeshVertex
"""

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

    @staticmethod
    def creator():
        return PrMovePointsCmd()

    def isUndoable(self):
        return True


def maya_useNewAPI():
    pass


def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, "Parzival Roethlein", "1.0.0", "Any")
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

