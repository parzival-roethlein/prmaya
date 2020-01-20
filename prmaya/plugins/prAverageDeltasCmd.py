"""


USAGE:

"""

import sys
from itertools import izip


import maya.api.OpenMaya as om


class prAverageDeltasCmd(om.MPxCommand):

    PLUGIN_NAME = 'prAverageDeltasCmd'

    def addDeltas(self, undoCall=False):
        print('deltas: {}'.format(len(self.deltas)))
        for vertexId, delta in self.deltas.iteritems():
            self.drivenIter.setIndex(vertexId)
            position = self.drivenIter.position(self.space)
            if undoCall:
                position -= delta
            else:
                position += delta
            self.drivenIter.setPosition(position, self.space)

    def __init__(self):
        om.MPxCommand.__init__(self)
        self.drivenIter = None
        self.deltas = None
        self.space = None

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
        self.deltas = {}
        baseDeltas = {}

        # calculate deformation delta
        for vertexId, vertexWeight in izip(vertexIds, vertexWeights):
            self.drivenIter.setIndex(vertexId)

            # get average delta
            averageDelta = om.MVector()
            neighborVtxIds = self.drivenIter.getConnectedVertices()
            for neighborVtxId in neighborVtxIds:
                if neighborVtxId not in baseDeltas:
                    baseIter.setIndex(neighborVtxId)
                    self.drivenIter.setIndex(neighborVtxId)
                    baseDeltas[neighborVtxId] = (self.drivenIter.position(self.space) -
                                                 baseIter.position(self.space))
                averageDelta += baseDeltas[neighborVtxId]
            if averageDelta.length() == 0.0:
                continue
            averageDelta *= 1.0/len(neighborVtxIds)

            # final delta
            self.drivenIter.setIndex(vertexId)
            baseIter.setIndex(vertexId)
            self.deltas[vertexId] = (
                (baseIter.position(self.space) + averageDelta -
                 self.drivenIter.position(self.space)) * vertexWeight * weight
            )
        self.redoIt()

    def redoIt(self):
        self.addDeltas()

    def undoIt(self):
        self.addDeltas(undoCall=True)

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

