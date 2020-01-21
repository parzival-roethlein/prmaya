"""
move mesh vertices with the Maya API (MItMeshVertex) for speed
made into MPxCommand for undo support

USAGE:
import maya.cmds as mc
import maya.api.OpenMaya as om
mc.polySphere(ch=False)
mc.prMovePointsCmd('pSphereShape1', om.MSpace.kObject, [294, 297, 280],
                   om.MVector(0, 0.25, 0), om.MVector(0, 0.5, 0), om.MVector(0, 1, 0))
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
        self.vertexIds = None
        self.deltas = None

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
        self.vertexIds = args.asIntArray(3)
        if len(args)-4 != len(self.vertexIds):
            raise ValueError('vectorIds size: {0} does not match MVector count: {1}'.format(
                             len(self.vertexIds), len(args)-4))
        selection = om.MSelectionList()
        selection.add(mesh)
        self.vertexIterator = om.MItMeshVertex(selection.getDagPath(0))
        vectors = [args.asVector(i) for i in range(4, len(args))]
        self.deltas = {vtx: vec for vtx, vec in izip(self.vertexIds, vectors)
                       if vec.length() > minDeltaLength}
        self.redoIt()

    def redoIt(self):
        self.addDeltas()

    def undoIt(self):
        self.addDeltas(undoCall=True)

    def addDeltas(self, undoCall=False):
        for vertexId, vector in self.deltas.iteritems():
            self.vertexIterator.setIndex(vertexId)
            position = self.vertexIterator.position(self.space)
            if undoCall:
                position -= vector
            else:
                position += vector
            self.vertexIterator.setPosition(position, self.space)

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

