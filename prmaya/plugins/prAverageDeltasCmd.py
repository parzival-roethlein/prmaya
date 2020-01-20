"""


USAGE:

"""

import sys
from itertools import izip


import maya.api.OpenMaya as om


class prAverageDeltasCmd(om.MPxCommand):

    PLUGIN_NAME = 'prAverageDeltasCmd'

    def __init__(self):
        om.MPxCommand.__init__(self)
        self.space = None
        self.drivenIter = None
        self.deformationDeltas = None
        self.deformationPositions = None

    def doIt(self, args):
        """
        :param args: baseMesh, drivenMesh, om.MSpace.kObject, [vertexId_1, ...], [weight_1, ...], weight
        :return:
        """
        baseMesh = args.asString(0)
        drivenMesh = args.asString(1)
        self.space = args.asInt(2)
        vertexIds = args.asIntArray(3)
        vertexWeights = args.asDoubleArray(4)
        weight = args.asFloat(5)
        if len(vertexIds) != len(vertexWeights):
            raise ValueError('len(vertexIds) != len(vertexWeights) // {0} != {1}'.format(
                             len(vertexIds), len(vertexWeights)))
        selection = om.MSelectionList()
        selection.add(baseMesh)
        baseIter = om.MItMeshVertex(selection.getDagPath(0))
        selection.add(drivenMesh)
        self.drivenIter = om.MItMeshVertex(selection.getDagPath(1))
        self.deformationDeltas = {}
        self.deformationPositions = {}

        deltas = {}
        # calculate deformation delta
        for vertexId, vertexWeight in izip(vertexIds, vertexWeights):
            self.drivenIter.setIndex(vertexId)

            # get average delta
            averageDelta = om.MVector()
            neighborVtxIds = self.drivenIter.getConnectedVertices()
            for neighborVtxId in neighborVtxIds:
                if neighborVtxId not in deltas:
                    baseIter.setIndex(neighborVtxId)
                    self.drivenIter.setIndex(neighborVtxId)
                    deltas[neighborVtxId] = (self.drivenIter.position(self.space) -
                                             baseIter.position(self.space))
                averageDelta += deltas[neighborVtxId]
            if averageDelta.length() == 0.0:
                continue
            averageDelta *= 1.0 / len(neighborVtxIds)

            # final delta
            baseIter.setIndex(vertexId)
            self.drivenIter.setIndex(vertexId)
            drivenPosition = self.drivenIter.position(self.space)
            delta = (baseIter.position(self.space) + averageDelta -
                     drivenPosition) * vertexWeight * weight

            position = drivenPosition + delta
            self.drivenIter.setPosition(position, self.space)

            # for undo
            self.deformationDeltas[vertexId] = delta
            # for redo
            self.deformationPositions[vertexId] = position

    def redoIt(self):
        for vertexId, position in self.deformationPositions.iteritems():
            self.drivenIter.setIndex(vertexId)
            self.drivenIter.setPosition(position, self.space)

    def undoIt(self):
        for vertexId, delta in self.deformationDeltas.iteritems():
            self.drivenIter.setIndex(vertexId)
            self.drivenIter.setPosition(
                    self.drivenIter.position(self.space) - delta, self.space)

    @staticmethod
    def creator():
        return prAverageDeltasCmd()

    def isUndoable(self):
        return True


def maya_useNewAPI():
    pass


def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, "Parzival Roethlein", "0.0.1", "Any")
    try:
        plugin.registerCommand(prAverageDeltasCmd.PLUGIN_NAME, prAverageDeltasCmd.creator)
    except:
        sys.stderr.write("Failed to register command\n")
        raise


def uninitializePlugin(obj):
    plugin = om.MFnPlugin(obj)
    try:
        plugin.deregisterCommand(prAverageDeltasCmd.PLUGIN_NAME)
    except:
        sys.stderr.write("Failed to deregister command\n")
        raise

