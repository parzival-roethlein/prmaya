'''
D E S C R I P T I O N:
in prHeatDeformer.h

T E S T:
####################
def prHeatDeformerTest():
    import maya.cmds as mc
    import maya.mel as mm
    mc.file(new=True, f=True)
    try:
        mc.unloadPlugin( "prHeatDeformer.py" )
    except:
        pass
    mc.loadPlugin( r"C:\Users\prothlein\Documents\eclipseworkspace\svn\prRS\plug-ins\prHeatDeformer\prHeatDeformer.py" )
    #mc.file("C:/Users/prothlein/Documents/eclipseworkspace/svn/prRS/plug-ins/prHeatDeformer/cube.mb", o=1, f=1 )
    mc.file("C:/Users/prothlein/Documents/eclipseworkspace/svn/prRS/plug-ins/prHeatDeformer/plane.mb", o=1, f=1 )
    mc.select( 'squash', 'stretch', 'original', 'target' )
    mm.eval( 'prHeatDeformer()' )
    mc.setAttr( 'prHeatDeformer1.deformationType', 2 )
prHeatDeformerTest()
####################
'''

import maya.OpenMaya as om
import maya.OpenMayaMPx as OpenMayaMPx
import maya.mel as mm
import sys

# node definition
class prHeatDeformer(OpenMayaMPx.MPxDeformerNode):
    # plug-in
    pluginName = "prHeatDeformer"
    pluginId = om.MTypeId(0x0010A51C)# from Filmakademie, not written in their wiki
    
    # attributes: deformer internal
    aOrigMesh = om.MObject()
    aSquashMesh = om.MObject()
    aStretchMesh = om.MObject()
    # attributes: for user
    #     color
    aDisplayColors = om.MObject()
    aColorBase = om.MObject()
    aColorStretch = om.MObject()
    aColorSquash = om.MObject()
    #     heat / algorithm
    aMeasureTypeHeat = om.MObject()
    aMultiplyHeat = om.MObject()
    aSquashMultiplyHeat = om.MObject()
    aStretchMultiplyHeat = om.MObject()
    aMaxHeat = om.MObject()
    aSquashMaxHeat = om.MObject()
    aStretchMaxHeat = om.MObject()
    aGrowHeat = om.MObject()
    aSquashGrowHeat = om.MObject()
    aStretchGrowHeat = om.MObject()
    aIterationsSmoothHeat = om.MObject()
    aStrengthSmoothHeat = om.MObject()
    #     deformation
    aDeformationType = om.MObject()
    aIterationsSmoothDeformation = om.MObject()
    aStrengthSmoothDeformation = om.MObject()
    #     blendShape
    aTangentSpace = om.MObject()
    
    # constructor
    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
    
    def postConstructor(self):
        ''' to be able to modify vertex color with the deformer and viewport/mesh updates '''
        self.setDeformationDetails( OpenMayaMPx.MPxDeformerNode.kDeformsColors )
    
    '''
    def accessoryNodeSetup( self, cmd ):
        # connect displayColors attribute to mesh
        oThis = self.thisMObject()
        fnThis = om.MFnDependencyNode( oThis )
        nameThis = fnThis.name()
        
        # get output shapes # ERROR shape.displayColors not connectable ?! - why?
        import maya.cmds as mc
        for each in mc.listConnections( nameThis+'.outputGeometry', p=1 ):
            cmd.commandToExecute( 'connectAttr '+nameThis+'.displayColors '+each[:each.find('.')]+'.displayColors -f' )
        #
    '''
    
    # deform
    def deform(self,block,iter,mat,multiIndex):
        # ###################################
        # get attributes
        # ###################################
        # envelope
        envelope = block.inputValue( OpenMayaMPx.cvar.MPxDeformerNode_envelope ).asFloat()
        if( envelope == 0.0 ):
            return
        
        # ==================================
        # aOrigMesh
        oOrig = block.inputValue( self.aOrigMesh ).asMesh()
        if oOrig.isNull():
            return
        fnOrig = om.MFnMesh( oOrig )
        
        # ==================================
        # input[multiIndex].inputGeometry
        hInput = block.outputArrayValue( self.input )
        hInput.jumpToElement( multiIndex )
        hInputGeom = hInput.outputValue().child( self.inputGeom )
        oInputGeom = hInputGeom.asMesh()
        fnCurrent = om.MFnMesh( oInputGeom )
        
        # ==================================
        # aDisplayColors
        displayColors = block.inputValue( self.aDisplayColors ).asBool()
        if( displayColors ):
            colorBase = block.inputValue( self.aColorBase ).asFloatVector()
            colorStretch = block.inputValue( self.aColorStretch ).asFloatVector()
            colorSquash = block.inputValue( self.aColorSquash ).asFloatVector()
        
        # ==================================
        # aMeasureTypeHeat
        measureTypeHeat = block.inputValue( self.aMeasureTypeHeat ).asShort()
        
        # aMultiplyHeat aSquashMultiplyHeat aStretchMultiplyHeat
        multHeat = block.inputValue( self.aMultiplyHeat ).asFloat()
        squashMultHeat = block.inputValue( self.aSquashMultiplyHeat ).asFloat()
        stretchMultHeat = block.inputValue( self.aStretchMultiplyHeat ).asFloat()
        if( multHeat == 0.0 or squashMultHeat == 0.0 and stretchMultHeat == 0.0 ):
            return
        
        # aMaxHeat aSquashMaxHeat aStretchMaxHeat
        maxHeat = block.inputValue( self.aMaxHeat ).asBool()
        squashMaxHeat = block.inputValue( self.aSquashMaxHeat ).asFloat() * -1
        stretchMaxHeat = block.inputValue( self.aStretchMaxHeat ).asFloat()
        if( squashMaxHeat == 0.0 and stretchMaxHeat == 0.0 ):
            return
        
        # aGrowHeat aSquashGrowHeat aStretchGrowHeat
        growHeat = block.inputValue( self.aGrowHeat ).asInt()
        squashGrowHeat = block.inputValue( self.aSquashGrowHeat ).asInt()
        stretchGrowHeat = block.inputValue( self.aStretchGrowHeat ).asInt()
        
        # aIterationsSmoothHeat
        iterationsSmoothHeat = block.inputValue( self.aIterationsSmoothHeat ).asInt()
        
        # aStrengthSmoothHeat
        strengthSmoothHeat  = block.inputValue( self.aStrengthSmoothHeat ).asFloat() 
        
        # ==================================
        # aDeformationType
        deformationType = block.inputValue( self.aDeformationType ).asShort()
        if( deformationType == 0 ):
            return
        
        # aIterationsSmoothDeformation
        iterationsSmoothDeformation = block.inputValue( self.aIterationsSmoothDeformation ).asInt()
        
        # aStrengthSmoothDeformation
        strengthSmoothDeformation = block.inputValue( self.aStrengthSmoothDeformation ).asFloat()
        
        # aTangentSpace
        tangentSpace = False
        if( deformationType == 2 ):
            tangentSpace = block.inputValue( self.aTangentSpace ).asShort()
        
        # ==================================
        # aStretchMesh aSquashMesh
        if( deformationType == 2 ):
            # aStretchMesh
            oStretch = block.inputValue( self.aStretchMesh ).asMesh()
            if oStretch.isNull():
                return
            fnStretch = om.MFnMesh( oStretch )
            stretchPoints = om.MPointArray()
            fnStretch.getPoints(stretchPoints)
            # aSquashMesh
            oSquash = block.inputValue( self.aSquashMesh ).asMesh()
            if oSquash.isNull():
                return
            fnSquash = om.MFnMesh( oSquash )
            squashPoints = om.MPointArray()
            fnSquash.getPoints(squashPoints)
            # orig points
            origPoints = om.MPointArray()
            fnOrig.getPoints(origPoints)
        
        # ###################################
        # Gather information TODO: STORE in node (refresh button)
        # ###################################
        d_util = om.MScriptUtil()
        doublePtr = d_util.asDoublePtr()
        # orig edge lengths
        itEdgeOrig = om.MItMeshEdge( oOrig )
        edgeLengthsOrig = []
        lengthSum = 0.0
        while not itEdgeOrig.isDone():
            itEdgeOrig.getLength( doublePtr )
            eachLength = d_util.getDouble( doublePtr )
            lengthSum += eachLength
            edgeLengthsOrig.append( eachLength )
            itEdgeOrig.next()
        edgeLengthAvrg = lengthSum / itEdgeOrig.count()
        # orig face area
        itPolyOrig = om.MItMeshPolygon( oOrig )
        polyAreasOrig = []
        while not itPolyOrig.isDone():
            itPolyOrig.getArea( doublePtr )
            eachArea = d_util.getDouble( doublePtr )
            polyAreasOrig.append( eachArea )
            itPolyOrig.next()
        # connected edges and vertices (and faces)
        connectedEdges = []
        connectedPoints = []
        connectedFaces = []
        itPointCurrent = om.MItMeshVertex( oOrig )
        iaConnectedObjects = om.MIntArray()
        while not itPointCurrent.isDone():
            # edges
            itPointCurrent.getConnectedEdges( iaConnectedObjects )
            connectedEdges.append( list(iaConnectedObjects) )
            # vertices
            itPointCurrent.getConnectedVertices( iaConnectedObjects )
            connectedPoints.append( list(iaConnectedObjects) )
            # faces
            itPointCurrent.getConnectedFaces( iaConnectedObjects )
            connectedFaces.append( list(iaConnectedObjects) )
            # finish
            itPointCurrent.next()
        
        # ###################################
        # Gather information per call
        # ###################################
        d_util = om.MScriptUtil()
        doublePtr = d_util.asDoublePtr()
        # current polygon area
        if( measureTypeHeat == 0 ):
            itPolyCurrent = om.MItMeshPolygon( oInputGeom )
            polyAreasCurrent = []
            while not itPolyCurrent.isDone():
                itPolyCurrent.getArea( doublePtr )
                eachArea = d_util.getDouble( doublePtr )
                polyAreasCurrent.append( eachArea )
                itPolyCurrent.next()
        # current edge length
        elif( measureTypeHeat ==1 ):
            edgeLengthsCurrent = []
            itEdgeCurrent = om.MItMeshEdge( oInputGeom )
            while not itEdgeCurrent.isDone():
                itEdgeCurrent.getLength( doublePtr )
                edgeLengthsCurrent.append( d_util.getDouble( doublePtr ) )
                itEdgeCurrent.next()
        # current normals
        if( deformationType == 1 ):
            currentNormals = om.MFloatVectorArray()
            fnCurrent.getVertexNormals( False, currentNormals, om.MSpace.kObject ) 
        # find relevant points
        paPoints = om.MPointArray()
        ptIndices = []
        ptWeights = []
        while not iter.isDone():
            iterIndex = iter.index()
            pt = iter.position()
            # get painted weight
            wPt = self.weightValue( block, multiIndex, iterIndex )
            if( wPt == 0.0 ):
                iter.next()
                continue
            # only store points with weights
            paPoints.append( pt )
            ptIndices.append( iterIndex )
            ptWeights.append( wPt )
            iter.next()
        iter.reset()
        
        # ###################################
        # Heat Calculation 
        # ###################################
        # input: relevant points, default lengths, current lengths, edgeLengthAvrg
        # output: arHeat
        #
        # eachHeat =-1.0 // origLength*0 // squashed
        # eachHeat = 0.0 // origLength*1 // default
        # eachHeat = 1.0 // origLength*2 // stretched
        arHeat = []
        for x, eachId in enumerate( ptIndices ):
            # measure difference between orig and current
            currentMeasure = 0.0
            origMeasure = 0.0
            # faces
            if( measureTypeHeat == 0 ):
                for eachFace in connectedFaces[eachId]:
                    currentMeasure += polyAreasCurrent[eachFace]
                    origMeasure += polyAreasOrig[eachFace]
                eachHeat = (( currentMeasure - origMeasure ) / origMeasure )
            # edges
            elif( measureTypeHeat == 1 ):
                for eachEdge in connectedEdges[eachId]:
                    currentMeasure += edgeLengthsCurrent[eachEdge]
                    origMeasure += edgeLengthsOrig[eachEdge]
                # to have similar behavior as face area multiply
                eachHeat = (( currentMeasure - origMeasure ) / origMeasure )*2
            #
            
            # stretch and squash specific modification
            if( eachHeat < 0.0 ):
                eachHeat *= squashMultHeat * multHeat
                if( eachHeat < squashMaxHeat and maxHeat ):
                    eachHeat = squashMaxHeat
            elif( eachHeat > 0.0 ):
                eachHeat *= stretchMultHeat * multHeat
                if( eachHeat > stretchMaxHeat and maxHeat ):
                    eachHeat = stretchMaxHeat
            # store
            arHeat.append( eachHeat )
        
        # ###################################
        # Heat Grow
        # ###################################
        squashGrowHeat += growHeat
        stretchGrowHeat += growHeat
        if( squashGrowHeat or stretchGrowHeat ):
            # find iteration count
            growIterations = squashGrowHeat
            if( stretchGrowHeat > growIterations  ):
                growIterations = stretchGrowHeat
            
            for y in range( growIterations ):
                arHeatNew = list(arHeat)
                # loop through effected points
                for x, eachId in enumerate( ptIndices ):
                    strongestSquash = arHeatNew[x]
                    strongestStretch = arHeatNew[x]
                    # loop over neighbors
                    for eachNeighborId in connectedPoints[eachId]:
                        if( eachNeighborId in ptIndices ):
                            eachNeighborHeat = arHeat[ ptIndices.index(eachNeighborId) ]
                            if( eachNeighborHeat < strongestSquash ):
                                strongestSquash = eachNeighborHeat
                            if( eachNeighborHeat > strongestStretch ):
                                strongestStretch = eachNeighborHeat
                    # set proper value
                    if( squashGrowHeat > y and stretchGrowHeat > y ):
                        newValue = 0.0
                        if( strongestSquash < 0.0 ):
                            newValue = strongestSquash
                        if( strongestStretch > 0.0 ):
                            newValue += strongestStretch
                        if( newValue ):
                            arHeatNew[x] = newValue
                    elif( squashGrowHeat > y and strongestSquash < 0.0 ):
                        if( arHeatNew[x] > 0.0 ):
                            arHeatNew[x] += strongestSquash
                        else:
                             arHeatNew[x] = strongestSquash
                    elif( stretchGrowHeat > y and strongestStretch > 0.0 ):
                        if( arHeatNew[x] < 0.0 ):
                            arHeatNew[x] += strongestStretch
                        else:
                            arHeatNew[x] = strongestStretch
                arHeat = arHeatNew
            #
        
        # ###################################
        # Heat Smooth
        # ###################################
        # input: arHeat
        # output: arHeat
        for y in range( iterationsSmoothHeat ):
            arHeatNew = list(arHeat)
            for x, eachId in enumerate( ptIndices ):
                neighborIds = connectedPoints[eachId]
                neighborAvrg = 0.0
                validNeighbor = False
                for eachNeighborId in neighborIds:
                    if( eachNeighborId in ptIndices ):
                        validNeighbor = True
                        neighborAvrg += arHeat[ ptIndices.index(eachNeighborId) ]
                if( validNeighbor ):
                    neighborAvrg /= len(neighborIds)
                    arHeatNew[x] = arHeatNew[x]*(1.0-strengthSmoothHeat) + neighborAvrg*strengthSmoothHeat
            arHeat = arHeatNew
        
        # ###################################
        # Heat Display
        # ###################################
        # input: arHeat
        # result: vertexColors
        if( displayColors ):
            colorList = om.MColorArray()
            indexList = om.MIntArray()
            for x, eachId in enumerate( ptIndices ):
                # colorBase colorStretch colorSquash
                eachColor = om.MFloatVector( colorBase )
                if( arHeat[x] > 0.0 ):
                    eachColor += (colorStretch - eachColor)*( arHeat[x] )
                elif( arHeat[x] < 0.0 ):
                    eachColor += (colorSquash - eachColor)*( arHeat[x]*-1 )
                colorList.append( om.MColor( eachColor.x, eachColor.y, eachColor.z, 1.0 ) )
                indexList.append( eachId )
                #fnCurrent.setVertexColor( om.MColor(eachColor.x, eachColor.y, eachColor.z), eachId )# (setting all at once is faster)
            fnCurrent.setVertexColors( colorList, indexList )
        
        # ###################################
        # Deformation Calculation
        # ###################################
        # input: heatArray
        # output: motionVectorArray
        arVectors = []
        for x, eachId in enumerate( ptIndices ):
            eachHeat = arHeat[x]
            vecMove = om.MVector()
            
            # skip calculation for 0.0 heat
            if( eachHeat == 0.0 ):
                arVectors.append( vecMove )
                continue
            
            # ###################################
            # Normal
            # ###################################
            if( deformationType == 1 ):
                # normal deformation
                vecMove += om.MVector(currentNormals[eachId]) * (eachHeat*-1) * edgeLengthAvrg
            
            # ###################################
            # BlendShape
            # ###################################
            if( deformationType == 2 ):
                if( eachHeat < 0.0 ):
                    targetPt = squashPoints[eachId]
                    vecMove += (targetPt - origPoints[eachId]) * (eachHeat*-1) 
                elif( eachHeat > 0.0 ):
                    targetPt = stretchPoints [eachId]
                    vecMove += (targetPt - origPoints[eachId]) * (eachHeat)
                # tangent spaces
                if( tangentSpace ):
                    matTangentOrig = getTangentSpace( tangentSpace, fnOrig, eachId, connectedFaces[eachId] )
                    matTangentCurrent = getTangentSpace( tangentSpace, fnCurrent, eachId, connectedFaces[eachId] )
                    vecMove *= matTangentOrig.inverse() * matTangentCurrent
                #
            # save vector
            arVectors.append( vecMove )
        
        # ###################################
        # Deformation Smooth
        # ###################################
        # input: motionVectorArray
        # result: motionVectorArray
        for x in range( iterationsSmoothDeformation ):
            arVectorsNew = list(arVectors)
            for x, eachId in enumerate( ptIndices ):
                neighborIds = connectedPoints[eachId]
                neighborAvrg = om.MVector()
                validNeighbor = False
                for eachNeighborId in neighborIds:
                    if( eachNeighborId in ptIndices ):
                        validNeighbor = True
                        neighborAvrg += arVectors[ ptIndices.index(eachNeighborId) ]
                if( validNeighbor ):
                    neighborAvrg /= len(neighborIds)
                    arVectorsNew[x] = arVectorsNew[x]*(1.0-strengthSmoothDeformation) + neighborAvrg*strengthSmoothDeformation
            arVectors = arVectorsNew
        
        # ###################################
        # Deformation
        # ###################################
        # input: motionVectorArray, weights
        # result: deformed mesh
        counter = 0
        while not iter.isDone():
            if( iter.index() in ptIndices ):
                iter.setPosition( paPoints[counter] + arVectors[counter] * ptWeights[counter] * envelope )
                counter += 1
            iter.next()
        #
    # deform
# class

def getTangentSpace( algorithm, fnMesh, vertexId, faceIds ):
    ''' return tangent space matrix of given vertexId on given MFnMesh'''
    # normal
    vNorm = om.MVector()
    fnMesh.getVertexNormal( vertexId, False, vNorm, om.MSpace.kObject )
    # tangent
    vTan = om.MVector()
    tmpVec = om.MVector()
    for eachFaceId in faceIds:
        fnMesh.getFaceVertexTangent( eachFaceId, vertexId, tmpVec, om.MSpace.kObject )
        vTan += tmpVec
        if( algorithm == 1 ):
            # just use first tangent. Because it is faster to calculate. will work in most cases, except for wrinkle area
            break
    vTan /= len(faceIds)
    # binormal from MFnMesh
    '''vBin = om.MVector()
    for eachFaceId in faceIds:
        fnMesh.getFaceVertexBinormal( eachFaceId, vertexId, tmpVec, om.MSpace.kObject )
        vBin += tmpVec
    vBin /= len(faceIds)'''
    # binormal from cross-product (is faster)
    vBin = vTan^vNorm
    # matrix
    matList = [ vTan.x,  vTan.y,  vTan.z, 0.0,
               vNorm.x, vNorm.y, vNorm.z, 0.0,
               vBin.x,   vBin.y,  vBin.z, 0.0,
                   0.0,     0.0,     0.0, 1.0 ]
    matTangent = om.MMatrix()
    om.MScriptUtil.createMatrixFromList( matList, matTangent )
    return matTangent

# initializer
def nodeInitializer():
    outgeoAr = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    # attribute type variables
    tAttr = om.MFnTypedAttribute()
    nAttr = om.MFnNumericAttribute()
    cAttr = om.MFnCompoundAttribute()
    gAttr = om.MFnGenericAttribute()
    eAttr = om.MFnEnumAttribute()
    
    # ###############################
    # essential (deformer)
    # ###############################
    # aOrigMesh
    prHeatDeformer.aOrigMesh = gAttr.create( "origMesh", "origMesh" )
    gAttr.setReadable(False)
    gAttr.addDataAccept( om.MFnMeshData.kMesh )
    prHeatDeformer.addAttribute( prHeatDeformer.aOrigMesh )
    prHeatDeformer.attributeAffects(prHeatDeformer.aOrigMesh, outgeoAr)
    
    # ###############################
    # blendshape (deformer)
    # ###############################
    # aSquashMesh
    prHeatDeformer.aSquashMesh = gAttr.create( "squashMesh", "squashMesh" )
    gAttr.setReadable(False)
    gAttr.addDataAccept( om.MFnMeshData.kMesh )
    prHeatDeformer.addAttribute( prHeatDeformer.aSquashMesh )
    prHeatDeformer.attributeAffects(prHeatDeformer.aSquashMesh, outgeoAr)
    # aStretchMesh
    prHeatDeformer.aStretchMesh = gAttr.create( "stretchMesh", "stretchMesh" )
    gAttr.setReadable(False)
    gAttr.addDataAccept( om.MFnMeshData.kMesh )
    prHeatDeformer.addAttribute( prHeatDeformer.aStretchMesh )
    prHeatDeformer.attributeAffects(prHeatDeformer.aStretchMesh, outgeoAr)
    
    # ###############################
    # Color
    # ###############################
    # aDisplayColors
    prHeatDeformer.aDisplayColors = nAttr.create( "displayColors", "displayColors", om.MFnNumericData.kBoolean, 0 )
    nAttr.setKeyable(True)
    prHeatDeformer.addAttribute( prHeatDeformer.aDisplayColors )
    prHeatDeformer.attributeAffects(prHeatDeformer.aDisplayColors, outgeoAr)
    # aColorBase
    prHeatDeformer.aColorBase = nAttr.createColor( "colorBase", "colorBase" )
    nAttr.setDefault( 0.122, 0.122, 0.122 )
    prHeatDeformer.addAttribute( prHeatDeformer.aColorBase )
    prHeatDeformer.attributeAffects(prHeatDeformer.aColorBase, outgeoAr)
    # aColorSquash
    prHeatDeformer.aColorSquash = nAttr.createColor( "colorSquash", "colorSquash" )
    nAttr.setDefault( 1.0, 0.0, 0.0 )
    prHeatDeformer.addAttribute( prHeatDeformer.aColorSquash )
    prHeatDeformer.attributeAffects(prHeatDeformer.aColorSquash, outgeoAr)
    # aColorStretch
    prHeatDeformer.aColorStretch = nAttr.createColor( "colorStretch", "colorStretch" )
    nAttr.setDefault( 0.0, 1.0, 0.0 )
    prHeatDeformer.addAttribute( prHeatDeformer.aColorStretch )
    prHeatDeformer.attributeAffects(prHeatDeformer.aColorStretch, outgeoAr)
    
    # ###############################
    # heat / algorithm
    # ###############################
    # aMeasureTypeHeat
    prHeatDeformer.aMeasureTypeHeat = eAttr.create( "measureTypeHeat", "measureTypeHeat", 0 )
    eAttr.setKeyable(True)
    eAttr.addField( "Face Area", 0 )
    eAttr.addField( "Edge Length", 1 )
    prHeatDeformer.addAttribute( prHeatDeformer.aMeasureTypeHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aMeasureTypeHeat, outgeoAr)
    
    # aMultiplyHeat 
    prHeatDeformer.aMultiplyHeat = nAttr.create( "multiplyHeat", "multiplyHeat", om.MFnNumericData.kFloat, 1.0 )
    nAttr.setSoftMin(0.0)
    nAttr.setKeyable(True)
    prHeatDeformer.addAttribute( prHeatDeformer.aMultiplyHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aMultiplyHeat, outgeoAr)
    # aSquashMultiplyHeat
    prHeatDeformer.aSquashMultiplyHeat = nAttr.create( "squashMultiplyHeat", "squashMultiplyHeat", om.MFnNumericData.kFloat, 1.0 )
    nAttr.setSoftMin(0.0)
    nAttr.setKeyable(True)
    prHeatDeformer.addAttribute( prHeatDeformer.aSquashMultiplyHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aSquashMultiplyHeat, outgeoAr)
    # aStretchMultiplyHeat
    prHeatDeformer.aStretchMultiplyHeat = nAttr.create( "stretchMultiplyHeat", "stretchMultiplyHeat", om.MFnNumericData.kFloat, 1.0 )
    nAttr.setSoftMin(0.0)
    nAttr.setKeyable(True)
    prHeatDeformer.addAttribute( prHeatDeformer.aStretchMultiplyHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aStretchMultiplyHeat, outgeoAr)
    
    # aMaxHeat 
    prHeatDeformer.aMaxHeat = nAttr.create( "maxHeat", "maxHeat", om.MFnNumericData.kBoolean, 1 )
    nAttr.setKeyable(True)
    prHeatDeformer.addAttribute( prHeatDeformer.aMaxHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aMaxHeat, outgeoAr)
    # aSquashMaxHeat
    prHeatDeformer.aSquashMaxHeat = nAttr.create( "squashMaxHeat", "squashMaxHeat", om.MFnNumericData.kFloat, 1.0 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0.0 )
    prHeatDeformer.addAttribute( prHeatDeformer.aSquashMaxHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aSquashMaxHeat, outgeoAr)
    # aStretchMaxHeat
    prHeatDeformer.aStretchMaxHeat = nAttr.create( "stretchMaxHeat", "stretchMaxHeat", om.MFnNumericData.kFloat, 1.0 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0.0 )
    prHeatDeformer.addAttribute( prHeatDeformer.aStretchMaxHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aStretchMaxHeat, outgeoAr)
    
    # aGrowHeat
    prHeatDeformer.aGrowHeat = nAttr.create( "growHeat", "growHeat", om.MFnNumericData.kInt, 0 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0 )
    nAttr.setSoftMax( 10 )
    prHeatDeformer.addAttribute( prHeatDeformer.aGrowHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aGrowHeat, outgeoAr)
    # aSquashGrowHeat
    prHeatDeformer.aSquashGrowHeat = nAttr.create( "squashGrowHeat", "squashGrowHeat", om.MFnNumericData.kInt, 0 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0 )
    nAttr.setSoftMax( 10 )
    prHeatDeformer.addAttribute( prHeatDeformer.aSquashGrowHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aSquashGrowHeat, outgeoAr)
    # aStretchGrowHeat
    prHeatDeformer.aStretchGrowHeat = nAttr.create( "stretchGrowHeat", "stretchGrowHeat", om.MFnNumericData.kInt, 0 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0 )
    nAttr.setSoftMax( 10 )
    prHeatDeformer.addAttribute( prHeatDeformer.aStretchGrowHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aStretchGrowHeat, outgeoAr)
    
    # aIterationsSmoothHeat
    prHeatDeformer.aIterationsSmoothHeat = nAttr.create( "iterationsSmoothHeat", "iterationsSmoothHeat", om.MFnNumericData.kInt, 0 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0 )
    nAttr.setSoftMax( 10 )
    prHeatDeformer.addAttribute( prHeatDeformer.aIterationsSmoothHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aIterationsSmoothHeat, outgeoAr)
    # aStrengthSmoothHeat
    prHeatDeformer.aStrengthSmoothHeat = nAttr.create( "strengthSmoothHeat", "strengthSmoothHeat", om.MFnNumericData.kFloat, 0.2 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0.0 )
    nAttr.setSoftMax( 1.0 )
    prHeatDeformer.addAttribute( prHeatDeformer.aStrengthSmoothHeat )
    prHeatDeformer.attributeAffects(prHeatDeformer.aStrengthSmoothHeat, outgeoAr)
    
    # ###############################
    # deformation type (user)
    # ###############################
    prHeatDeformer.aDeformationType = eAttr.create( "deformationType", "deformationType", 0 )
    eAttr.setKeyable(True)
    eAttr.addField( "None", 0 )
    eAttr.addField( "Normal Vector", 1 )
    eAttr.addField( "BlendShape", 2 )
    prHeatDeformer.addAttribute( prHeatDeformer.aDeformationType )
    prHeatDeformer.attributeAffects(prHeatDeformer.aDeformationType, outgeoAr)
    
    # aIterationsSmoothDeformation
    prHeatDeformer.aIterationsSmoothDeformation = nAttr.create( "iterationsSmoothDeformer", "iterationsSmoothDeformer", om.MFnNumericData.kInt, 0 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0 )
    nAttr.setSoftMax( 10 )
    prHeatDeformer.addAttribute( prHeatDeformer.aIterationsSmoothDeformation )
    prHeatDeformer.attributeAffects(prHeatDeformer.aIterationsSmoothDeformation, outgeoAr)
    # aStrengthSmoothHeat
    prHeatDeformer.aStrengthSmoothDeformation = nAttr.create( "strengthSmoothDeformer", "strengthSmoothDeformer", om.MFnNumericData.kFloat, 0.2 )
    nAttr.setKeyable(True)
    nAttr.setMin( 0.0 )
    nAttr.setSoftMax( 1.0 )
    prHeatDeformer.addAttribute( prHeatDeformer.aStrengthSmoothDeformation )
    prHeatDeformer.attributeAffects(prHeatDeformer.aStrengthSmoothDeformation, outgeoAr)
    
    # ###############################
    # BlendShape
    # ##############################
    prHeatDeformer.aTangentSpace = eAttr.create( "tangentSpace", "tangentSpace", 2 )
    eAttr.setKeyable(True)
    eAttr.addField( "Off", 0 )
    eAttr.addField( "Simple", 1 )
    eAttr.addField( "Full", 2 )
    prHeatDeformer.addAttribute( prHeatDeformer.aTangentSpace )
    prHeatDeformer.attributeAffects(prHeatDeformer.aTangentSpace, outgeoAr)
    
    # ###############################
    # paintable
    # ###############################
    import maya.cmds as mc
    mc.makePaintable('prHeatDeformer', 'weights', attrType='multiFloat', shapeMode='deformer')

# creator
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( prHeatDeformer() )

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Parzival Roethlein", "0.0.1")
    try:
        mplugin.registerNode( prHeatDeformer.pluginName, prHeatDeformer.pluginId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kDeformerNode )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % prHeatDeformer.pluginName )

# un-initialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( prHeatDeformer.pluginId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % prHeatDeformer.pluginName )

# AEtemeplate for MRampAttributes and custom functions for deformer creation+connections
mm.eval(
'''
global proc AEprHeatDeformerTemplate( string $nodeName )
{
    AEswatchDisplay  $nodeName;
    editorTemplate -beginScrollLayout;
        editorTemplate -beginLayout "Color attributes" -collapse 0;
            editorTemplate -addControl "displayColors";
            editorTemplate -addControl "colorBase";
            editorTemplate -addControl "colorSquash";
            editorTemplate -addControl "colorStretch";
        editorTemplate -endLayout;
        editorTemplate -beginLayout "Heat attributes" -collapse 0;
            editorTemplate -addControl "measureTypeHeat";
            editorTemplate -addControl "multiplyHeat";
            editorTemplate -addControl "squashMultiplyHeat";
            editorTemplate -addControl "stretchMultiplyHeat";
            editorTemplate -addControl "maxHeat";
            editorTemplate -addControl "squashMaxHeat";
            editorTemplate -addControl "stretchMaxHeat";
            editorTemplate -addControl "growHeat";
            editorTemplate -addControl "squashGrowHeat";
            editorTemplate -addControl "stretchGrowHeat";
            editorTemplate -addControl "iterationsSmoothHeat";
            editorTemplate -addControl "strengthSmoothHeat";
        editorTemplate -endLayout;
        editorTemplate -beginLayout "Deformation attributes" -collapse 0;
            editorTemplate -addControl "deformationType";
            editorTemplate -addControl "strengthSmoothDeformer";
            editorTemplate -addControl "iterationsSmoothDeformer";
        editorTemplate -endLayout;
        editorTemplate -beginLayout "BlendShape attributes" -collapse 0;
            editorTemplate -addControl "tangentSpace";
        editorTemplate -endLayout;
        // include/call base class/node attributes
        AEgeometryFilterCommon $nodeName;
        AEgeometryFilterInclude $nodeName;
        // add missing attrs (should be none)
        editorTemplate -addExtraControls;
    editorTemplate -endScrollLayout;
    // hide attrs 
    editorTemplate -suppress "weightList";
};

global proc string prHeatDeformer()
{
    string $sel[] = `ls -sl -type "transform"`;
    int $selSize = size($sel);
    if( $selSize != 2 && $selSize != 4)
        error "Invalid selection length. Select 2 or 4 transforms ([squash, stretch], orig, target).";
    // assign
    string $squashShape[], $stretchShape[], $origShape[], $targetShape[];
    if( $selSize == 4 ){
        $squashShape = `listRelatives -children $sel[0]`;
        $stretchShape = `listRelatives -children $sel[1]`;
        $origShape = `listRelatives -children $sel[2]`;
        $targetShape = `listRelatives -children $sel[3]`;
    }else{
        $origShape = `listRelatives -children $sel[0]`;
        $targetShape = `listRelatives -children $sel[1]`;
    }
    // deformer
    string $def[] = `deformer -type "prHeatDeformer" $targetShape`;
    // attrs
    setAttr -type "string" ($targetShape[0]+".displayColorChannel") "None";
    setAttr ($targetShape[0]+".displayColors") 1;
    setAttr ($def[0]+".displayColors") 1;
    setAttr ($def[0]+".deformationType") 1;
    // connections
    connectAttr ($def[0]+".displayColors") ($targetShape[0]+".displayColors");
    connectAttr ($origShape[0]+".outMesh") ($def[0]+".origMesh");
    if( $selSize == 4 )
    {
        connectAttr ($squashShape[0]+".outMesh") ($def[0]+".squashMesh");
        connectAttr ($stretchShape[0]+".outMesh") ($def[0]+".stretchMesh");
    }
    select `listRelatives -p $targetShape[0]`;
    select -addFirst $def[0] ;
    return $def[0];
};
''')
