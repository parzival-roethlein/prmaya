"""
DESCRIPTION
Deformer that moves points to closest: position / mesh shape or vertex / curve shape / nurbs-surface shape.

USE CASES
- Modeling: Interactively snap vertices between meshes (inputMeshClosestVertex attribute)
- Modeling/Rigging: Interactively match shapes of different geometries
- Rigging/Animation: Sticky lips deformation

USAGE
- Like any other deformer (MEL):
deformer -type "prClosestPoint"
- Helper function. Select all drivers then driven and execute (Python):
import prClosestPoint;prClosestPoint.fromSelection()
- Improve performance by either removing unaffected vertices with the Edit membership tools or painting their weights attribute value to 0.0

ATTRIBUTES
setup:
- inputPosition : float3, array : expects worldSpace position (inputPositionX, inputPositionY, inputPositionZ)
- inputMeshShape : mesh, array : expects myMeshNode.worldMesh
- inputCurveShape : curve, array : expects myCurveNode.worldSpace
- inputSurfaceShape: surface, array : expects mySurfaceNode.worldSpace
control:
- maxDistance : float (min 0.0) : Only deltas shorter than maxDistance are affected. Value of 0.0 will disable maxDistance and falloff
- falloff : ramp : Scale deltas within maxDistance
- maxDistanceUScale : ramp : Scale maxDistance depending on U value of closest point on input target (Ramp maps U value from 0.0 to 1.0)
- maxDistanceVScale : ramp : Scale maxDistance depending on V value of closest point on input target (Ramp maps V value from 0.0 to 1.0)
- inputMeshClosestVertex : float (min 0.0, max 1.0) : blend deltas from closest point to closest vertex
switches:
- inputPositionEnabled : bool : on/off
- inputMeshEnabled : bool : on/off
- inputCurveEnabled : bool : on/off
- inputSurfaceEnabled : bool : on/off
- falloffEnabled : bool : on/off
- maxDistanceUScaleEnabled : bool : on/off
- maxDistanceVScaleEnabled : bool : on/off
inherited:
- envelope: Scale all deltas
- weights: Paintable per vertex envelope

LINKS
- Demo:
TODO
- Making-off:
https://pazrot3d.blogspot.com/2018/10/prclosestpointpy-making-of.html
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- should maxDistance be a maya unit attribute?
- now after removing matrix input for mesh shapes, maybe switch back to a single inputShape array attribute and each shape has its own on/off switch, closestVertex global or per shape?
- creation script should work with vertex selection
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
        rampAttr = om.MRampAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        
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
        
        prClosestPoint.inputMeshClosestVertex = numericAttr.create('inputMeshClosestVertex', 'inputMeshClosestVertex', om.MFnNumericData.kFloat, 0.0)
        numericAttr.setKeyable(True)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        prClosestPoint.addAttribute(prClosestPoint.inputMeshClosestVertex)
        prClosestPoint.attributeAffects(prClosestPoint.inputMeshClosestVertex, prClosestPoint.outputGeometry)

        prClosestPoint.inputMeshShape = typedAttr.create('inputMeshShape', 'inputMeshShape', om.MFnMeshData.kMesh)
        typedAttr.setArray(True)
        prClosestPoint.addAttribute(prClosestPoint.inputMeshShape)
        prClosestPoint.attributeAffects(prClosestPoint.inputMeshShape, prClosestPoint.outputGeometry)
        
        # inputCurve
        prClosestPoint.inputCurveEnabled = numericAttr.create('inputCurveEnabled', 'inputCurveEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.inputCurveEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.inputCurveEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputCurveShape = typedAttr.create('inputCurveShape', 'inputCurveShape', om.MFnNurbsCurveData.kNurbsCurve)
        typedAttr.setArray(True)
        prClosestPoint.addAttribute(prClosestPoint.inputCurveShape)
        prClosestPoint.attributeAffects(prClosestPoint.inputCurveShape, prClosestPoint.outputGeometry)
        
        # inputSurface
        prClosestPoint.inputSurfaceEnabled = numericAttr.create('inputSurfaceEnabled', 'inputSurfaceEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.inputSurfaceEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.inputSurfaceEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputSurfaceShape = typedAttr.create('inputSurfaceShape', 'inputSurfaceShape', om.MFnNurbsSurfaceData.kNurbsSurface)
        typedAttr.setArray(True)
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
    
    def shouldSave(self, plug, result):
        """
        implemented because of bug(?) if lower index of two ramp elements is (0, 0, linear) it will not get saved. debug:
        - does not happen with maya node remapValue
        - documentation is wrong: This method (shouldSave) is not called for ramp attributes since they should always be written.
        - the only devkit python example in pyApiMeshShape.py is misleading: return True, False, None does not make a difference
        """
        if plug == self.falloff or plug == self.maxDistanceUScale or plug == self.maxDistanceVScale:
            return True
        return OpenMayaMPx.MPxNode.shouldSave(self, plug, result)
    
    def deform(self, block, iterator, localToWorldMatrix, multiIndex):
        thisNode = self.thisMObject()
        envelope = block.inputValue(self.envelope).asFloat()
        if envelope == 0.0:
            return
        
        maxDistance = block.inputValue(self.maxDistance).asFloat()
        maxDistanceUScaleEnabled = block.inputValue(self.maxDistanceUScaleEnabled).asBool()
        maxDistanceVScaleEnabled = block.inputValue(self.maxDistanceVScaleEnabled).asBool()
        if maxDistanceUScaleEnabled or maxDistanceVScaleEnabled:
            float2PtrUtil = om.MScriptUtil()
            float2PtrUtil.createFromList([0.0, 0.0], 2)
            float2Ptr = float2PtrUtil.asFloat2Ptr()
        if maxDistanceUScaleEnabled:
            maxDistanceUScaleAttr = om.MRampAttribute(thisNode, self.maxDistanceUScale)
            uValues = {}
        if maxDistanceVScaleEnabled:
            maxDistanceVScaleAttr = om.MRampAttribute(thisNode, self.maxDistanceVScale)
            vValues = {}
        
        positionEnabled = block.inputValue(self.inputPositionEnabled).asBool()
        meshEnabled = block.inputValue(self.inputMeshEnabled).asBool()
        curveEnabled = block.inputValue(self.inputCurveEnabled).asBool()
        surfaceEnabled = block.inputValue(self.inputSurfaceEnabled).asBool()
        if not positionEnabled and not meshEnabled and not curveEnabled and not surfaceEnabled:
            return
        if meshEnabled:
            intUtil = om.MScriptUtil()
            intUtil.createFromInt(0)
            intPtr = intUtil.asIntPtr()
        if curveEnabled or surfaceEnabled:
            doublePtrUtil = om.MScriptUtil()
            doublePtrUtil.createFromDouble(0.0)
            doublePtr = doublePtrUtil.asDoublePtr()
        if surfaceEnabled:
            doublePtrUtil2 = om.MScriptUtil()
            doublePtrUtil2.createFromDouble(0.0)
            doublePtr2 = doublePtrUtil2.asDoublePtr()
        
        falloffEnabled = block.inputValue(self.falloffEnabled).asBool()
        if falloffEnabled:
            falloffRampAttr = om.MRampAttribute(thisNode, self.falloff)
        if falloffEnabled or maxDistanceUScaleEnabled or maxDistanceVScaleEnabled:
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
            for i in range(inputPositionsHandle.elementCount()):
                inputPositionsHandle.jumpToArrayElement(i)
                position = om.MPoint(*inputPositionsHandle.inputValue().asFloat3())
                for index, weight, point in izip(indices, weights, pointsWorldSpace):
                    if not weight:
                        continue
                    delta = position - point
                    if index in deltas and deltas[index].length() < delta.length():
                        continue
                    deltas[index] = delta
        
        if meshEnabled:
            meshArrayHandle = block.inputArrayValue(self.inputMeshShape)
            closestVertex = block.inputValue(self.inputMeshClosestVertex).asFloat()
            for i in range(meshArrayHandle.elementCount()):
                meshArrayHandle.jumpToArrayElement(i)
                meshHandle = meshArrayHandle.inputValue()
                meshData = meshHandle.data()
                if not meshData.isNull():
                    meshFn = om.MFnMesh(meshData)
                    if closestVertex:
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
                                uValues[index] = float2PtrUtil.getFloat2ArrayItem(float2Ptr, 0, 0)
                            if maxDistanceVScaleEnabled:
                                vValues[index] = float2PtrUtil.getFloat2ArrayItem(float2Ptr, 0, 1)
        
        if curveEnabled:
            curveArrayHandle = block.inputArrayValue(self.inputCurveShape)
            for i in range(curveArrayHandle.elementCount()):
                curveArrayHandle.jumpToArrayElement(i)
                curveShapeData = curveArrayHandle.inputValue().data()
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
            surfaceArrayHandle = block.inputArrayValue(self.inputSurfaceShape)
            for i in range(surfaceArrayHandle.elementCount()):
                surfaceArrayHandle.jumpToArrayElement(i)
                surfaceShapeData = surfaceArrayHandle.inputValue().data()
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
                            uValues[index] = om.MScriptUtil.getDouble(doublePtr) / surfaceShapeFn.numSpansInU()
                        if maxDistanceVScaleEnabled:
                            vValues[index] = om.MScriptUtil.getDouble(doublePtr2) / surfaceShapeFn.numSpansInV()
        
        # maxDistance / falloff
        for vertexId, delta in deltas.iteritems():
            if maxDistance:
                deltaLength = delta.length()
                vertexMaxDistance = maxDistance
                if maxDistanceUScaleEnabled and vertexId in uValues:
                    maxDistanceUScaleAttr.getValueAtPosition(uValues[vertexId], floatPtr)
                    vertexMaxDistance *= om.MScriptUtil.getFloat(floatPtr)
                if maxDistanceVScaleEnabled and vertexId in vValues:
                    maxDistanceVScaleAttr.getValueAtPosition(vValues[vertexId], floatPtr)
                    vertexMaxDistance *= om.MScriptUtil.getFloat(floatPtr)
                if deltaLength > vertexMaxDistance:
                    continue
                if falloffEnabled:
                    lengthMaxDistancePercent = deltaLength / vertexMaxDistance
                    falloffRampAttr.getValueAtPosition(float(1.0 - lengthMaxDistancePercent), floatPtr)
                    falloff = om.MScriptUtil.getFloat(floatPtr)
                    delta *= falloff
            listIndex = indices.index(vertexId)
            pointsWorldSpace[listIndex] += delta * weights[listIndex] * envelope
        
        pointsObjectSpace = om.MPointArray()
        worldToLocalMatrix = localToWorldMatrix.inverse()
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
    global proc AEprClosestPointTemplate(string $nodeName)
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
                    editorTemplate -label "inputMeshClosestVertex" -addControl "inputMeshClosestVertex";
                    editorTemplate -label "inputMeshShape" -addControl "inputMeshShape";
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
    """
    :param nodes: [driver1, ... driverN, driven]
    :return:
    """
    nodes = nodes or mc.ls(sl=True)
    if not nodes:
        return
    nodes = [mc.listRelatives(n, type='shape')[0] if mc.ls(n, type='transform') else n for n in nodes]
    driven = nodes.pop()
    deformer = mc.deformer(driven, type=prClosestPoint.nodeTypeName)[0]
    
    for driver in nodes:
        driverType = mc.ls(driver, showType=True)[1]
        if driverType == 'mesh':
            attr = '{}.inputMeshShape'.format(deformer)
            mc.connectAttr('{}.worldMesh'.format(driver), '{0}[{1}]'.format(attr, mc.getAttr(attr, size=True)))
        elif driverType == 'nurbsCurve':
            attr = '{}.inputCurveShape'.format(deformer)
            mc.connectAttr('{}.worldSpace'.format(driver), '{0}[{1}]'.format(attr, mc.getAttr(attr, size=True)))
        elif driverType == 'nurbsSurface':
            attr = '{}.inputSurfaceShape'.format(deformer)
            mc.connectAttr('{}.worldSpace'.format(driver), '{0}[{1}]'.format(attr, mc.getAttr(attr, size=True)))
        else:
            raise ValueError('Invalid nodeType : {0} : {1}'.format(driverType, driver))

