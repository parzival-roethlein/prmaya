"""
DESCRIPTION
Deformer that moves points to closest: position / mesh shape or mesh vertex / nurbs-curve shape / nurbs-surface shape.

USE CASES
- Modeling: Interactively snap vertices between meshes (inputTargetMeshClosestVertex attribute)
- Modeling/Rigging: Interactively match shapes of different geometries
- Rigging/Animation: Sticky lips deformation

USAGE
- Like any other deformer (MEL):
deformer -type "prClosestPoint"
- Helper function. Select all drivers then driven and execute (Python):
import prClosestPoint;prClosestPoint.fromSelection()
- Improve performance by either removing unaffected vertices with the Edit membership tools or painting their weights attribute value to 0.0

ATTRIBUTES
- maxDistanceEnabled : bool : on/off
- maxDistance : distance (double) (min 0.0) : Only deltas shorter than maxDistance are considered. Value of 0.0 will disable maxDistance and falloff
- maxDistanceWeights : float (min 0.0, max 1.0) : Paintable per vertex maxDistance
- maxDistanceUScaleEnabled : bool : on/off
- maxDistanceUScale : ramp : Scale maxDistance depending on U value of closest point on input target (Ramp maps U value from 0.0 to 1.0)
- maxDistanceVScaleEnabled : bool : on/off
- maxDistanceVScale : ramp : Scale maxDistance depending on V value of closest point on input target (Ramp maps V value from 0.0 to 1.0)
- falloffEnabled : bool : on/off
- falloff : ramp : Scale deltas within maxDistance
- inputPositionEnabled : bool : on/off
- inputPosition : compound / distance3 (double3), array : expects worldSpace position (inputPositionX, inputPositionY, inputPositionZ)
- inputTargetEnabled : bool : on/off
- inputTarget : compound, array :
- inputTargetShapeEnabled : bool : on/off
- inputTargetShape : mesh/nurbs-curve/nurbs-surface : myMeshNode.worldMesh, myCurveNode.worldSpace, mySurfaceNode.worldSpace
- inputTargetMeshClosestVertex : float (min 0.0, max 1.0) : blend target position from closest point to closest vertex
inherited:
- envelope: Scale all deltas
- weights: Paintable per vertex envelope

LINKS
- Demo:
TODO
- Making-of:
https://pazrot3d.blogspot.com/2018/10/prclosestpointpy-making-of.html
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- can maxDistanceWeight be a child of weightList?
- weightMap and inputPositions should show up in node editor
- caching, frozen, nodeState should not show up twice in connection editor
- input shape closest point texture value based maxDistance?
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
        numericAttr = om.MFnNumericAttribute()
        rampAttr = om.MRampAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        unitAttr = om.MFnUnitAttribute()
        genericAttr = om.MFnGenericAttribute()
        
        # maxDistance
        prClosestPoint.maxDistanceEnabled = numericAttr.create('maxDistanceEnabled', 'maxDistanceEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.maxDistanceEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistanceEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.maxDistance = unitAttr.create('maxDistance', 'maxDistance', om.MFnUnitAttribute.kDistance, 1.0)
        unitAttr.setKeyable(True)
        unitAttr.setMin(0.0)
        prClosestPoint.addAttribute(prClosestPoint.maxDistance)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistance, prClosestPoint.outputGeometry)
        
        prClosestPoint.maxDistanceWeights = numericAttr.create('maxDistanceWeights', 'maxDistanceWeights', om.MFnNumericData.kFloat, 1.0)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        numericAttr.setArray(True)
        numericAttr.setUsesArrayDataBuilder(True)
        
        prClosestPoint.weightMaps = compoundAttr.create('weightMaps', 'weightMaps')
        compoundAttr.setArray(True)
        compoundAttr.setUsesArrayDataBuilder(True)
        compoundAttr.addChild(prClosestPoint.maxDistanceWeights)
        prClosestPoint.addAttribute(prClosestPoint.weightMaps)
        prClosestPoint.attributeAffects(prClosestPoint.maxDistanceWeights, prClosestPoint.outputGeometry)
        
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
        
        prClosestPoint.inputPositionX = unitAttr.create('inputPositionX', 'inputPositionX', om.MFnUnitAttribute.kDistance, 0.0)
        prClosestPoint.addAttribute(prClosestPoint.inputPositionX)
        prClosestPoint.attributeAffects(prClosestPoint.inputPositionX, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputPositionY = unitAttr.create('inputPositionY', 'inputPositionY', om.MFnUnitAttribute.kDistance, 0.0)
        prClosestPoint.addAttribute(prClosestPoint.inputPositionY)
        prClosestPoint.attributeAffects(prClosestPoint.inputPositionY, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputPositionZ = unitAttr.create('inputPositionZ', 'inputPositionZ', om.MFnUnitAttribute.kDistance, 0.0)
        prClosestPoint.addAttribute(prClosestPoint.inputPositionZ)
        prClosestPoint.attributeAffects(prClosestPoint.inputPositionZ, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputPosition = compoundAttr.create('inputPosition', 'inputPosition')
        compoundAttr.addChild(prClosestPoint.inputPositionX)
        compoundAttr.addChild(prClosestPoint.inputPositionY)
        compoundAttr.addChild(prClosestPoint.inputPositionZ)
        compoundAttr.setArray(True)
        prClosestPoint.addAttribute(prClosestPoint.inputPosition)
        prClosestPoint.attributeAffects(prClosestPoint.inputPosition, prClosestPoint.outputGeometry)
        
        # inputTarget
        prClosestPoint.inputTargetEnabled = numericAttr.create('inputTargetEnabled', 'inputTargetEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        prClosestPoint.addAttribute(prClosestPoint.inputTargetEnabled)
        prClosestPoint.attributeAffects(prClosestPoint.inputTargetEnabled, prClosestPoint.outputGeometry)
        
        prClosestPoint.inputTargetMeshClosestVertex = numericAttr.create('inputTargetMeshClosestVertex', 'inputTargetMeshClosestVertex', om.MFnNumericData.kFloat, 0.0)
        numericAttr.setKeyable(True)
        numericAttr.setMin(0.0)
        numericAttr.setMax(1.0)
        
        prClosestPoint.inputTargetShapeEnabled = numericAttr.create('inputTargetShapeEnabled', 'inputTargetShapeEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.setKeyable(True)
        
        prClosestPoint.inputTargetShape = genericAttr.create("inputTargetShape", "inputTargetShape")
        # genericAttr.setReadable(False)
        genericAttr.addDataAccept(om.MFnNurbsCurveData.kNurbsCurve)
        genericAttr.addDataAccept(om.MFnNurbsSurfaceData.kNurbsSurface)
        genericAttr.addDataAccept(om.MFnMeshData.kMesh)
        
        prClosestPoint.inputTarget = compoundAttr.create('inputTarget', 'inputTarget')
        compoundAttr.addChild(prClosestPoint.inputTargetShapeEnabled)
        compoundAttr.addChild(prClosestPoint.inputTargetMeshClosestVertex)
        compoundAttr.addChild(prClosestPoint.inputTargetShape)
        compoundAttr.setArray(True)
        prClosestPoint.addAttribute(prClosestPoint.inputTarget)
        prClosestPoint.attributeAffects(prClosestPoint.inputTargetShapeEnabled, prClosestPoint.outputGeometry)
        prClosestPoint.attributeAffects(prClosestPoint.inputTargetMeshClosestVertex, prClosestPoint.outputGeometry)
        prClosestPoint.attributeAffects(prClosestPoint.inputTargetShape, prClosestPoint.outputGeometry)
        
        # paintable
        mc.makePaintable('prClosestPoint', 'weights', attrType='multiFloat', shapeMode='deformer')
        mc.makePaintable('prClosestPoint', 'maxDistanceWeights', attrType='multiFloat', shapeMode='deformer')
    
    @staticmethod
    def creator():
        return prClosestPoint()
    
    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
        self.__membership__ = defaultdict(list)
        self.__weights__ = {}
        self.__weightsDirty__ = defaultdict(lambda: True)
        self.__maxDistanceWeights__ = {}
        self.__maxDistanceWeightsDirty__ = defaultdict(lambda: True)

    def setDependentsDirty(self, plug, plugArray):
        if plug == self.weights:
            self.__weightsDirty__[plug.parent().logicalIndex()] = True
        elif plug == self.maxDistanceWeights:
            self.__maxDistanceWeightsDirty__[plug.parent().logicalIndex()] = True
    
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
        - documentation is wrong: "This method is not called for ramp attributes since they should always be written." (shouldSave)
        - the only devkit python example in pyApiMeshShape.py is misleading: return values True, False, None all seem to force save
        """
        if plug == self.falloff or plug == self.maxDistanceUScale or plug == self.maxDistanceVScale:
            return True
        return OpenMayaMPx.MPxNode.shouldSave(self, plug, result)
    
    def deform(self, block, iterator, localToWorldMatrix, multiIndex):
        thisNode = self.thisMObject()
        envelope = block.inputValue(self.envelope).asFloat()
        if envelope == 0.0:
            return
        
        if not block.inputValue(self.maxDistanceEnabled).asBool():
            maxDistance = 0.0
        else:
            maxDistance = block.inputValue(self.maxDistance).asDistance().value()
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
        inputTargetEnabled = block.inputValue(self.inputTargetEnabled).asBool()
        if not positionEnabled and not inputTargetEnabled:
            return
        if inputTargetEnabled:
            intUtil = om.MScriptUtil()
            intUtil.createFromInt(0)
            intPtr = intUtil.asIntPtr()
            doublePtrUtil = om.MScriptUtil()
            doublePtrUtil.createFromDouble(0.0)
            doublePtr = doublePtrUtil.asDoublePtr()
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
        
        if self.__maxDistanceWeightsDirty__[multiIndex]:
            weightMapsArrayHandle = block.inputArrayValue(self.weightMaps)
            JumpToElement(weightMapsArrayHandle, multiIndex)
            weightMapsHandle = weightMapsArrayHandle.inputValue()
            maxDistanceWeightsArrayHandle = om.MArrayDataHandle(weightMapsHandle.child(self.maxDistanceWeights))
            self.__maxDistanceWeights__[multiIndex] = []
            for index in self.__membership__[multiIndex]:
                JumpToElement(maxDistanceWeightsArrayHandle, index)
                self.__maxDistanceWeights__[multiIndex].append(maxDistanceWeightsArrayHandle.inputValue().asFloat())
            self.__maxDistanceWeightsDirty__[multiIndex] = False
        maxDistanceWeights = self.__maxDistanceWeights__[multiIndex]
        
        pointsWorldSpace = []
        while not iterator.isDone():
            pointsWorldSpace.append(iterator.position() * localToWorldMatrix)
            iterator.next()
        
        deltas = {}
        
        if positionEnabled:
            inputPositionsArrayHandle = block.inputArrayValue(self.inputPosition)
            for i in range(inputPositionsArrayHandle.elementCount()):
                inputPositionsArrayHandle.jumpToArrayElement(i)
                inputPositionsHandle = inputPositionsArrayHandle.inputValue()
                positionX = inputPositionsHandle.child(self.inputPositionX).asDistance().value()
                positionY = inputPositionsHandle.child(self.inputPositionY).asDistance().value()
                positionZ = inputPositionsHandle.child(self.inputPositionZ).asDistance().value()
                position = om.MPoint(positionX, positionY, positionZ)
                for index, weight, point in izip(indices, weights, pointsWorldSpace):
                    if not weight:
                        continue
                    delta = position - point
                    if index in deltas and deltas[index].length() < delta.length():
                        continue
                    deltas[index] = delta
        
        if inputTargetEnabled:
            inputTargetArrayHandle = block.inputArrayValue(self.inputTarget)
            for i in range(inputTargetArrayHandle.elementCount()):
                inputTargetArrayHandle.jumpToArrayElement(i)
                inputTargetHandle = inputTargetArrayHandle.inputValue()
                if not inputTargetHandle.child(self.inputTargetShapeEnabled).asBool():
                    continue
                targetShapeHandle = inputTargetHandle.child(self.inputTargetShape)
                shapeData = targetShapeHandle.data()
                if shapeData.isNull():
                    continue
                shapeType = targetShapeHandle.type()
                targetPoint = om.MPoint()
                
                if shapeType == om.MFnMeshData.kMesh:
                    shapeFn = om.MFnMesh(shapeData)
                    closestVertex = inputTargetHandle.child(self.inputTargetMeshClosestVertex).asFloat()
                    if closestVertex:
                        tempPoint = om.MPoint()
                        faceVertices = om.MIntArray()
                    
                    def getClosestPoint(startPoint):
                        shapeFn.getClosestPoint(startPoint, targetPoint, om.MSpace.kWorld, intPtr)
                        if closestVertex:
                            shapeFn.getPolygonVertices(om.MScriptUtil(intPtr).asInt(), faceVertices)
                            shortestDistance = None
                            for vertexId in faceVertices:
                                shapeFn.getPoint(vertexId, tempPoint, om.MSpace.kWorld)
                                vertexDistance = (startPoint - tempPoint).length()
                                if shortestDistance is None or vertexDistance < shortestDistance:
                                    shortestDistance = vertexDistance
                                    closestVertexPoint = om.MPoint(tempPoint)
                            return targetPoint * (1.0 - closestVertex) + om.MVector(closestVertexPoint * closestVertex)
                        return targetPoint
                    
                    def setMaxDistanceUvScaleValues(uvPoint):
                        if maxDistanceUScaleEnabled or maxDistanceVScaleEnabled:
                            shapeFn.getUVAtPoint(uvPoint, float2Ptr, om.MSpace.kWorld)
                            if maxDistanceUScaleEnabled:
                                uValues[index] = float2PtrUtil.getFloat2ArrayItem(float2Ptr, 0, 0)
                            if maxDistanceVScaleEnabled:
                                vValues[index] = float2PtrUtil.getFloat2ArrayItem(float2Ptr, 0, 1)
                    
                elif shapeType == om.MFnNurbsCurveData.kNurbsCurve:
                    shapeFn = om.MFnNurbsCurve(shapeData)
                    
                    def getClosestPoint(startPoint):
                        return shapeFn.closestPoint(startPoint, doublePtr, 0.00001, om.MSpace.kWorld)
                    
                    def setMaxDistanceUvScaleValues(*args):
                        if maxDistanceUScaleEnabled:
                            uValues[index] = om.MScriptUtil.getDouble(doublePtr) / shapeFn.numSpans()
                        if maxDistanceVScaleEnabled and index in vValues:
                            del vValues[index]
                
                elif shapeType == om.MFnNurbsSurfaceData.kNurbsSurface:
                    shapeFn = om.MFnNurbsSurface(shapeData)
                    
                    def getClosestPoint(startPoint):
                        return shapeFn.closestPoint(startPoint, doublePtr, doublePtr2, False, 0.00001, om.MSpace.kWorld)
                    
                    def setMaxDistanceUvScaleValues(*args):
                        if maxDistanceUScaleEnabled:
                            uValues[index] = om.MScriptUtil.getDouble(doublePtr) / shapeFn.numSpansInU()
                        if maxDistanceVScaleEnabled:
                            vValues[index] = om.MScriptUtil.getDouble(doublePtr2) / shapeFn.numSpansInV()
                    
                else:
                    raise ValueError('can never happen?')
                
                for index, weight, point in izip(indices, weights, pointsWorldSpace):
                    if not weight:
                        continue
                    targetPoint = getClosestPoint(point)
                    delta = targetPoint - point
                    if index in deltas and deltas[index].length() < delta.length():
                        continue
                    deltas[index] = targetPoint - point
                    setMaxDistanceUvScaleValues(targetPoint)
        
        # maxDistance / falloff
        for vertexId, delta in deltas.iteritems():
            listIndex = indices.index(vertexId)
            if maxDistance:
                deltaLength = delta.length()
                vertexMaxDistance = maxDistance * maxDistanceWeights[listIndex]
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
            
            pointsWorldSpace[listIndex] += delta * weights[listIndex] * envelope
        
        pointsObjectSpace = om.MPointArray()
        worldToLocalMatrix = localToWorldMatrix.inverse()
        for point in pointsWorldSpace:
            pointsObjectSpace.append(point * worldToLocalMatrix)
        iterator.setAllPositions(pointsObjectSpace)
        

def initializePlugin(obj):
    pluginFn = OpenMayaMPx.MFnPlugin(obj, 'Parzival Roethlein', '0.0.3')
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
                    editorTemplate -label "maxDistanceEnabled" -addControl "maxDistanceEnabled";
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
                editorTemplate -beginLayout "inputTarget Attributes" -collapse 1;
                    editorTemplate -label "inputTargetEnabled" -addControl "inputTargetEnabled";
                    editorTemplate -label "inputTarget" -addControl "inputTarget";
                editorTemplate -endLayout;
            editorTemplate -endLayout;
            AEgeometryFilterCommon $nodeName;
            AEgeometryFilterInclude $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "weightList";
        editorTemplate -suppress "weightMaps";
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
        outputAttr = '{0}.{1}'.format(driver, {'mesh': 'worldMesh', 'nurbsCurve': 'worldSpace', 'nurbsSurface': 'worldSpace'}[driverType])
        inputParentAttr = '{0}.inputTarget'.format(deformer)
        inputAttr = '{0}[{1}].inputTargetShape'.format(inputParentAttr, mc.getAttr(inputParentAttr, size=True))
        mc.connectAttr(outputAttr, inputAttr)


def JumpToElement(arrayHandle, index):
    try:
        arrayHandle.jumpToElement(index)
    except RuntimeError:
        builder = arrayHandle.builder()
        builder.addElement(index)
        arrayHandle.set(builder)
        arrayHandle.jumpToElement(index)
