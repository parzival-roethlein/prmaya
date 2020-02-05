"""
set mesh point positions

USAGE:
import maya.cmds as mc
mc.prSetPointsCmd('pSphereShape1',
                  om.MSpace.kObject,
                  [3, ..., 1],
                  om.MPoint(1, 0, 0), ..., om.MPoint(0, 1, 0))

"""

import sys
from itertools import izip

import maya.cmds as mc

import maya.api.OpenMaya as om


def setPoints(mesh, points, space=om.MSpace.kObject):
    if isinstance(points, om.MPointArray):
        vertexIds = range(0, len(points))
    elif isinstance(points, list):
        vertexIds = range(0, len(points))
        points = [om.MPoint(p) for p in points]
    elif isinstance(points, dict):
        vertexIds = points.keys()
        points = [om.MPoint(p) for p in points.values()]
    else:
        raise ValueError('Unknown points type: {}'.format(points))
    mc.prSetPointsCmd(mesh, space, vertexIds, *points)


class PrSetPointsCmd(om.MPxCommand):

    PLUGIN_NAME = 'prSetPointsCmd'

    def __init__(self):
        om.MPxCommand.__init__(self)
        self.space = None
        self.vertexIterator = None
        self.vertexIds = []
        self.points = om.MPointArray()
        self.deltas = om.MVectorArray()

    def doIt(self, args):
        """
        :param args: meshName, space, vertexIdList (n-length),
                     point_1, point_2, ... point_n
        :return:
        """
        mesh = args.asString(0)
        self.space = args.asInt(1)
        self.vertexIds = args.asIntArray(2)
        if len(args)-3 != len(self.vertexIds):
            raise ValueError('vectorIds size: {0} does not match MPoint count: {1}'.format(
                             len(self.vertexIds), len(args)-3))
        selection = om.MSelectionList()
        selection.add(mesh)
        self.vertexIterator = om.MItMeshVertex(selection.getDagPath(0))
        for vertexId, pointArgPosition in izip(self.vertexIds, range(3, len(args))):
            self.points.append(args.asPoint(pointArgPosition))
        self.redoIt()

    def redoIt(self):
        for vertexId, targetPosition in izip(self.vertexIds, self.points):
            self.vertexIterator.setIndex(vertexId)
            startPosition = self.vertexIterator.position(self.space)
            self.deltas.append(targetPosition-startPosition)
            self.vertexIterator.setPosition(targetPosition, self.space)

    def undoIt(self):
        for vertexId, vector in izip(self.vertexIds, self.deltas):
            self.vertexIterator.setIndex(vertexId)
            position = self.vertexIterator.position(self.space) - vector
            self.vertexIterator.setPosition(position, self.space)

    @staticmethod
    def creator():
        return PrSetPointsCmd()

    def isUndoable(self):
        return True


def maya_useNewAPI():
    pass


def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, "Parzival Roethlein", "1.0.0", "Any")
    try:
        plugin.registerCommand(PrSetPointsCmd.PLUGIN_NAME, PrSetPointsCmd.creator)
    except:
        sys.stderr.write("Failed to register command\n")
        raise


def uninitializePlugin(obj):
    plugin = om.MFnPlugin(obj)
    try:
        plugin.deregisterCommand(PrSetPointsCmd.PLUGIN_NAME)
    except:
        sys.stderr.write("Failed to deregister command\n")
        raise

