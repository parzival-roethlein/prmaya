"""
D E S C R I P T I O N:
This is an open source Maya plug-in (deformer) written in Python.
It is based on an Eurographics paper written by Dmitriy Pinskiy:
"Sliding Deformation: Shape Preserving Per-Vertex Displacement"
It can be used to create user-controlled local skin sliding for example.
In addition there is a simple closest-point algorithm, which is faster, 
but does not deform as well.

L I N K S:
- Demo video with link to latest version
.........
- Background information on my blog
.........
- If you found the script useful for rigging or coding, consider a small donation
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

U S A G E:
- First load the plug-in via Window->Settings->Prefs->Plug-in Manager
  Then you should be able to normally apply the deformer:
  (With a polygon mesh selected) execute (MEL): deformer -type "prSlideNode"

V E R S I O N S:
2012-02-xx / 0.9.1: new attributes, new handle setup, error fixes, paper algorithm WIP
2011-08-21 / 0.9.0: closestPoint algorithm done

T O D O:
- initialize paintable falloff with 1.0 (in viewport displayed with 0.0 on first call)
- normalCurve distance
-- paper: approximating shortest paths on weighted polyhedral surfaces
-- paper: exact geodesics and shortest paths on polyhedral surfaces
- 2D coordinate psi:
-- addPoint (translate to 2D)
-- pointInPoly (support non-convex polys, maybe will fix error when displace on edge)
-- projectDisplaceVector: use method from paper? (rotate handle displace)

- (maybe) store Psis, to improve performance? (slide should happen before skincluster/blendshapes then)
- (if stored) extra input mesh for psi (bindpose) so each psi does not have to be recalculated
-- but: maybe bad results? if in combination with other deformers, it maybe should always
-- recalculate? -> user should have option for either

- (maybe) when projecting handleVector on each vector, create plane with handleNormal+handleVector, and adjust each vector with plane, so direction does not change?
- rayintersection algorithm as option (to prevent bad sliding on sphere like area)

- (because of idea to create jiggle deformer, that would need slide as well)
-- extra input for target mesh, that way (if i have a mesh with jiggle deformer) 
-- the inputMesh of jiggle deformer can be used in slide node as target 
-- and output of jiggle node as slide target (loop through all vertices, if distance
-- between jiggle input/output vertex is greater 0.0000x slide the vertex)
-- maybe works for toms idea as well? (deform mesh, smooth mesh -> slide all)

A T T R I B U T E S:
input user:
- position (int): vertex number, start position of handle
- algorithm (enum): which algorithm will be used for deformation
- aHandleVisibility (float): show/hide handles of deformer
- falloff type (enum): either use radius around position or painted weight map
- falloffWeights (double, paintable): weight map to be painted by user for falloff
- radius (float): influence radius around position
- radiusFalloff (ramp): influence fall-off inside of radius
input internal:
- displace (3double): handle locator world position
- nullParentInverse (matrix): parentInverseMatrix off null-group
output:
- nullTranslate (3double): translate value for null-group 

T E S T:
def prTestSlide():
    import maya.cmds as mc
    import maya.mel as mm
    mc.file(new=True, f=True)
    mm.eval( 'setWireframeOnShadedOption true modelPanel4;' )
    mc.unloadPlugin( "prSlideNode.py" )
    mc.loadPlugin( "prSlideNode.py" )
    mc.polySphere()
    myNode = mc.deformer( type='prSlideNode' )[0]
    # setup
    mc.setAttr( myNode+".algorithm", 0 )
    mc.setAttr( myNode+".position", 200 )
prTestSlide()

"""

import sys
import maya.OpenMaya as om
import maya.OpenMayaMPx as OpenMayaMPx
import maya.mel as mm


class prSlideNode(OpenMayaMPx.MPxDeformerNode):
    pluginName = "prSlideNode"
    pluginId = om.MTypeId(0x0010A51B)
    
    # attributes
    #     input user
    aPosition = om.MObject()
    aFlipOpposingSide = om.MObject()
    aAlgorithm = om.MObject()
    aHandleVisibility = om.MObject()
    aFalloffType = om.MObject()
    aRadius = om.MObject()
    aRadiusFalloff = om.MObject()
    aFalloffWeights = om.MObject()
    aFalloffWeightList = om.MObject()
    #     input deformer
    aDisplace = om.MObject()
    aDisplaceX = om.MObject()
    aDisplaceY = om.MObject()
    aDisplaceZ = om.MObject()
    aNullParentInverse = om.MObject()
    #     output
    aNullTranslate = om.MObject()
    aNullTranslateX = om.MObject()
    aNullTranslateY = om.MObject()
    aNullTranslateZ = om.MObject()
    
    # code variable
    algorithmLastCall = None
    # algorithm variables
    plane = om.MPlane()
    vector = om.MVector()
    #     closest point algorithm
    intersector = om.MMeshIntersector()
    ptOM = om.MPointOnMesh()
    #     paper algorithm
    vertexEdges = None  # vertex id order: connected edges
    vertexFaces = None  # vertex id order: faces connected to vertex
    vertexNeighborVertices = None  # vertex id order: all vertices that build connected faces
    vertexFacesBorderEdges = None  # vertex id order: border edges of connected faces
    
    edgeVertices = None  # edge id order: vertices that build edge
    edgeFaces = None  # edge id order: connected faces
    
    faceVertices = None  # face id order: vertices that build face
    faceEdges = None  # face id order: edges that build face
    faceUs = None  # face id order: U values of vertices of face
    faceVs = None  # face id order: V values of vertices of face
    
    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
    
    # initialize ramp attribute
    # and
    # create deformer handles (hierarchy): 
    # - null (sphere): constrained to surface, with sphereShape to display radius
    #   - handle (locator): for slide, has annotation to show start position
    def accessoryNodeSetup(self, cmd):
        oThis = self.thisMObject()
        fnThis = om.MFnDependencyNode(oThis)
        nameThis = fnThis.name()
        
        # initialize radiusFalloff ramp
        hRadiusFalloff = om.MRampAttribute(oThis, self.aRadiusFalloff)
        
        a1 = om.MFloatArray()  # positions
        b1 = om.MFloatArray()  # values
        c1 = om.MIntArray()  # interpolations
        
        a1.append(float(0.0))
        a1.append(float(1.0))
        
        b1.append(float(1.0))
        b1.append(float(0.0))
        
        c1.append(om.MRampAttribute.kSmooth)
        c1.append(om.MRampAttribute.kSmooth)
        
        hRadiusFalloff.addEntries(a1, b1, c1)
        
        # create handles
        #     null-group to be constrained to surface 
        #         implicitSphere shape to show radius
        #         locatorShape (hidden) required for annotation
        oGroup = cmd.createNode('transform', om.MObject().kNullObj)
        oGroupSphere = cmd.createNode('implicitSphere', oGroup)
        oGroupLoc = cmd.createNode('locator', oGroup)
        #     locator controlling sliding direction and magnitude, to be translated by user
        #         annotationShape to show start position
        oLocator = cmd.createNode('locator')
        oLocatorAnno = cmd.createNode('annotationShape', oLocator)
        cmd.reparentNode(oLocator, oGroup)  # cmd.reparentNode to get extra transform
        #     create nodes
        cmd.doIt()
        # function sets and shape objects
        #     group
        fnGroup = om.MFnDagNode(oGroup)
        fnGroupSphere = om.MFnDagNode(oGroupSphere)
        fnGroupLoc = om.MFnDagNode(oGroupLoc)
        #     locator
        fnLocator = om.MFnDagNode(oLocator)
        oLocatorShape = fnLocator.child(0)
        fnLocatorShape = om.MFnDagNode(oLocatorShape)
        fnLocatorAnno = om.MFnDagNode(oLocatorAnno)
        # connections
        #     group
        #         aHandleVisibility >> oGroupSphere.v
        aGroupSphereV = fnGroupSphere.attribute('visibility')
        cmd.connect(oThis, self.aHandleVisibility, oGroupSphere, aGroupSphereV)
        #         group.inverseParentMatrix >> aNullParentInverse
        aGroupIPM = fnGroup.attribute('parentInverseMatrix')
        cmd.connect(oGroup, aGroupIPM, oThis, self.aNullParentInverse)
        #         aNullTranslate >> group.t
        aGroupT = fnGroup.attribute('translate')
        cmd.connect(oThis, self.aNullTranslate, oGroup, aGroupT)
        #         aRadius >> sphereShape.radius
        aGroupSphereR = fnGroupSphere.attribute('radius')
        cmd.connect(oThis, self.aRadius, oGroupSphere, aGroupSphereR)
        #         aFalloffType >> sphereShape.lodVisibility
        aGroupSphereLV = fnGroupSphere.attribute('lodVisibility')
        cmd.connect(oThis, self.aFalloffType, oGroupSphere, aGroupSphereLV)
        #         groupLoc >> locAnno 
        aGroupLocWM = fnGroupLoc.attribute('worldMatrix')
        aLocatorAnnoDOM = fnLocatorAnno.attribute('dagObjectMatrix')
        cmd.connect(oGroupLoc, aGroupLocWM, oLocatorAnno, aLocatorAnnoDOM)
        #     locator
        #         aHandleVisibility >> oLocatorShape.v
        aLocatorShapeV = fnLocatorShape.attribute('visibility')
        cmd.connect(oThis, self.aHandleVisibility, oLocatorShape, aLocatorShapeV)
        #         aHandleVisibility >> oLocatorAnno.v
        aLocatorAnnoV = fnLocatorAnno.attribute('visibility')
        cmd.connect(oThis, self.aHandleVisibility, oLocatorAnno, aLocatorAnnoV)
        #         locatorShape.worldPosition >> aDisplace
        aLocatorShapeWP = fnLocatorShape.attribute('worldPosition')
        cmd.connect(oLocatorShape, aLocatorShapeWP, oThis, self.aDisplace)
        #         aRadius >> locatorShape.localScaleXYZ
        for each in ['localScaleX', 'localScaleY', 'localScaleZ']:
            aLocatorShapeEach = fnLocatorShape.attribute(each)
            cmd.connect(oThis, self.aRadius, oLocatorShape, aLocatorShapeEach)
        # set attributes
        #     group
        #         template groupSphereShape
        cmd.commandToExecute('setAttr ' + fnGroupSphere.name() + '.overrideEnabled 1')
        cmd.commandToExecute('setAttr ' + fnGroupSphere.name() + '.overrideDisplayType 1')
        #         hide group locator (was just made for annotation)
        cmd.commandToExecute('setAttr ' + fnGroupLoc.name() + '.overrideEnabled 1')
        cmd.commandToExecute('setAttr ' + fnGroupLoc.name() + '.overrideVisibility 0')
        #     locator
        #         lock locator scale
        for each in ['.sx', '.sy', '.sz']:
            cmd.commandToExecute('setAttr ' + fnLocator.name() + each + ' -lock 1 -keyable 0 -channelBox 0')
        #         template locAnno
        cmd.commandToExecute('setAttr ' + fnLocatorAnno.name() + '.overrideEnabled 1')
        cmd.commandToExecute('setAttr ' + fnLocatorAnno.name() + '.overrideDisplayType 1')
        #         locatorShape.localPosition keyable
        for each in ['.localPositionX', '.localPositionY', '.localPositionZ']:
            cmd.commandToExecute('setAttr -k 1 ' + fnLocatorShape.name() + each)
        # rename nodes
        #     group
        cmd.renameNode(oGroup, nameThis + 'Null')
        cmd.renameNode(oGroupSphere, nameThis + 'NullShape')
        cmd.renameNode(oGroupLoc, nameThis + 'NullShape')
        #     locator
        cmd.renameNode(oLocator, nameThis + 'Handle')
        cmd.renameNode(oLocatorShape, nameThis + 'HandleShape')
        cmd.renameNode(oLocatorAnno, nameThis + 'HandleShape')
    
    def accessoryAttribute(self):
        return self.aNullParentInverse
    
    def deform(self, block, inputIter, matrix, multiIndex):
        thisNode = self.thisMObject()
        
        hEnvelope = block.inputValue(OpenMayaMPx.cvar.MPxDeformerNode_envelope)
        env = hEnvelope.asFloat()
        if env == 0.0:
            return
        
        hPosition = block.inputValue(self.aPosition)
        nPosition = hPosition.asInt()
        
        hFlip = block.inputValue(self.aFlipOpposingSide)
        bFlip = hFlip.asBool()
        
        hAlgorithm = block.inputValue(self.aAlgorithm)
        sAlgorithm = hAlgorithm.asShort()
        
        hInverse = block.inputValue(self.aNullParentInverse)
        mInverse = hInverse.asMatrix()
        
        # calculate translation constraint
        #   get mesh
        hInput = block.outputArrayValue(self.input)
        hInput.jumpToElement(multiIndex)
        hInputGeom = hInput.outputValue().child(self.inputGeom)
        oInputGeom = hInputGeom.asMesh()
        fnMesh = om.MFnMesh(oInputGeom)
        #   get world-space of position
        pPosition = om.MPoint()
        fnMesh.getPoint(nPosition, pPosition, om.MSpace.kWorld)
        #   adjust with inverse parent matrix
        nullPosition = pPosition * mInverse
        #   set constrain translate attribute
        hNullTranslate = block.outputValue(self.aNullTranslate)
        hNullTranslate.set3Double(nullPosition.x, nullPosition.y, nullPosition.z)
        #   displace (has to come after nullTranslate)
        hDisplace = block.inputValue(self.aDisplace)
        d3Displace = hDisplace.asDouble3()
        pDisplace = om.MPoint(d3Displace[0], d3Displace[1], d3Displace[2], 1.0)
        #   create displace vector
        fnMesh.getVertexNormal(nPosition, True, self.vector, om.MSpace.kWorld)
        vecDisplace = prProjectVectorOnPlane((pPosition - pDisplace), self.vector, self.plane)
        vecDisplaceLength = vecDisplace.length()
        if vecDisplaceLength == 0.0:
            return
        
        hFalloffType = block.inputValue(self.aFalloffType)
        sFalloffType = hFalloffType.asShort()
        
        ahFalloffWeightsList = block.inputArrayValue(self.aFalloffWeightList)
        arrayFalloffWeights = []
        if multiIndex < ahFalloffWeightsList.elementCount():
            ahFalloffWeightsList.jumpToArrayElement(multiIndex)
            # get array values
            hFalloffWeightsList = ahFalloffWeightsList.inputValue()
            hFalloffWeights = hFalloffWeightsList.child(self.aFalloffWeights)
            oFalloffWeights = hFalloffWeights.data()
            fnFalloffWeights = om.MFnDoubleArrayData(oFalloffWeights)
            arrayFalloffWeights = fnFalloffWeights.array()
            # adjust array size depending on vertex count (first call or user changed input geom)
            lenFalloffWeights = arrayFalloffWeights.length()
            vtxCount = fnMesh.numVertices()
            if lenFalloffWeights != vtxCount:
                if lenFalloffWeights < vtxCount:
                    # expand array, to match vertex count
                    fillValue = 1.0
                    if lenFalloffWeights:
                        fillValue = arrayFalloffWeights[-1]
                    for x in range(vtxCount - lenFalloffWeights):
                        arrayFalloffWeights.append(fillValue)
                elif lenFalloffWeights > vtxCount:
                    # reduce array size to match vertex count
                    arrayFalloffWeights.setLength(vtxCount)
                # extra query, just so the weights are displayed correctly in the viewport
                #  on first usage of paint tool. todo: better method?
                block.inputArrayValue(self.aFalloffWeightList)
        #     falloff radius
        hRadius = block.inputValue(self.aRadius)
        fRadius = hRadius.asFloat()
        #     aRadiusFalloff attribute
        f_util = om.MScriptUtil()
        fPtrRadiusFalloff = f_util.asFloatPtr()
        hRadiusFalloff = om.MRampAttribute(thisNode, self.aRadiusFalloff)
        # pre-loop variables and operations (to improve performance)
        matrixInverse = matrix.inverse()
        vecNormal = om.MVector()
        paAllPoints = om.MPointArray()
        # algorithm specific
        if sAlgorithm == 0:
            # mesh intersector: is faster than MFnMesh
            self.intersector.create(oInputGeom, matrix)
        elif sAlgorithm == 1:
            # code
            ptTarget = om.MPoint()
            f2_util = om.MScriptUtil()
            vec1 = om.MVector()
            vec2 = om.MVector()
            eachPlane = om.MPlane()
            # per vertex information (position, normal)
            #     maybe todo: to improve performance only use the indices from iter. the points that are 
            #                 used for param have to be included as well, so give good error msg for user 
            iterVertex = om.MItMeshVertex(oInputGeom)
            allPositions = []
            # allNormals = [] # removed, because it is required for both algorithms, and will be done per iter element anyways
            handlePlane = None
            while not iterVertex.isDone():
                # position
                allPositions.append(iterVertex.position(om.MSpace.kWorld))
                # normal
                # iterVertex.getNormal( vecNormal, om.MSpace.kWorld )
                # allNormals.append( om.MVector( vecNormal ) )
                # handle normal
                if iterVertex.index() == nPosition:
                    iterVertex.getNormal(vecNormal, om.MSpace.kWorld)  # remove if using allNormals
                    handlePlane = om.MPlane()
                    handlePlane.setPlane(vecNormal, 0.0)
                
                iterVertex.next()
            # error check handle normal
            if handlePlane is None:
                raise NameError(
                    'Did not create handlePlane, maybe invalid position attribute value (no vertex with id): ',
                    nPosition)
            # gather mesh data that can be saved over multiple deform calls
            if sAlgorithm != self.algorithmLastCall:
                # gather mesh data to be used for parameterization
                intArray = om.MIntArray()
                # #################
                # per edge data
                iterEdge = om.MItMeshEdge(oInputGeom)
                self.edgeVertices = []  # IDs of connected vertices [(0,1), (1,2),...]
                self.edgeFaces = []  # IDs of connected faces [(0,1), (1,2),...]
                while not iterEdge.isDone():
                    # vertices
                    self.edgeVertices.append([iterEdge.index(0), iterEdge.index(1)])
                    # faces
                    iterEdge.getConnectedFaces(intArray)
                    self.edgeFaces.append(om.MIntArray(intArray))
                    
                    iterEdge.next()
                # #################
                # per face data
                iterPoly = om.MItMeshPolygon(oInputGeom)
                self.faceVertices = []  # all vertices of a face
                self.faceEdges = []  # edges building face
                self.faceUs = []  # all U values of faceVertices
                self.faceVs = []  # all V values of faceVertices
                eachFaceU = om.MFloatArray()
                eachFaceV = om.MFloatArray()
                while not iterPoly.isDone():
                    # face vertices
                    iterPoly.getVertices(intArray)
                    self.faceVertices.append(om.MIntArray(intArray))
                    # face edges
                    iterPoly.getEdges(intArray)
                    self.faceEdges.append(om.MIntArray(intArray))
                    # faceVertex UVs
                    iterPoly.getUVs(eachFaceU, eachFaceV)
                    self.faceUs.append(om.MFloatArray(eachFaceU))
                    self.faceVs.append(om.MFloatArray(eachFaceV))
                    
                    iterPoly.next()
                # #################
                # per vertex data
                self.vertexEdges = []  # edges connected to vertex
                self.vertexFaces = []  # faces connected to vertex
                self.vertexNeighborVertices = []  # vertices on faces, which are connected to vertex
                self.vertexFacesBorderEdges = []  # initial border edges
                iterVertex.reset()
                while not iterVertex.isDone():
                    # edges
                    iterVertex.getConnectedEdges(intArray)
                    self.vertexEdges.append(om.MIntArray(intArray))
                    # faces
                    iterVertex.getConnectedFaces(intArray)
                    self.vertexFaces.append(om.MIntArray(intArray))
                    # vertex neighbors
                    tmpNeighbors = []
                    for eachFaceId in self.vertexFaces[-1]:
                        for eachPoint in self.faceVertices[eachFaceId]:
                            if eachPoint not in tmpNeighbors:
                                tmpNeighbors.append(eachPoint)
                    self.vertexNeighborVertices.append(tmpNeighbors)
                    # border edges
                    borderEdges = []
                    for eachFace in self.vertexFaces[-1]:
                        for eachEdge in self.faceEdges[eachFace]:
                            if borderEdges.count(eachEdge) == 0:
                                borderEdges.append(eachEdge)
                            else:
                                borderEdges.remove(eachEdge)
                    self.vertexFacesBorderEdges.append(borderEdges)
                    iterVertex.next()
        
        # main deform loop
        while not inputIter.isDone():
            iterIndex = inputIter.index()
            pt = inputIter.position()
            weight = self.weightValue(block, multiIndex, iterIndex)
            if weight == 0.0:
                paAllPoints.append(pt)
                inputIter.next()
                continue
            # set point to world space (all calculations in this plugin are in world-space ... i think?!)
            pt *= matrix
            # get falloff value
            #     weight map
            if sFalloffType == 0:
                if arrayFalloffWeights:
                    falloffValue = arrayFalloffWeights[iterIndex]
                else:
                    falloffValue = 1.0
            #     radius
            elif sFalloffType == 1:
                # get distance to pPosition to see if it is in radius
                distance = (pPosition - pt).length()
                #     skip if out of radius
                if distance > fRadius:
                    paAllPoints.append(inputIter.position())
                    inputIter.next()
                    continue
                # get fall-off value from ramp
                hRadiusFalloff.getValueAtPosition(distance / fRadius, fPtrRadiusFalloff)
                falloffValue = f_util.getFloat(fPtrRadiusFalloff)
            #     skip if fall-off value is zero (zero influence)
            if falloffValue == 0.0:
                paAllPoints.append(inputIter.position())
                inputIter.next()
                continue
            # adjust displace vector with fall-off
            vecDisplaceEach = vecDisplace * falloffValue
            # get normal
            fnMesh.getVertexNormal(iterIndex, True, vecNormal, om.MSpace.kWorld)
            # flip displace vector, if its angle is more than 90degree off and flipAttr is on
            if bFlip:
                if vecNormal * self.vector < 0:
                    vecDisplaceEach *= -1
            # -------------------------
            # closest point slide:
            # 1. project locator-movement (with falloffValue) on vertex-normal-plane
            # 2. then get closest point on mesh
            # -------------------------
            if sAlgorithm == 0:
                # project handle displacement on each point normal plane and adjust length with falloff
                # fnMesh.getVertexNormal( iterIndex, True, vecNormal, om.MSpace.kWorld )
                vecMove = prProjectVectorOnPlane(vecDisplaceEach, vecNormal, self.plane,
                                                 (vecDisplaceLength * falloffValue))
                # get closest point on mesh
                self.intersector.getClosestPoint((pt - vecMove), self.ptOM)
                ptClosest = om.MPoint(self.ptOM.getPoint())  # else it is MFloatPoint
                ptClosest *= matrix  # worldspace, so it is same space as pt
                vecMove = pt - ptClosest
                # adjust movement with envelope and painted weight
                vecMove *= env * weight
                pt = pt - vecMove
            # -------------------------
            # paper slide
            # -------------------------
            if sAlgorithm == 1:
                if True:  # iter.index() == 0):
                    #
                    # 1. create Psi / local parameterization plane
                    # self.plane.setPlane(allNormals[iterIndex], 0.0)# allNormals
                    self.plane.setPlane(vecNormal, 0.0)
                    # eachPsi = prPsi( iterIndex, pt, allNormals[iterIndex], self.plane ) # -14 fps ... not sure why, when working with functions and variables locally only, it was only 1.5 fps faster# allNormals
                    eachPsi = prPsi(iterIndex, pt, vecNormal, self.plane)
                    #
                    # 2. initial point mapping (handle-vertex and its neighbors)
                    eachPsi.addPoints(self.vertexNeighborVertices[iterIndex], allPositions)  # -37 fps
                    #
                    # 3. save initial faces and border edges
                    eachPsi.calculatePolygons(self.vertexFaces, self.faceVertices,
                                              self.vertexFaces[iterIndex])  # -0.7 fps
                    eachPsi.calculateBorderEdges(self.edgeVertices, self.faceEdges, self.vertexFaces[iterIndex],
                                                 self.vertexFacesBorderEdges[iterIndex])  # -0.2 fps
                    #
                    # 4. project displace vector on Psi (todo: only rotate vecDisplaceEach in psi 2d coordinates)
                    eachPsi.projectDisplaceVector(vecDisplaceEach, handlePlane)  # -0.9 fps
                    #
                    # 5. get target position faceId
                    faceId = eachPsi.pointInPolygon(vec1, vec2)  # -10 fps
                    # if displace point is out of range, expand Psi until displace is on a face
                    if faceId is None:
                        counter = 0  # limit to avoid crash - todo: maybe add attribute for user to set maximum?
                        newFaceId = None
                        while counter < 100 and faceId is None:
                            # get new face to map
                            newFaceId = eachPsi.getConnectedFace(self.edgeFaces)
                            # map new points
                            eachPsi.addPoints(self.faceVertices[newFaceId], allPositions)  # , fnMesh )
                            # save face and border edges
                            eachPsi.calculatePolygons(self.vertexFaces, self.faceVertices, [newFaceId])
                            eachPsi.calculateBorderEdges(self.edgeVertices, self.faceEdges, [newFaceId])
                            # try to get face id with new mapped face
                            faceId = eachPsi.pointInPolygon(vec1, vec2, [newFaceId])
                            #
                            counter += 1
                        # error check
                        if counter == 100:
                            raise NameError('counter limit reached for vertex: ', iterIndex)
                        if faceId is None:
                            raise NameError('faceId not found, for vertex: ', iterIndex)
                    #
                    # 6. get UV value [u,v] on Psi to get position on mesh
                    eachUV = eachPsi.getPositionUv(faceId, self.faceUs[faceId], self.faceVs[faceId])  # -1.2 fps
                    f2_util.createFromList(eachUV, 2)
                    f2_ptr = f2_util.asFloat2Ptr()
                    #
                    fnMesh.getPointAtUV(faceId, ptTarget, f2_ptr, om.MSpace.kWorld)
                    #
                    # sometimes error if ptDisplace is on edge, in that case just try all faces - todo: maybe find better solution??
                    # try:
                    #    fnMesh.getPointAtUV( faceId, ptTarget, f2_ptr, om.MSpace.kWorld )
                    # except:
                    #    for eachId in eachPsi.facePoints:
                    #        try:
                    #            fnMesh.getPointAtUV( eachId, ptTarget, f2_ptr, om.MSpace.kWorld )
                    #            break
                    #        except:
                    #            continue
                    #    else:
                    #        raise NameError( 'Could not find position on mesh for vertex (are connected polygons quads?): ', iterIndex )
                    #
                    # 7. displace vertex
                    vecMove = pt - ptTarget
                    # adjust with envelope and painted weight
                    vecMove *= env * weight
                    # adjust pt
                    pt = pt - vecMove
            # set point to object space again
            pt *= matrixInverse
            
            # position point
            paAllPoints.append(pt)
            
            inputIter.next()
        # while iter
        # set the new positions
        inputIter.setAllPositions(paAllPoints)
        # save algorithm used in this call for next call
        self.algorithmLastCall = sAlgorithm
        return


def prProjectVectorOnPlane(vec_arg, normal_arg, plane_arg, length_arg=None):
    # project vector on plane and optionally set to given length
    #  vec_arg: vector to be projected
    #  normal_arg: plane normal
    #  plane_arg: plane to project onto
    #  length_arg: length of projected vector
    plane_arg.setPlane(normal_arg, 0.0)
    dDistance = plane_arg.directedDistance(vec_arg)
    # get vector to plane
    ptOnPlane = (normal_arg * dDistance)
    vecProjected = vec_arg - ptOnPlane
    if length_arg:
        vecProjectedLength = vecProjected.length()
        if vecProjectedLength > 0.0:
            vecProjected *= length_arg / vecProjectedLength
    return vecProjected


class prPsi:
    """
    custom class for local parameterization "Psi" (a simplified 2D mesh)
    - save root position and plane on initialization (def __init__)
    - map new points (def addPoints)
    - save fully mapped polygons (def calculatePolygons)
    - save border edges (def calculateBorderEdges)
    - calculate local displacement representation (def projectDisplaceVector)
    - calculate UV value at displacement representation
    """
    # variables / psi information to save
    rootId = None
    root = None
    plane = None
    normal = None
    displace = None
    points = None  # all mapped points {vertexId:<MPoint...>, ...}
    facePoints = None  # all completely mapped faces {faceId:(vtx1, vtx2), ...}
    borderEdges = None  # all border edges {edgeId:(vtx1, vtx2), ...}
    
    # create plane
    def __init__(self, id_arg, pt_arg, normal_arg, plane_arg):
        # reset values (else they get used from last deform call / class instance is saved)
        self.rootId = None
        self.root = None
        self.plane = None
        self.normal = None
        self.displace = None
        self.points = {}
        self.facePoints = {}
        self.borderEdges = {}
        # initialize
        self.rootId = id_arg
        self.root = pt_arg
        self.plane = plane_arg
        self.normal = normal_arg
    
    def addPoints(self, pointIDsToAdd_arg, pointPositions_arg, mesh_arg=None):
        """
        Adds points with world position on Psi-plane
        - pointIDsToAdd_arg: [id1,id2,..]
        - pointPositions_arg: all point positions {1:MPoint(), 2:MPoint(),...}
        - mesh_arg: MFnMesh, if given use normalCurve distance, else just world space distance
        """
        for eachID in pointIDsToAdd_arg:
            # skip mapped points
            if eachID in self.points:
                continue
            vecNeighbor = pointPositions_arg[eachID] - self.root  # -8fps // 1079 times
            # distance between points
            if mesh_arg:
                dDistToNeighbor = self.normalCurveDistance(self.rootId, eachID, mesh_arg)
            else:
                dDistToNeighbor = vecNeighbor.length()  # -2 fps
            # get normalized direction vector on Psi from root to new point
            dDistance = self.plane.directedDistance(vecNeighbor)  # -2 fps
            vecToNeighborOnPsi = vecNeighbor - (self.normal * dDistance)  # -11 fps
            vecToNeighborOnPsi.normalize()  # -0.8 fps
            # create mapped point
            ptMapped = om.MPoint(vecToNeighborOnPsi * dDistToNeighbor)  # -12 fps
            # save point position
            self.points[eachID] = ptMapped
    
    def calculatePolygons(self, vertexFaces_arg, faceVertices_arg, polygonsToSave_arg=None):
        """calculate and save polygons, which have all their vertices mapped"""
        # if polygonsToSave_arg is given, just save them. no error checking. made for initial neighbor mapping
        if polygonsToSave_arg:
            for eachPoly in polygonsToSave_arg:
                self.facePoints[eachPoly] = faceVertices_arg[eachPoly]
            return
        # else calculate faces from mapped points
        #    get all polygons connected to any mapped point
        connectedPolygons = []
        for eachID in self.points:
            connectedPolygons += vertexFaces_arg[eachID]
        #     remove duplicates
        connectedPolygons = list(set(connectedPolygons))
        # save complete faces
        for eachPoly in connectedPolygons:
            allVertices = True
            for eachVertex in faceVertices_arg[eachPoly]:
                if eachVertex not in self.points:
                    allVertices = False
                    break
            if allVertices:
                self.facePoints[eachPoly] = faceVertices_arg[eachPoly]
    
    def calculateBorderEdges(self, edgeVertices_arg, faceEdges_arg, newFaces_arg, borderEdgesToSave_arg=None):
        """ calculate and save border edges """
        # if borderEdgesToSave_arg is given, just save them. no error checking. made for initial neighbor mapping
        if borderEdgesToSave_arg:
            for eachEdge in borderEdgesToSave_arg:
                self.borderEdges[eachEdge] = edgeVertices_arg[eachEdge]
            return
        # else calculate border edges
        for eachFace in newFaces_arg:
            for eachEdge in faceEdges_arg[eachFace]:
                if eachEdge in self.borderEdges:
                    del self.borderEdges[eachEdge]
                else:
                    self.borderEdges[eachEdge] = edgeVertices_arg[eachEdge]
    
    def projectDisplaceVector(self, vec_arg, plane_arg):
        """project vector from handle-plane on this Psi plane"""
        # temporary just project vector without handle-plane adjustment
        dDistance = self.plane.directedDistance(vec_arg)
        self.displace = om.MPoint((self.normal * dDistance) - vec_arg)  # todo: why not vec-planevec
    
    def getConnectedFace(self, edgeFaces_arg):
        # return face, which is connected to the closest borderEdge, which is intersected by ptDisplace
        idClosest = None
        distanceClosest = None
        vecDisplace = om.MVector(self.displace)
        for each in self.borderEdges:
            # angle of edge points
            vecEdge1 = om.MVector(self.points[self.borderEdges[each][0]])
            vecEdge2 = om.MVector(self.points[self.borderEdges[each][1]])
            angleEdge = vecEdge1.angle(vecEdge2)
            # angles between displace and each edge point
            angle1 = vecDisplace.angle(vecEdge1)
            angle2 = vecDisplace.angle(vecEdge2)
            hit = False
            # check if displace intersects edge
            if angle1 <= 0.0000001:
                # on edge point
                eachDistance = vecEdge1.length()
                idClosest = each
                hit = True
            elif angle2 <= 0.0000001:
                # on edge point
                eachDistance = vecEdge2.length()
                idClosest = each
                hit = True
            elif angle1 < angleEdge and angle2 < angleEdge:
                # between edge points
                weight1 = 1 - angle1 / angleEdge
                weight2 = 1 - angle2 / angleEdge
                eachDistance = weight1 * vecEdge1.length() + weight2 * vecEdge2.length()
                idClosest = each
                hit = True
            # save if first hit or shorter distance than current
            if hit and (idClosest is None or eachDistance < distanceClosest):
                idClosest = each
                distanceClosest = eachDistance
        
        # error check
        if idClosest is None:
            raise NameError('Did not find a border edge in getConnectedFace')
        
        # get new face
        for eachFace in edgeFaces_arg[idClosest]:
            if eachFace not in self.facePoints:
                return eachFace
        
        raise NameError('Did not return face id in getConnectedFace')
    
    # return face id that projected distplace point is on
    #    note: only works with convex polygons
    # algorithm from:
    # "Determining if a point lies on the interior of a polygon"
    # http://paulbourke.net/geometry/insidepoly/
    def pointInPolygon(self, v1_arg, v2_arg, faceIdsToCheck_arg=None):
        anglesums = []
        ids = []
        faceIdsToCheck = self.facePoints
        # only check given face ids. to improve performance 
        #    when mapping is increased -> only new face has to be checked
        if faceIdsToCheck_arg:
            faceIdsToCheck = faceIdsToCheck_arg
        from math import acos
        EPSILON = 0.0000001
        TWOPI = 6.283185307
        p1 = v1_arg
        p2 = v2_arg
        for eachId in faceIdsToCheck:
            q = self.displace
            anglesum = 0
            p = self.facePoints[eachId]
            n = len(p)
            for i in range(n):
                # if displace point is on vertex, return face
                p1.x = self.points[p[i]].x - q.x
                p1.y = self.points[p[i]].y - q.y
                p1.z = self.points[p[i]].z - q.z
                
                p2.x = self.points[p[(i + 1) % n]].x - q.x
                p2.y = self.points[p[(i + 1) % n]].y - q.y
                p2.z = self.points[p[(i + 1) % n]].z - q.z
                
                m1 = p1.length()
                m2 = p2.length()
                if m1 * m2 <= EPSILON:
                    return eachId
                else:
                    costheta = (p1.x * p2.x + p1.y * p2.y + p1.z * p2.z) / (m1 * m2)
                # costheta between -1.0 and 1.0 (python rounding?? does make it -1.000..1 or 1.000..1 sometimes) 
                if costheta < -1.0:
                    costheta = -1.0
                elif costheta > 1.0:
                    costheta = 1.0
                anglesum += acos(costheta)
            if anglesum + EPSILON >= TWOPI and anglesum - EPSILON <= TWOPI:  # rounding... instead of anglesum == TWOPI
                return eachId
            anglesums.append(anglesum)
            ids.append(eachId)
        return None
    
    # calculate UV value for ptDisplace on given face (Barycentric Coordinates)
    # algorithm from paper:
    # "Barycentric Coordinates for Arbitrary Polygons in the Plane"
    def getPositionUv(self, faceId_arg, faceUs_arg, faceVs_arg):
        # eachPsi.displace, eachPsi.points, eachPsi.facePoints
        # get uvs
        fUi = faceUs_arg
        fVi = faceVs_arg
        # get vertices / MPoints
        vertexIds = self.facePoints[faceId_arg]
        vi = []
        for eachId in vertexIds:
            vi.append(self.points[eachId])
        n = len(vi)
        v = self.displace
        # algorithm
        si = []  # vectors from ptDisplace to each vi
        for i in range(n):
            si.append(vi[i] - v)
        
        ri = []  # distances from v to each vi
        Ai = []  # plane area between si[i] and si[i+1] (crossproduct/2)
        Di = []  # dot product of si[i] and si[i+1]
        for i in range(n):
            # this for loop is for the special cases that v is on a vertex or edge
            ip = i + 1  # for last loop iteration #todo: better python way with lists?
            if ip == n:
                ip = 0
            ri.append(si[i].length())
            Ai.append((si[i] ^ si[ip]).length() / 2)
            Di.append(si[i].x * si[ip].x + si[i].y * si[ip].y + si[i].z * si[ip].z)
            if ri[i] < 0.0001:  # v on vertex #todo rounding avoidable?
                return [fUi[i], fVi[i]]
            if Ai[i] < 0.000001 and Di[i] < 0:  # v on edge #todo rounding avoidable?
                ri.append(si[ip].length())
                fU = (ri[ip] * fUi[i] + ri[i] * fUi[ip]) / (ri[i] + ri[ip])
                fV = (ri[ip] * fVi[i] + ri[i] * fVi[ip]) / (ri[i] + ri[ip])
                return [fU, fV]
        
        fU = 0
        fV = 0
        W = 0
        for i in range(n):
            # this for loop is for 'normal' cases
            ip = i + 1  # for last loop iteration #todo: better python way with lists?
            if ip == n:
                ip = 0
            w = 0
            if Ai[i - 1] != 0:
                w = w + (ri[i - 1] - Di[i - 1] / ri[i]) / Ai[i - 1]
            if Ai[i] != 0:
                w = w + (ri[ip] - Di[i] / ri[i]) / Ai[i]
            fU = fU + w * fUi[i]
            fV = fV + w * fVi[i]
            W = W + w
        return [fU / W, fV / W]
    
    def normalCurveDistance(self, firstPointId_arg, secondPointId_arg, fnMesh_arg):
        return 0.1


def nodeInitializer():
    nAttr = om.MFnNumericAttribute()
    rAttr = om.MRampAttribute()
    cAttr = om.MFnCompoundAttribute()
    eAttr = om.MFnEnumAttribute()
    mAttr = om.MFnMatrixAttribute()
    tAttr = om.MFnTypedAttribute()
    # input user
    #     aPosition
    prSlideNode.aPosition = nAttr.create("position", "pos", om.MFnNumericData.kInt, 0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    prSlideNode.addAttribute(prSlideNode.aPosition)
    #     aAlgorithm
    prSlideNode.aAlgorithm = eAttr.create("algorithm", "alg", 0)
    eAttr.setKeyable(True)
    eAttr.addField("slide closestPoint", 0)
    eAttr.addField("slide paper", 1)
    prSlideNode.addAttribute(prSlideNode.aAlgorithm)
    #     aHandleVisibility
    prSlideNode.aFlipOpposingSide = nAttr.create("flipOpposingSide", "fos", om.MFnNumericData.kBoolean, 0.0)
    nAttr.setKeyable(True)
    prSlideNode.addAttribute(prSlideNode.aFlipOpposingSide)
    #     aHandleVisibility
    prSlideNode.aHandleVisibility = nAttr.create("handleVisibility", "hv", om.MFnNumericData.kBoolean, 1.0)
    nAttr.setKeyable(True)
    prSlideNode.addAttribute(prSlideNode.aHandleVisibility)
    #     aFalloffType
    prSlideNode.aFalloffType = eAttr.create("falloffType", "fot", 1)
    eAttr.setKeyable(True)
    eAttr.addField("painted weight", 0)
    eAttr.addField("radius", 1)
    prSlideNode.addAttribute(prSlideNode.aFalloffType)
    #     aRadius
    prSlideNode.aRadius = nAttr.create("radius", "rr", om.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.01)
    prSlideNode.addAttribute(prSlideNode.aRadius)
    #     aRadiusFalloff
    prSlideNode.aRadiusFalloff = rAttr.createCurveRamp("radiusFalloff", "rfo")
    prSlideNode.addAttribute(prSlideNode.aRadiusFalloff)
    #     aFalloffWeight
    prSlideNode.aFalloffWeights = tAttr.create('falloffWeights', 'fow', om.MFnNumericData.kDoubleArray)
    tAttr.setHidden(True)
    # default value... does not seem to be necessary/work properly
    # daWeightsDefault = om.MDoubleArray()
    # fnWeightsDefault = om.MFnDoubleArrayData()
    # oWeightsDefault = fnWeightsDefault.create( daWeightsDefault )
    # tAttr.setDefault( oWeightsDefault )
    #     aFalloffWeightList
    prSlideNode.aFalloffWeightList = cAttr.create('falloffWeightsList', 'fwl')
    cAttr.addChild(prSlideNode.aFalloffWeights)
    cAttr.setHidden(True)
    cAttr.setArray(True)
    cAttr.setUsesArrayDataBuilder(True)
    prSlideNode.addAttribute(prSlideNode.aFalloffWeightList)
    # input deformer
    #     aDisplace
    prSlideNode.aDisplaceX = nAttr.create("displaceX", "dpx", om.MFnNumericData.kDouble, 0.0)
    nAttr.setReadable(False)
    prSlideNode.aDisplaceY = nAttr.create("displaceY", "dpy", om.MFnNumericData.kDouble, 0.0)
    nAttr.setReadable(False)
    prSlideNode.aDisplaceZ = nAttr.create("displaceZ", "dpz", om.MFnNumericData.kDouble, 0.0)
    nAttr.setReadable(False)
    prSlideNode.aDisplace = cAttr.create("displace", "dsp")
    cAttr.addChild(prSlideNode.aDisplaceX)
    cAttr.addChild(prSlideNode.aDisplaceY)
    cAttr.addChild(prSlideNode.aDisplaceZ)
    cAttr.setKeyable(True)
    cAttr.setReadable(False)
    prSlideNode.addAttribute(prSlideNode.aDisplace)
    #     aNullParentInverse
    prSlideNode.aNullParentInverse = mAttr.create('nullParentInverse', 'npi')
    mAttr.setReadable(False)
    prSlideNode.addAttribute(prSlideNode.aNullParentInverse)
    # output deformer
    #     aNullTranslate
    prSlideNode.aNullTranslateX = nAttr.create("nullTranslateX", "ntx", om.MFnNumericData.kDouble, 0.0)
    nAttr.setWritable(False)
    prSlideNode.aNullTranslateY = nAttr.create("nullTranslateY", "nty", om.MFnNumericData.kDouble, 0.0)
    nAttr.setWritable(False)
    prSlideNode.aNullTranslateZ = nAttr.create("nullTranslateZ", "ntz", om.MFnNumericData.kDouble, 0.0)
    nAttr.setWritable(False)
    prSlideNode.aNullTranslate = cAttr.create("nullTranslate", "ntr")
    cAttr.addChild(prSlideNode.aNullTranslateX)
    cAttr.addChild(prSlideNode.aNullTranslateY)
    cAttr.addChild(prSlideNode.aNullTranslateZ)
    cAttr.setWritable(False)
    prSlideNode.addAttribute(prSlideNode.aNullTranslate)
    
    # affects
    aOutputgeom = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    aInputgeom = OpenMayaMPx.cvar.MPxDeformerNode_inputGeom
    #     default
    prSlideNode.attributeAffects(aInputgeom, prSlideNode.aNullTranslate)
    #     input user
    prSlideNode.attributeAffects(prSlideNode.aPosition, aOutputgeom)
    prSlideNode.attributeAffects(prSlideNode.aPosition, prSlideNode.aNullTranslate)
    prSlideNode.attributeAffects(prSlideNode.aFalloffType, aOutputgeom)
    prSlideNode.attributeAffects(prSlideNode.aRadius, aOutputgeom)
    prSlideNode.attributeAffects(prSlideNode.aRadiusFalloff, aOutputgeom)
    prSlideNode.attributeAffects(prSlideNode.aAlgorithm, aOutputgeom)
    prSlideNode.attributeAffects(prSlideNode.aFlipOpposingSide, aOutputgeom)
    prSlideNode.attributeAffects(prSlideNode.aFalloffWeights, aOutputgeom)
    #     input deformer
    prSlideNode.attributeAffects(prSlideNode.aDisplace, aOutputgeom)
    #     output
    prSlideNode.attributeAffects(prSlideNode.aNullParentInverse, prSlideNode.aNullTranslate)
    
    # Make deformer weights paintable
    import maya.cmds as mc
    mc.makePaintable('prSlideNode', 'weights', attrType='multiFloat', shapeMode='deformer')
    mc.makePaintable('prSlideNode', 'falloffWeights', attrType='doubleArray', shapeMode='deformer')


def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Parzival Roethlein", "0.9.1")
    try:
        mplugin.registerNode(prSlideNode.pluginName, prSlideNode.pluginId, nodeCreator, nodeInitializer,
                             OpenMayaMPx.MPxNode.kDeformerNode)
    except:
        sys.stderr.write("Failed to register node: %s\n" % prSlideNode.pluginName)


def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(prSlideNode.pluginId)
    except:
        sys.stderr.write("Failed to unregister node: %s\n" % prSlideNode.pluginName)


def nodeCreator():
    return OpenMayaMPx.asMPxPtr(prSlideNode())


mm.eval('''
global proc AEprSlideNodeTemplate( string $nodeName )
{
    //AEswatchDisplay  $nodeName;
    editorTemplate -beginScrollLayout;
        editorTemplate -beginLayout "prSlideNode Attributes" -collapse 0;
            editorTemplate -addControl "position";
            editorTemplate -addControl "algorithm";
            editorTemplate -addControl "handleVisibility";
            editorTemplate -addControl "scale";
            editorTemplate -addControl "falloffType";
            editorTemplate -addControl "radius";
            AEaddRampControl ($nodeName+".radiusFalloff");
        editorTemplate -endLayout;
    
    // include/call base class/node attributes
    AEgeometryFilterCommon $nodeName;
    AEgeometryFilterInclude $nodeName;
    
    editorTemplate -addExtraControls;
    editorTemplate -endScrollLayout;
    
    editorTemplate -suppress "displace";
    editorTemplate -suppress "nullParentInverse";
    editorTemplate -suppress "weightList";
};
''')
