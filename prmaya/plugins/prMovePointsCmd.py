"""
move mesh vertex

# TODO
- proper MPxCommand argument usage


# TEST
import maya.cmds as mc
mc.file(new=True, force=True)
mc.unloadPlugin('prMovePointsCmd.py')
mc.loadPlugin('/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py')

from prmaya.plugins import prMovePointsCmd;reload(prMovePointsCmd)
mc.setAttr(cube+'.s', 100, 100, 100)

movePoints(mesh=cube, deltas=[[0, -0.5, 0]])
movePoints(mesh=cube, deltas={4: [0, 0.5, 0]})
movePoints(mesh=cube, deltas={5: om.MVector([0, 0.5, 0])})

"""

import sys

import maya.cmds as mc
import maya.api.OpenMaya as om


def movePoints(mesh, deltas, space=om.MSpace.kObject):
    """
    simplified interface to run PrMovePointsCmd

    :param mesh: mesh shape name
    :param deltas: see PrMovePointsCmd.convert_deltas_to_cmd_args
    :param space: om.kSpace.kObject
    :return:
    """
    ids, vectors = PrMovePointsCmd.convert_deltas_to_cmd_args(deltas)
    mc.prMovePointsCmd(mesh, ids, vectors, space)


class PrMovePointsCmd(om.MPxCommand):

    PLUGIN_NAME = 'prMovePointsCmd'

    @staticmethod
    def convert_deltas_to_cmd_args(deltas):
        """
        convert different types of given deltas to flat lists (MPxCommand arguments type limitation)
        :param deltas: indexed vector dict // list of vectors // MVectorArray // MPointArray
        :return: (vertexIds, flatVectorList) : ([0, 1, ...], [1.0, 0.0, ...])
        """
        vertexIds = []
        flatVectorList = []

        if isinstance(deltas, dict):
            for pointId, vec in deltas.iteritems():
                vertexIds.append(pointId)
                flatVectorList += [vec[0], vec[1], vec[2]]

        if isinstance(deltas, list) or isinstance(deltas, om.MVectorArray) or isinstance(deltas, om.MPointArray):
            vertexIds = list(range(len(deltas)))
            for vec in deltas:
                flatVectorList += [vec[0], vec[1], vec[2]]
        return vertexIds, flatVectorList

    @staticmethod
    def convert_cmd_args_to_deltas(vertexIds, vectors):
        """
        convert a list of vertex ids and a flat vector list to an indexed MVector dict
        :param vertexIds: [0, 1, ...]
        :param vectors: [1.0, 0.0, ...]
        :return:
        """
        deltas = {}
        for x, vertexId in enumerate(vertexIds):
            deltas[vertexId] = om.MVector(vectors[x*3], vectors[x*3+1], vectors[x*3+2])
        return deltas

    def addDeltas(self, undoCall=False):
        selection = om.MSelectionList()
        selection.add(self.mesh)
        vertex_iter = om.MItMeshVertex(selection.getDagPath(0))
        for vertexId, delta in self.deltas.iteritems():
            vertex_iter.setIndex(vertexId)
            position = vertex_iter.position(space=self.space)
            if undoCall:
                position -= delta
            else:
                position += delta
            vertex_iter.setPosition(position, space=self.space)

    def __init__(self):
        om.MPxCommand.__init__(self)
        self.mesh = None
        self.deltas = None
        self.space = None
        self.undo_positions = None

    def doIt(self, args):
        self.mesh = args.asString(0)
        vertexIds = args.asIntArray(1)
        vectors = args.asDoubleArray(2)
        self.space = args.asInt(3)
        self.deltas = PrMovePointsCmd.convert_cmd_args_to_deltas(vertexIds=vertexIds, vectors=vectors)
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