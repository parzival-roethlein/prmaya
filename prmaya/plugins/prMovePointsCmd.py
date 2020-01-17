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


import maya.cmds as mc
import maya.api.OpenMaya as om


def movePoints(mesh, deltas, space=om.MSpace.kObject):
    """
    simplified interface to run PrMovePointsCmd

    :param mesh: mesh shape name
    :param deltas: {vertexId: MVector(), ...}
    :param space: om.kSpace.kObject
    :return:
    """
    mc.prMovePointsCmd(mesh, space, deltas.keys(), deltas.values())


class PrMovePointsCmd(om.MPxCommand):

    PLUGIN_NAME = 'prMovePointsCmd'

    def addDeltas(self, undoCall=False):
        for vertexId, delta in self.deltas.iteritems():
            self.vertexIterator.setIndex(vertexId)
            position = self.vertexIterator.position(space=self.space)
            if undoCall:
                position -= delta
            else:
                position += delta
            self.vertexIterator.setPosition(position, space=self.space)

    def __init__(self):
        om.MPxCommand.__init__(self)
        self.vertexIterator = None
        self.deltas = None
        self.space = None
        self.undo_positions = None

    def doIt(self, args):
        """
        :param args: meshName, space, vertexIdList, vector_1, vector_2, ... vector_n
        :return:
        """
        mesh = args.asString(0)
        selection = om.MSelectionList()
        selection.add(mesh)
        self.vertexIterator = om.MItMeshVertex(selection.getDagPath(0))
        self.space = args.asInt(1)
        vertexIds = args.asIntArray(2)
        if len(args)-3 != len(vertexIds):
            raise ValueError('vectorIds size: {0} does not match MVector count: {1}'.format(len(vertexIds), len(args)-3))
        self.deltas = {vert: args.asVector(vec) for vert, vec in izip(vertexIds, xrange(3, len(args)))}

        self.redoIt()

    def redoIt(self):
        self.addDeltas()

    def undoIt(self):
        self.addDeltas(undoCall=True)

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