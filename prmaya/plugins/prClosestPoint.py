"""
DESCRIPTION
Deformer that moves mesh vertices towards: position / mesh shape / mesh vertex / curve shape / nurbs-surface shape

USE CASES
- Modeling: Interactively snap vertices between meshes (closest mesh vertex option)
- Modeling/Rigging: Interactively match shapes of different geometries
- Rigging/Animation: Sticky lips deformation

USAGE
- After loading the plug-in via Window->Settings->Prefs->Plug-in Manager
- Automated setup:
  Select driver then driven and execute MEL command: "prClosestPoint"
- Manual setup:
  1. Select driven mesh, then execute (MEL): deformer -type "prClosestPoint"
  2. Connect input target(s)
    2.1. myMeshShape.outShape >> prClosestPoint.inputMesh
    2.2. myCurveShape.worldSpace >> prClosestPoint.inputCurve
    ...

ATTRIBUTES
setup:
- inputMeshWorldMatrix: expects mesh shape "worldMatrix" input
- inputMeshShape: expects mesh shape "outMesh" input
- inputCurveShape: ...
- inputCurveWorldMatrix: ...
- inputSurfaceShape: ...
- inputSurfaceWorldMatrix: ...
control:
- maxDistance: Only vertices closer than maxDistance are affected. Value of 0.0 will disable maxDistance and falloff
- falloffEnabled: Bool if falloff ramp should be used
- falloff: Ramp that controls the amount of displacement of points within maxDistance
- scaleMaxDistanceU: Rescale maxDistance, depending on U value of closest point on target (Ramp maps U value from 0.0 to 1.0)
- inputMeshClosestVertex: change from closestPoint to closest vertex
inherited:
- envelope: Multiply deformation effect
- weights: Paintable per vertex envelope

TIPS
- For sticky lips: Set envelope value over 1.0, to overshoot vertices at closed mouth position, to have closed geometry after smoothing/subdividing
- Improve performance by either removing unaffected vertices with the Edit membership tools or painting their weights attribute value to 0.0

LINKS
- Demo:
# TODO
- Making-off:
# TODO
- This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author:
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- inputMeshMatrix not working properly (currently inputMesh transform has to be at scene root)
- make all target attributes arrays
- creation script should work with vertex selection

TODO MAYBE
- find out why worldMesh as inputMesh does not trigger evaluation when transforming transform (only a problem with mesh)
- should maxDistance be a maya unit attribute?

VERSION
2018-09-26 / 0.0.1: Forked from prAttractNode / renamed to prClosestPoint / made work with latest Maya versions / major attribute changes
"""

import sys
from collections import defaultdict
from itertools import izip

import maya.OpenMaya as om
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as mc
import maya.mel as mm


class prClosestPoint(OpenMayaMPx.MPxDeformerNode):
    nodeTypeName = 'prClosestPoint'
    nodeTypeId = om.MTypeId(0x0004C262)  # local, not save
    
    if om.MGlobal.apiVersion() < 201600:
        envelope = OpenMayaMPx.cvar.MPxDeformerNode_envelope
        inputGeometry = OpenMayaMPx.cvar.MPxDeformerNode_inputGeom
        outputGeometry = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    else:
        envelope = OpenMayaMPx.cvar.MPxGeometryFilter_envelope
        inputGeometry = OpenMayaMPx.cvar.MPxGeometryFilter_inputGeom
        outputGeometry = OpenMayaMPx.cvar.MPxGeometryFilter_outputGeom
    
    @staticmethod
    def initialize():
        typedAttr = om.MFnTypedAttribute()
        numericAttr = om.MFnNumericAttribute()
        matrixAttr = om.MFnMatrixAttribute()
        rampAttr = om.MRampAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        
        prClosestPoint.displayWarnings = numericAttr.create('displayWarnings', 'displayWarnings', om.MFnNumericData.kBoolean, True)
        prClosestPoint.addAttribute(prClosestPoint.displayWarnings)
        
        # maxDistance
        prClosestPoint.maxDistance = numericAttr.create('maxDistance', 'maxDistance', om.MFnNumericData.kFloat, 1.0)
        numericAttr.setKeyable(True)
        numericAttr.setMin(0.0)
        prClosestPoint.addAttribute(prClosestPoint.maxDistance)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistance, prClosestPoint.outputGeometry)
        
        prClosestPoint.maxDistanceUScaleEnabled = numericAttr.create('maxDistanceUScaleEnabled', 'maxDistanceUScaleEnabled', om.MFnNumericData.kBoolean, False)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.maxDistanceUScaleEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistanceUScaleEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.maxDistanceUScale = rampAttr.createCurveRamp('maxDistanceUScale', 'maxDistanceUScale')
        prClosestPoint.addAttribute(prClosestPoint.maxDistanceUScale)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistanceUScale, prClosestPoint.outputGeometry)
        
        prClosestPoint.maxDistanceVScaleEnabled = numericAttr.create('maxDistanceVScaleEnabled', 'maxDistanceVScaleEnabled', om.MFnNumericData.kBoolean, False)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.maxDistanceVScaleEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistanceVScaleEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.maxDistanceVScale = rampAttr.createCurveRamp('maxDistanceVScale', 'maxDistanceVScale')
        prClosestPoint.addAttribute(prClosestPoint.maxDistanceVScale)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistanceVScale, prClosestPoint.outputGeometry)
        
        # falloff
        prClosestPoint.falloffEnabled = numericAttr.create('falloffEnabled', 'falloffEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.falloffEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.falloffEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.falloff = rampAttr.createCurveRamp('falloff', 'falloff')
        prClosestPoint.addAttribute(prClosestPoint.falloff)
        prClosestPoint.attributeAffects(prClosestPoint.falloff, prClosestPoint.outputGeometry)
        
        # inputPosition
        prClosestPoint.inputPositionEnabled = numericAttr.create('inputPositionEnabled', 'inputPositionEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.inputPositionEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.inputPositionEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputPositionX = numericAttr.create('inputPositionX', 'inputPositionX', om.MFnNumericData.kFloat, 0.0)
        prClosestPoint.addAttribute(prClosestPoint.inputPositionX)
        prClosestPoint.attributeAffects(prClosestPoint.inputPositionX, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputPositionY = numericAttr.create('inputPositionY', 'inputPositionY', om.MFnNumericData.kFloat, 0.0)
        prClosestPoint.addAttribute(prClosestPoint.inputPositionY)
        prClosestPoint.attributeAffects(prClosestPoint.inputPositionY, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputPositionZ = numericAttr.create('inputPositionZ', 'inputPositionZ', om.MFnNumericData.kFloat, 0.0)
        prClosestPoint.addAttribute(prClosestPoint.inputPositionZ)
        prClosestPoint.attributeAffects(prClosestPoint.inputPositionZ, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputPosition = compoundAttr.create('inputPosition', 'inputPosition')
        compoundAttr.addChild(prClosestPoint.inputPositionX)
        compoundAttr.addChild(prClosestPoint.inputPositionY)
        compoundAttr.addChild(prClosestPoint.inputPositionZ)
        compoundAttr.setArray(True)
        prClosestPoint.addAttribute(prClosestPoint.inputPosition)
        prClosestPoint.attributeAffects(prClosestPoint.inputPosition, prClosestPoint.outputGeometry)
        
        # inputMesh
        prClosestPoint.inputMeshEnabled = numericAttr.create('inputMeshEnabled', 'inputMeshEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.inputMeshEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.inputMeshEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputMeshShape = typedAttr.create('inputMeshShape', 'inputMeshShape', om.MFnMeshData.kMesh)
        prClosestPoint.addAttribute(prClosestPoint.inputMeshShape)
        prClosestPoint.attributeAffects(prClosestPoint.inputMeshShape, prClosestPoint.outputGeometry)
        '''
        prClosestPoint.inputMeshWorldMatrix = matrixAttr.create('inputMeshWorldMatrix', 'inputMeshWorldMatrix')
        prClosestPoint.addAttribute(prClosestPoint.inputMeshWorldMatrix)
        prClosestPoint.attributeAffects(prClosestPoint.inputMeshWorldMatrix, prClosestPoint.outputGeometry)
        '''
        prClosestPoint.inputMeshClosestVertex = numericAttr.create('inputMeshClosestVertex', 'inputMeshClosestVertex', om.MFnNumericData.kFloat, 0.0)
        numericAttr.setKeyable(True)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        prClosestPoint.addAttribute(prClosestPoint.inputMeshClosestVertex)
        prClosestPoint.attributeAffects(prClosestPoint.inputMeshClosestVertex, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputMesh = compoundAttr.create('inputMesh', 'inputMesh')
        compoundAttr.addChild(prClosestPoint.inputMeshShape)
        #compoundAttr.addChild(prClosestPoint.inputMeshWorldMatrix)
        compoundAttr.addChild(prClosestPoint.inputMeshClosestVertex)
        prClosestPoint.addAttribute(prClosestPoint.inputMesh)
        prClosestPoint.attributeAffects(prClosestPoint.inputMesh, prClosestPoint.outputGeometry)
        
        # inputCurve
        prClosestPoint.inputCurveEnabled = numericAttr.create('inputCurveEnabled', 'inputCurveEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.inputCurveEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.inputCurveEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputCurveShape = typedAttr.create('inputCurveShape', 'inputCurveShape', om.MFnNurbsCurveData.kNurbsCurve)
        prClosestPoint.addAttribute(prClosestPoint.inputCurveShape)
        prClosestPoint.attributeAffects(prClosestPoint.inputCurveShape, prClosestPoint.outputGeometry)
        
        # inputSurface
        prClosestPoint.inputSurfaceEnabled = numericAttr.create('inputSurfaceEnabled', 'inputSurfaceEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.inputSurfaceEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.inputSurfaceEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputSurfaceShape = typedAttr.create('inputSurfaceShape', 'inputSurfaceShape', om.MFnNurbsSurfaceData.kNurbsSurface)
        prClosestPoint.addAttribute(prClosestPoint.inputSurfaceShape)
        prClosestPoint.attributeAffects(prClosestPoint.inputSurfaceShape, prClosestPoint.outputGeometry)
        
        # paintable
        mc.makePaintable('prClosestPoint', 'weights', attrType='multiFloat', shapeMode='deformer')
    
    @staticmethod
    def creator():
        return prClosestPoint()
    
    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
        self.__membership__ = defaultdict(list)
        self.__weights__ = {}
        self.__weightsDirty__ = defaultdict(lambda: True)

    def setDependentsDirty(self, plug, plugArray):
        if plug == self.weights:
            self.__weightsDirty__[plug.parent().logicalIndex()] = True
    
    def accessoryNodeSetup(self, cmd):
        thisNode = self.thisMObject()
        
        falloffAttr = om.MRampAttribute(thisNode, self.falloff)
        positions = om.MFloatArray()
        values = om.MFloatArray()
        interpolations = om.MIntArray()
        positions.append(float(0.0))
        positions.append(float(1.0))
        values.append(float(0.0))
        values.append(float(1.0))
        interpolations.append(om.MRampAttribute.kLinear)
        interpolations.append(om.MRampAttribute.kLinear)
        falloffAttr.addEntries(positions, values, interpolations)
        
        for uvAttr in [self.maxDistanceUScale, self.maxDistanceVScale]:
            maxDistanceUVAttr = om.MRampAttribute(thisNode, uvAttr)
            positions = om.MFloatArray()
            values = om.MFloatArray()
            interpolations = om.MIntArray()
            positions.append(float(0.5))
            values.append(float(1.0))
            interpolations.append(om.MRampAttribute.kLinear)
            maxDistanceUVAttr.addEntries(positions, values, interpolations)
    
    def deform(self, block, iterator, localToWorldMatrix, multiIndex):
        thisNode = self.thisMObject()
        envelope = block.inputValue(self.envelope).asFloat()
        if envelope == 0.0:
            return
        
        maxDistance = block.inputValue(self.maxDistance).asFloat()
        maxDistanceUScaleEnabled = block.inputValue(self.maxDistanceUScaleEnabled).asBool()
        maxDistanceVScaleEnabled = block.inputValue(self.maxDistanceVScaleEnabled).asBool()
        if maxDistanceUScaleEnabled or maxDistanceVScaleEnabled:
            float2Util = om.MScriptUtil()
            float2Util.createFromList([0.0, 0.0], 2)
            float2Ptr = float2Util.asFloat2Ptr()
        if maxDistanceUScaleEnabled:
            uValues = {}
        if maxDistanceVScaleEnabled:
            vValues = {}
        
        positionEnabled = block.inputValue(self.inputPositionEnabled).asBool()
        meshEnabled = block.inputValue(self.inputMeshEnabled).asBool()
        curveEnabled = block.inputValue(self.inputCurveEnabled).asBool()
        surfaceEnabled = block.inputValue(self.inputSurfaceEnabled).asBool()
        if not positionEnabled and not meshEnabled and not curveEnabled and not surfaceEnabled:
            return
        if curveEnabled or surfaceEnabled:
            doubleUtil = om.MScriptUtil()
            doubleUtil.createFromDouble(0.0)
            doublePtr = doubleUtil.asDoublePtr()
            doubleUtil2 = om.MScriptUtil()
            doubleUtil2.createFromDouble(0.0)
            doublePtr2 = doubleUtil2.asDoublePtr()
        
        falloffEnabled = block.inputValue(self.falloffEnabled).asBool()
        if falloffEnabled:
            falloffRampAttr = om.MRampAttribute(thisNode, self.falloff)
            floatPtrUtil = om.MScriptUtil()
            floatPtrUtil.createFromDouble(0.0)
            floatPtr = floatPtrUtil.asFloatPtr()
        
        iteratorCount = iterator.count()
        if iteratorCount == 0:
            return
        
        if len(self.__membership__[multiIndex]) != iteratorCount:
            self.__membership__[multiIndex] = []
            while not iterator.isDone():
                index = iterator.index()
                self.__membership__[multiIndex].append(index)
                iterator.next()
            iterator.reset()
        indices = self.__membership__[multiIndex]
        
        if self.__weightsDirty__[multiIndex]:
            self.__weights__[multiIndex] = []
            for index in self.__membership__[multiIndex]:
                self.__weights__[multiIndex].append(self.weightValue(block, multiIndex, index))
            self.__weightsDirty__[multiIndex] = False
        weights = self.__weights__[multiIndex]
        
        pointsWorldSpace = []
        while not iterator.isDone():
            pointsWorldSpace.append(iterator.position() * localToWorldMatrix)
            iterator.next()
        iterator.reset()
        
        deltas = {}
        
        if positionEnabled:
            inputPositionsHandle = block.inputArrayValue(self.inputPosition)
            for x in range(inputPositionsHandle.elementCount()):
                inputPositionsHandle.jumpToArrayElement(x)
                position = om.MPoint(*inputPositionsHandle.inputValue().asFloat3())
                for index, weight, point in izip(indices, weights, pointsWorldSpace):
                    if not weight:
                        continue
                    delta = position - point
                    if index in deltas and deltas[index].length() < delta.length():
                        continue
                    deltas[index] = delta
        
        if meshEnabled:
            # inputMeshWorldMatrix = block.inputValue(self.inputMeshWorldMatrix).asMatrix()
            # inputMeshWorldMatrixPlug = om.MPlug(thisNode, self.inputMeshWorldMatrix)
            # if displayWarnings and not inputMeshWorldMatrixPlug.isConnected():
            #     om.MGlobal.displayWarning('Missing input : {}'.format(inputMeshWorldMatrixPlug.name()))
            meshHandle = block.inputValue(self.inputMeshShape)
            meshData = meshHandle.data()
            if not meshData.isNull():
                intUtil = om.MScriptUtil()
                intUtil.createFromInt(0)
                intPtr = intUtil.asIntPtr()
                # TODO: something is wrong with the matrix arg
                # meshIntersector = om.MMeshIntersector()
                # meshIntersector.create(meshData, inputMeshWorldMatrix)
                # closestPointOnMesh = om.MPointOnMesh()
                # meshIntersector.getClosestPoint(point, closestPointOnMesh)
                # faceId = closestPointOnMesh.faceIndex()
                # targetPoint = om.MPoint(closestPointOnMesh.getPoint())
                meshFn = om.MFnMesh(meshData)
                closestVertex = block.inputValue(self.inputMeshClosestVertex).asFloat()
                if closestVertex or maxDistanceUScaleEnabled or maxDistanceVScaleEnabled:
                    tempPoint = om.MPoint()
                for index, weight, point in izip(indices, weights, pointsWorldSpace):
                    if not weight:
                        continue
                    targetPoint = om.MPoint()
                    meshFn.getClosestPoint(point, targetPoint, om.MSpace.kWorld, intPtr)
                    if closestVertex:
                        faceVertices = om.MIntArray()
                        meshFn.getPolygonVertices(om.MScriptUtil(intPtr).asInt(), faceVertices)
                        shortestDistance = None
                        for vertexId in faceVertices:
                            meshFn.getPoint(vertexId, tempPoint, om.MSpace.kWorld)
                            vertexDistance = (point - tempPoint).length()
                            if shortestDistance is None or vertexDistance < shortestDistance:
                                shortestDistance = vertexDistance
                                closestVertexPoint = om.MPoint(tempPoint)
                        targetPoint = targetPoint * (1.0-closestVertex) + om.MVector(closestVertexPoint * closestVertex)
                    delta = targetPoint - point
                    if index in deltas and deltas[index].length() < delta.length():
                        continue
                    deltas[index] = targetPoint - point
                    if maxDistanceUScaleEnabled or maxDistanceVScaleEnabled:
                        meshFn.getUVAtPoint(targetPoint, float2Ptr, om.MSpace.kWorld)
                        if maxDistanceUScaleEnabled:
                            uValues[index] = float2Util.getFloat2ArrayItem(float2Ptr, 0, 0)
                        if maxDistanceVScaleEnabled:
                            vValues[index] = float2Util.getFloat2ArrayItem(float2Ptr, 0, 1)
        
        if curveEnabled:
            curveShapeData = block.inputValue(self.inputCurveShape).data()
            if not curveShapeData.isNull():
                curveShapeFn = om.MFnNurbsCurve(curveShapeData)
                for index, weight, point in izip(indices, weights, pointsWorldSpace):
                    if not weight:
                        continue
                    closestPoint = curveShapeFn.closestPoint(point, doublePtr, 0.00001, om.MSpace.kWorld)
                    delta = closestPoint - point
                    if index in deltas and deltas[index].length() < delta.length():
                        continue
                    deltas[index] = delta
                    if maxDistanceUScaleEnabled:
                        uValues[index] = om.MScriptUtil.getDouble(doublePtr) / curveShapeFn.numSpans()
                    if maxDistanceVScaleEnabled and index in vValues:
                        del(vValues[index])
        
        if surfaceEnabled:
            surfaceShapeData = block.inputValue(self.inputSurfaceShape).data()
            if not surfaceShapeData.isNull():
                surfaceShapeFn = om.MFnNurbsSurface(surfaceShapeData)
                for index, weight, point in izip(indices, weights, pointsWorldSpace):
                    if not weight:
                        continue
                    closestPoint = surfaceShapeFn.closestPoint(point, doublePtr, doublePtr2, False, 0.00001, om.MSpace.kWorld)
                    delta = closestPoint - point
                    if index in deltas and deltas[index].length() < delta.length():
                        continue
                    deltas[index] = delta
                    if maxDistanceUScaleEnabled:
                        uValues[index] = om.MScriptUtil.getDouble(doublePtr)
                    if maxDistanceVScaleEnabled:
                        vValues[index] = om.MScriptUtil.getDouble(doublePtr2)
        
        if maxDistanceUScaleEnabled:
            print 'u : ', uValues
        if maxDistanceVScaleEnabled:
            print 'v : ', vValues
        
        # maxDistance / falloff
        for vertexId, delta in deltas.iteritems():
            if maxDistance:
                deltaLength = delta.length()
                if deltaLength > maxDistance:
                    continue
                elif falloffEnabled:
                    lengthMaxDistancePercent = deltaLength / maxDistance
                    falloffRampAttr.getValueAtPosition(float(1.0 - lengthMaxDistancePercent), floatPtr)
                    falloff = om.MScriptUtil.getFloat(floatPtr)
                    delta *= falloff
            listIndex = indices.index(vertexId)
            pointsWorldSpace[listIndex] += delta * weights[listIndex] * envelope
        
        # final positions
        worldToLocalMatrix = localToWorldMatrix.inverse()
        pointsObjectSpace = om.MPointArray()
        for point in pointsWorldSpace:
            pointsObjectSpace.append(point * worldToLocalMatrix)
        iterator.setAllPositions(pointsObjectSpace)


def initializePlugin(obj):
    pluginFn = OpenMayaMPx.MFnPlugin(obj, 'Parzival Roethlein', '0.0.2')
    try:
        pluginFn.registerNode(prClosestPoint.nodeTypeName, prClosestPoint.nodeTypeId, prClosestPoint.creator,
                              prClosestPoint.initialize, OpenMayaMPx.MPxNode.kDeformerNode)
    except:
        sys.stderr.write('Failed to register node: {}'.format(prClosestPoint.nodeTypeName))
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = OpenMayaMPx.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prClosestPoint.nodeTypeId)
    except:
        sys.stderr.write('Failed to unregister node: {}'.format(prClosestPoint.nodeTypeName))


def evalAETemplate():
    mm.eval('''
    global proc AEprClosestPointTemplate( string $nodeName )
    {
        AEswatchDisplay $nodeName;
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prClosestPoint Attributes" -collapse 0;
                editorTemplate -beginLayout "maxDistance Attributes" -collapse 1;
                    editorTemplate -label "maxDistance" -addControl "maxDistance";
                    editorTemplate -label "maxDistanceUScaleEnabled" -addControl "maxDistanceUScaleEnabled";
                    AEaddRampControl ($nodeName+".maxDistanceUScale");
                    editorTemplate -label "maxDistanceVScaleEnabled" -addControl "maxDistanceVScaleEnabled";
                    AEaddRampControl ($nodeName+".maxDistanceVScale");
                editorTemplate -endLayout;
                editorTemplate -beginLayout "falloff Attributes" -collapse 1;
                    editorTemplate -label "falloffEnabled" -addControl "falloffEnabled";
                    AEaddRampControl ($nodeName+".falloff");
                editorTemplate -endLayout;
                editorTemplate -beginLayout "inputPosition Attributes" -collapse 1;
                    editorTemplate -label "inputPositionEnabled" -addControl "inputPositionEnabled";
                    editorTemplate -label "inputPosition" -addControl "inputPosition";
                editorTemplate -endLayout;
                editorTemplate -beginLayout "inputMesh Attributes" -collapse 1;
                    editorTemplate -label "inputMeshEnabled" -addControl "inputMeshEnabled";
                    editorTemplate -label "inputMesh" -addControl "inputMesh";
                editorTemplate -endLayout;
                editorTemplate -beginLayout "inputCurve Attributes" -collapse 1;
                    editorTemplate -label "inputCurveEnabled" -addControl "inputCurveEnabled";
                    editorTemplate -label "inputCurveShape" -addControl "inputCurveShape";
                editorTemplate -endLayout;
                editorTemplate -beginLayout "inputSurface Attributes" -collapse 1;
                    editorTemplate -label "inputSurfaceEnabled" -addControl "inputSurfaceEnabled";
                    editorTemplate -label "inputSurfaceShape" -addControl "inputSurfaceShape";
                editorTemplate -endLayout;
            editorTemplate -endLayout;
            AEgeometryFilterCommon $nodeName;
            AEgeometryFilterInclude $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "weightList";
    };
    ''')


def fromSelection(nodes=None):
    nodes = nodes or mc.ls(sl=True)
    if not nodes:
        return
    nodes = [mc.listRelatives(n, type='shape')[0] if mc.ls(n, type='transform') else n for n in nodes]
    driven = nodes.pop()
    deformer = mc.deformer(driven, type='prClosestPoint')[0]
    
    for driver in nodes:
        print driver
        driverType = mc.ls(driver, showType=True)[1]
        if driverType == 'mesh':
            mc.connectAttr('{}.worldMesh'.format(driver), '{}.inputMesh.inputMeshShape'.format(deformer))
            # mc.connectAttr('{}.worldMatrix'.format(driver), '{}.inputMesh.inputMeshWorldMatrix'.format(deformer))
        elif driverType == 'nurbsCurve':
            mc.connectAttr('{}.worldSpace'.format(driver), '{}.inputCurveShape'.format(deformer))
        elif driverType == 'nurbsSurface':
            mc.connectAttr('{}.worldSpace'.format(driver), '{}.inputSurfaceShape'.format(deformer))
        else:
            raise ValueError('Invalid nodeType : {0} : {1}'.format(driverType, driver))


def test():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(prClosestPoint.nodeTypeName)
    mc.loadPlugin(r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\{}.py'.format(prClosestPoint.nodeTypeName))
    mc.file(r'C:\Users\paz\Documents\git\prmaya\test\plugins\prClosestPoint_scene_v001.ma', open=True)
    mc.select(['driverMesh', 'driverCurve', 'driverSurface', 'driven'])
    fromSelection()
    mc.select('driven')

