#include "prHeatDeformer.h"

// ----------------------------------
// Variables
// ----------------------------------
// default
MTypeId prHeatDeformer::id( 0x0010A51C );// from Filmakademie, not written in their wiki
// code
MObject prHeatDeformer::aDebug;
// setup
MObject prHeatDeformer::aScale;
MObject prHeatDeformer::aDeformationScale;
// perMesh geo
MObject prHeatDeformer::aOrigMesh;
MObject prHeatDeformer::aSquashMesh;
MObject prHeatDeformer::aStretchMesh;
// perMesh maps
MObject prHeatDeformer::aMultiplyHeatMap;
MObject prHeatDeformer::aMultiplyHeatSquashMap;
MObject prHeatDeformer::aMultiplyHeatStretchMap;
MObject prHeatDeformer::aMaxHeatSquashMap;
MObject prHeatDeformer::aMaxHeatStretchMap;
// perMesh
MObject prHeatDeformer::aPerGeometry;
// deformation type
MObject prHeatDeformer::aDeformationTitle;
MObject prHeatDeformer::aDeformationType;
MObject prHeatDeformer::aSmoothDeformationIterations;
MObject prHeatDeformer::aSmoothDeformationStrength;
MObject prHeatDeformer::aTangentSpace;
// heat / algorithm
MObject prHeatDeformer::aHeatTitle;
MObject prHeatDeformer::aDisplayColors;
MObject prHeatDeformer::aColorBase;
MObject prHeatDeformer::aColorSquash;
MObject prHeatDeformer::aColorStretch;
MObject prHeatDeformer::aMeasureTypeHeat;
MObject prHeatDeformer::aMultiplyHeat;
MObject prHeatDeformer::aMultiplyHeatSquash;
MObject prHeatDeformer::aMultiplyHeatStretch;
MObject prHeatDeformer::aMaxHeat;
MObject prHeatDeformer::aMaxHeatSquash;
MObject prHeatDeformer::aMaxHeatStretch;
MObject prHeatDeformer::aGrowHeat;
MObject prHeatDeformer::aGrowHeatSquash;
MObject prHeatDeformer::aGrowHeatStretch;
MObject prHeatDeformer::aSmoothHeatIterations;
MObject prHeatDeformer::aSmoothHeatStrength;

// ==================================
// DEFORM
// ==================================
MStatus prHeatDeformer::deform(MDataBlock& block, MItGeometry& iter, const MMatrix& mat, unsigned int idx)
{
	MStatus stat;
	// ###########################################################################################
	// GET ATTRIBUTES
	// ###########################################################################################
	// debug
	short sDebug = block.inputValue( aDebug ).asShort();
	if( sDebug == 2 )
		MGlobal::displayInfo( "Debug: --------------------" );
	// envelope
	float fEnvelope = block.inputValue( envelope, &stat ).asFloat();
	if( fEnvelope == 0.0 )
	{
		if( sDebug == 2 )
			MGlobal::displayInfo( "Debug: Return because of envelope 0.0" );
		return stat;
	}
	// openMP
	MThreadUtils::syncNumOpenMPThreads();
	
	// aScale
	float fScale = block.inputValue( aScale ).asFloat();
	
	// inputGeometry
	MArrayDataHandle ahInput = block.outputArrayValue( input );
    ahInput.jumpToElement( idx );
	MObject oInputGeom = ahInput.outputValue().child( inputGeom ).asMesh();
    MFnMesh fnCurrent( oInputGeom );
	// perGeometry
	MArrayDataHandle ahPerGeometry = block.inputArrayValue( aPerGeometry );
	stat = jumpToElement( ahPerGeometry, idx );
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	MDataHandle hPerGeometry = ahPerGeometry.inputValue();
	// ----------------------------------
	// DEFORMATION
	// ----------------------------------
	// aScaleDeformation
	float fScaleDeformation = block.inputValue( aDeformationScale ).asFloat();
	// aDeformationType
	short sDeformationType = block.inputValue( aDeformationType ).asShort();
	// aSmoothDeformationIterations
	int iSmoothDeformationIterations = block.inputValue( aSmoothDeformationIterations ).asInt();
	// aStrengthSmoothDeformation
	float fSmoothDeformationStrength = block.inputValue( aSmoothDeformationStrength ).asFloat();
	// aTangentSpace
	short sTangentSpace = block.inputValue( aTangentSpace ).asShort();

	// ----------------------------------
	// HEAT
	// ----------------------------------
	// aDisplayColors aColorBase aColorSquash aColorStretch
	bool bDisplayColors = block.inputValue( aDisplayColors ).asBool();
	MFloatVector fvColorBase;
	MFloatVector fvColorSquash;
	MFloatVector fvColorStretch;
	if( bDisplayColors == true )
	{
		fvColorBase = block.inputValue( aColorBase ).asFloatVector();
		fvColorSquash = block.inputValue( aColorSquash ).asFloatVector();
		fvColorStretch = block.inputValue( aColorStretch ).asFloatVector();
	}
	// aMeasureTypeHeat
	short sMeasureTypeHeat = block.inputValue( aMeasureTypeHeat ).asShort();
	// aMultiplyHeat aMultiplyHeatSquash aMultiplyHeatStretch
	float fMultHeat = block.inputValue( aMultiplyHeat ).asFloat();
    float fMultHeatSquash = block.inputValue( aMultiplyHeatSquash ).asFloat();
    float fMultHeatStretch = block.inputValue( aMultiplyHeatStretch ).asFloat();
    if( fMultHeat == 0.0 || fMultHeatSquash == 0.0 && fMultHeatStretch == 0.0 )
        return stat;
	// aMaxHeat aMaxHeatSquash aMaxHeatStretch
	bool bMaxHeat = block.inputValue( aMaxHeat ).asBool();
	float fSquashMaxHeat = block.inputValue( aMaxHeatSquash ).asFloat() * -1;
	float fStretchMaxHeat = block.inputValue( aMaxHeatStretch ).asFloat();
	if( fSquashMaxHeat == 0.0 && fStretchMaxHeat == 0.0 )
	{
		if( sDebug == 2 )
			MGlobal::displayInfo( "Debug: Return because fSquashMaxHeat == 0.0 && fStretchMaxHeat == 0.0" );
		return stat;
	}
	// aGrowHeat aSquashGrowHeat aStretchGrowHeat
	unsigned int iGrowHeat = block.inputValue( aGrowHeat ).asInt();
	unsigned int iGrowHeatSquash = block.inputValue( aGrowHeatSquash ).asInt() + iGrowHeat;
	unsigned int iGrowHeatStretch = block.inputValue( aGrowHeatStretch ).asInt() + iGrowHeat;
	// aSmoothHeatIterations
	unsigned int iSmoothHeatIterations = block.inputValue( aSmoothHeatIterations ).asInt();
	// aSmoothHeatStrength
	float fSmoothHeatStrength = block.inputValue( aSmoothHeatStrength ).asFloat();

	// ###########################################################################################
	// get all points and vertex IDs for this call
	// ###########################################################################################
	// membership handle
	MIntArray& membership = membership_[idx];
	unsigned int oldMembershipLength = membership.length();
	membership.clear();
	// get all points
	MPointArray points;
	iter.allPositions( points );
	// get all vertex ids in membership
	for( iter.reset(); !iter.isDone(); iter.next() )
		membership.append( iter.index() );
	// check dirty membership
	if( oldMembershipLength != membership.length() )
		initialized_[idx] = false;
	// check for initialize
	if( !initialized_[idx] )
	{
		dirtyMap_[idx] = true;
		dirtyOrigMesh_[idx] = true;
		dirtySquashMesh_[idx] = true;
		dirtyStretchMesh_[idx] = true;
	}

	// ###########################################################################################
	// INITIALIZE AND ORIG MESH
	// ###########################################################################################
	// handles
	MPointArray& origPoints = origPoints_[idx];
	MDoubleArray& origConnectedEdgeLengths = origConnectedEdgeLengths_[idx];
	MDoubleArray& origConnectedFaceAreas = origConnectedFaceAreas_[idx];
	double& dAverageEdgeLength = dAverageEdgeLength_[idx];
	MMatrixArray& origTangentSpaces = origTangentSpaces_[idx];
	std::map<unsigned int, MIntArray>& connectedVertices = connectedVertices_[idx];
	std::map<unsigned int, MIntArray>& connectedEdges = connectedEdges_[idx];
	std::map<unsigned int, MIntArray>& connectedFaces = connectedFaces_[idx];
	// reload
	if( dirtyOrigMesh_[idx] )
	{
		// orig mesh handle/object/functionset
		MDataHandle hOrigMesh = hPerGeometry.child( aOrigMesh );
		MObject oOrigMesh = hOrigMesh.asMesh();
		if( oOrigMesh.isNull() )
		{
			if( sDebug >= 1 )
				MGlobal::displayInfo( "Warning: Return because of missing origMesh input" );
            return stat;
		}
		MFnMesh fnOrigMesh( oOrigMesh );
		// get connected vertexIds, edgeIds, faceIds
		if( !initialized_[idx] )
		{
			MItMeshVertex itMeshVertexOrigMesh( oOrigMesh );
			connectedVertices.clear();
			connectedEdges.clear();
			connectedFaces.clear();
			for( unsigned int i = 0; i < membership.length(); i++ )
			{
				int oldIndex = itMeshVertexOrigMesh.index();
				itMeshVertexOrigMesh.setIndex( membership[i], oldIndex );
				itMeshVertexOrigMesh.getConnectedVertices( connectedVertices[i] );
				// store neighbor ids as membership positions
				MIntArray iaRemoveNeighbors;
				for( unsigned int j = 0; j < connectedVertices[i].length(); j++ )
				{
					connectedVertices[i][j] = binarySearch( membership, connectedVertices[i][j] );
					if( connectedVertices[i][j] == -1 )
						iaRemoveNeighbors.insert( j, 0 );
				}
				// remove neighbors that are not in membership
				for( unsigned int j = 0; j < iaRemoveNeighbors.length(); j++ )
					connectedVertices[i].remove( iaRemoveNeighbors[j] );
				// get edges and faces
				itMeshVertexOrigMesh.getConnectedEdges( connectedEdges[i] );
				itMeshVertexOrigMesh.getConnectedFaces( connectedFaces[i] );
			}
			if( sDebug == 2 )
				MGlobal::displayInfo( MString("Debug: Initialized with origMesh ") );
		}
		// orig mesh points
		origPoints.clear();
		fnOrigMesh.getPoints( origPoints );
		// orig mesh normals
		MFloatVectorArray fvaOrigNormals;
		fnOrigMesh.getVertexNormals( false, fvaOrigNormals );
		// orig mesh edgeLengths
		MDoubleArray origEdgeLengths;
		MItMeshEdge itEdgeOrig( oOrigMesh );
		dAverageEdgeLength = 0.0;
		for( itEdgeOrig.reset(); !itEdgeOrig.isDone(); itEdgeOrig.next() )
		{
			double eachEdgeLength;
			itEdgeOrig.getLength( eachEdgeLength );
			origEdgeLengths.append( eachEdgeLength );
			dAverageEdgeLength += eachEdgeLength;
		}
		dAverageEdgeLength /= itEdgeOrig.count();
		// orig mesh face areas
		MDoubleArray origFaceAreas;
		MItMeshPolygon itPolyOrig( oOrigMesh );
		for( itPolyOrig.reset(); !itPolyOrig.isDone(); itPolyOrig.next() )
		{
			double eachFaceArea;
			itPolyOrig.getArea( eachFaceArea );
			origFaceAreas.append( eachFaceArea );
		}
		// orig mesh edgeLengthSums, faceAreaSums, tangent spaces
		origConnectedEdgeLengths.setLength( membership.length() );
		origConnectedFaceAreas.setLength( membership.length() );
		origTangentSpaces.setLength( membership.length() );

		for( unsigned int i = 0; i < membership.length(); i++ )
		{
			// edge
			origConnectedEdgeLengths[i] = 0.0;
			for( unsigned int j = 0; j < connectedEdges[i].length(); j++ )
				origConnectedEdgeLengths[i] += origEdgeLengths[connectedEdges[i][j]];
			// area
			origConnectedFaceAreas[i] = 0.0;
			for( unsigned int j = 0; j < connectedFaces[i].length(); j++ )
				origConnectedFaceAreas[i] += origFaceAreas[connectedFaces[i][j]];
			// tangent
			origTangentSpaces[i] = getTangentSpace( fnOrigMesh, membership[i], connectedFaces[i], fvaOrigNormals[membership[i]], sTangentSpace );
		}
		// finish
		initialized_[idx] = true;
		dirtyOrigMesh_[idx] = false;
		dirtySquashMesh_[idx] = true;// to force recalculation of blendShape vectors
		dirtyStretchMesh_[idx] = true;// to force recalculation of blendShape vectors
		if( sDebug == 2 )
			MGlobal::displayInfo( "Debug: Updated aOrigMesh" );
	}

	// ###########################################################################################
	// MAPS
	// ###########################################################################################
	// handles
	MFloatArray& weights = weights_[idx];
	MFloatArray& multiplyHeatMap = multiplyHeatMap_[idx];
	MFloatArray& multiplyHeatSquashMap = multiplyHeatSquashMap_[idx];
	MFloatArray& multiplyHeatStretchMap = multiplyHeatStretchMap_[idx];
	MFloatArray& maxHeatSquashMap = maxHeatSquashMap_[idx];
	MFloatArray& maxHeatStretchMap = maxHeatStretchMap_[idx];
	// reload maps
	if( dirtyMap_[idx] )
	{
		// map lengths
		weights.setLength( membership.length() );
		multiplyHeatMap.setLength( membership.length() );
		multiplyHeatSquashMap.setLength( membership.length() );
		multiplyHeatStretchMap.setLength( membership.length() );
		maxHeatSquashMap.setLength( membership.length() );
		maxHeatStretchMap.setLength( membership.length() );
		// get handles to maps
		MArrayDataHandle ahMultiplyHeatMap = hPerGeometry.child( aMultiplyHeatMap );
		MArrayDataHandle ahMultiplyHeatSquashMap = hPerGeometry.child( aMultiplyHeatSquashMap );
		MArrayDataHandle ahMultiplyHeatStretchMap = hPerGeometry.child( aMultiplyHeatStretchMap );
		MArrayDataHandle ahMaxHeatSquashMap = hPerGeometry.child( aMaxHeatSquashMap );
		MArrayDataHandle ahMaxHeatStretchMap = hPerGeometry.child( aMaxHeatStretchMap );
		
		// read new values
		for( unsigned int i = 0; i < membership.length(); i++ )
		{
			// weights
			weights[i] = weightValue( block, idx, membership[i] );
			// maps
			stat = jumpToElement(ahMultiplyHeatMap, membership[i] );
			CHECK_MSTATUS_AND_RETURN_IT(stat);
			multiplyHeatMap[i] = ahMultiplyHeatMap.inputValue().asFloat();
			
			stat = jumpToElement(ahMultiplyHeatSquashMap, membership[i] );
			CHECK_MSTATUS_AND_RETURN_IT(stat);
			multiplyHeatSquashMap[i] = ahMultiplyHeatSquashMap.inputValue().asFloat();
			
			stat = jumpToElement(ahMultiplyHeatStretchMap, membership[i] );
			CHECK_MSTATUS_AND_RETURN_IT(stat);
			multiplyHeatStretchMap[i] = ahMultiplyHeatStretchMap.inputValue().asFloat();
			
			stat = jumpToElement(ahMaxHeatSquashMap, membership[i] );
			CHECK_MSTATUS_AND_RETURN_IT(stat);
			maxHeatSquashMap[i] = ahMaxHeatSquashMap.inputValue().asFloat();
			
			stat = jumpToElement(ahMaxHeatStretchMap, membership[i] );
			CHECK_MSTATUS_AND_RETURN_IT(stat);
			maxHeatStretchMap[i] = ahMaxHeatStretchMap.inputValue().asFloat();
		}
		// finish
		dirtyMap_[idx] = false;
		if( sDebug == 2 )
			MGlobal::displayInfo( "Debug: Updated maps" );
	}
	
	// ###########################################################################################
	// BLENDSHAPE VECTORS
	// ###########################################################################################
	// ----------------------------------
	// aSquashMesh
	// ----------------------------------
	// handles
	MVectorArray& squashVectors = squashVectors_[idx];
	// reload
	if( dirtySquashMesh_[idx] )
	{
		// aSquashMesh
		MDataHandle hSquashMesh = hPerGeometry.child( aSquashMesh );
		MObject oSquashMesh = hSquashMesh.asMesh();
		if( oSquashMesh.isNull() )
		{
			initialized_[idx] = false;
			if( sDebug >= 1 )
				MGlobal::displayInfo( "Warning: Skipped because of missing aSquashMesh input" );
			return stat;
		}
		MFnMesh fnSquashMesh( oSquashMesh );
		// get points
		MPointArray paSquashMeshPoints;
		fnSquashMesh.getPoints( paSquashMeshPoints );
		// calculate vectors
		squashVectors.setLength( membership.length() );
		for( unsigned int i = 0; i < membership.length(); i++ )
		{
			squashVectors[i] = paSquashMeshPoints[membership[i]] - origPoints[membership[i]];
		}
		// finish
		dirtySquashMesh_[idx] = false;
		if( sDebug == 2 )
			MGlobal::displayInfo( "Debug: Updated aSquashMesh vectors" );
	}
	// ----------------------------------
	// aStretchMesh
	// ----------------------------------
	// handles
	MVectorArray& stretchVectors = stretchVectors_[idx];
	// reload
	if( dirtyStretchMesh_[idx] )
	{
		// aStretchMesh
		MDataHandle hStretchMesh = hPerGeometry.child( aStretchMesh );
		MObject oStretchMesh = hStretchMesh.asMesh();
		if( oStretchMesh.isNull() )
		{
			initialized_[idx] = false;
			if( sDebug >= 1 )
				MGlobal::displayInfo( "Warning: Skipped because of missing aStretchMesh input" );
			return stat;
		}
		MFnMesh fnStretchMesh( oStretchMesh );
		// get points
		MPointArray paStretchMeshPoints;
		fnStretchMesh.getPoints( paStretchMeshPoints );
		// calculate vectors
		stretchVectors.setLength( membership.length() );
		for( unsigned int i = 0; i < membership.length(); i++ )
		{
			stretchVectors[i] = paStretchMeshPoints[membership[i]] - origPoints[membership[i]];
		}
		// finish
		dirtyStretchMesh_[idx] = false;
		if( sDebug == 2 )
			MGlobal::displayInfo( "Debug: Updated aStretchMesh vectors" );
	}

	// ###########################################################################################
	// per call attribute reading
	// ###########################################################################################
	// current normals
	MFloatVectorArray currentNormals;
	if( sDeformationType == 1 || sDeformationType == 2 && sTangentSpace > 0 )
		fnCurrent.getVertexNormals( false, currentNormals );
	
	// current tangent spaces (9902 verts: from 35.5 to 21.5)// 25 to 14
	MMatrixArray currentTangentSpaces;
	if( sDeformationType == 2 && sTangentSpace > 0 )
	{
		currentTangentSpaces.setLength( membership.length() );
		//#ifdef _OPENMP
		//#pragma omp parallel for
		//#endif
		for( int i = 0; i < (int)membership.length(); i++ )
		{
			currentTangentSpaces[i] = getTangentSpace( fnCurrent, membership[i], connectedFaces[i], currentNormals[membership[i]], sTangentSpace );
		}
	}
	
	// current mesh face areas (9902 verts: from 26.4 to 22.0 /or/ 50.5 to 26.0)
	MDoubleArray currentConnectedFaceAreas;
	if( sMeasureTypeHeat == 0 )
	{
		MDoubleArray currentFaceAreas;
		MItMeshPolygon itPolyCurrent( oInputGeom );
		for( itPolyCurrent.reset(); !itPolyCurrent.isDone(); itPolyCurrent.next() )
		{
			double eachFaceArea;
			itPolyCurrent.getArea( eachFaceArea );
			currentFaceAreas.append( eachFaceArea / (fScale*fScale) );
		}
		// sum
		for( unsigned int i = 0; i < membership.length(); i++ )
		{
			currentConnectedFaceAreas.append( 0.0 );
			for( unsigned int j = 0; j < connectedFaces[i].length(); j++ )
				currentConnectedFaceAreas[i] += currentFaceAreas[connectedFaces[i][j]];
		}
	}

	// current mesh edgeLengths
	MDoubleArray currentConnectedEdgeLengths;
	if( sMeasureTypeHeat == 1 )
	{
		MDoubleArray currentEdgeLengths;
		MItMeshEdge itEdgeCurrent( oInputGeom );
		for( itEdgeCurrent.reset(); !itEdgeCurrent.isDone(); itEdgeCurrent.next() )
		{
			double eachEdgeLength;
			itEdgeCurrent.getLength( eachEdgeLength );
			currentEdgeLengths.append( eachEdgeLength / fScale );
		}
		// sum
		for( unsigned int i = 0; i < membership.length(); i++ )
		{
			currentConnectedEdgeLengths.append( 0.0 );
			for( unsigned int j = 0; j < connectedEdges[i].length(); j++ )
				currentConnectedEdgeLengths[i] += currentEdgeLengths[connectedEdges[i][j]];
		}
	}
	
	

	// ###########################################################################################
	// ALGORITHM
	// ###########################################################################################
	// ==================================
    // Heat Calculation 
    // ==================================
    // input: points, face areas, edge lengths, multiplyHeat, maxHeat
    // output: daHeat {1.0, -1.0, 0.0, ...}
    //
    // eachHeat =-1.0 // origLength*0 // squashed
    // eachHeat = 0.0 // origLength*1 // default
    // eachHeat = 1.0 // origLength*2 // stretched
    MDoubleArray daHeat;
	daHeat.setLength( points.length() );
	for( unsigned int i=0; i<points.length(); i++ )
	{
		double eachHeat = 0.0;
		// face area
		if( sMeasureTypeHeat == 0 )
			eachHeat = ( currentConnectedFaceAreas[i] - origConnectedFaceAreas[i] ) / origConnectedFaceAreas[i];
		// edge length
		else if( sMeasureTypeHeat == 1 ) 
			eachHeat = ( currentConnectedEdgeLengths[i] - origConnectedEdgeLengths[i] ) / origConnectedEdgeLengths[i];
        // squash heat modification
        if( eachHeat < 0.0 )
		{
            eachHeat *= fMultHeatSquash * multiplyHeatSquashMap[i] * fMultHeat * multiplyHeatMap[i];
            if( bMaxHeat && (eachHeat < fSquashMaxHeat*maxHeatSquashMap[i]) )
                eachHeat = fSquashMaxHeat*maxHeatSquashMap[i];
		}
		// stretch heat modification
		else if( eachHeat > 0.0 )
		{
            eachHeat *= fMultHeatStretch * multiplyHeatStretchMap[i] * fMultHeat * multiplyHeatMap[i];
            if( bMaxHeat && (eachHeat > fStretchMaxHeat*maxHeatStretchMap[i] ) )
                eachHeat = fStretchMaxHeat*maxHeatStretchMap[i];
		}
        // store
        daHeat[i] = eachHeat;
	}
	
	// ==================================
    // Heat Grow
    // ==================================
    if( iGrowHeatSquash > 0 || iGrowHeatStretch > 0 )
	{
        // find iteration count
        unsigned int iGrowIterations = iGrowHeatSquash;
        if( iGrowHeatStretch > iGrowIterations )
            iGrowIterations = iGrowHeatStretch;
		if( sDebug == 2 )
			MGlobal::displayInfo( MString("Debug: iGrowIterations ")+iGrowIterations );
        // grow loop
        for( unsigned int i=0; i<iGrowIterations; i++ )
		{
            MDoubleArray daHeatNew(daHeat);
            // loop through effected points;
            for( unsigned int j=0; j<points.length(); j++ )
			{
                double dStrongestSquash = daHeatNew[j];
                double dStrongestStretch = daHeatNew[j];
				
                // loop over neighbors to find strongest squash/stretch
				for( unsigned int k=0; k < connectedVertices[j].length(); k++ )
				{
                    double eachNeighborHeat = daHeat[connectedVertices[j][k]];
                    if( eachNeighborHeat < dStrongestSquash )
                        dStrongestSquash = eachNeighborHeat;
                    if( eachNeighborHeat > dStrongestStretch )
                        dStrongestStretch = eachNeighborHeat;
				}
                // grow squash and stretch
                if( iGrowHeatSquash > i && iGrowHeatStretch > i )
				{
                    double newValue = 0.0;
                    if( dStrongestSquash < 0.0 )
                        newValue = dStrongestSquash;
                    if( dStrongestStretch > 0.0 )
                        newValue += dStrongestStretch;
                    if( newValue != 0.0 )
                        daHeatNew[j] = newValue;
				}
				// grow squash only
                else if( iGrowHeatSquash > i && dStrongestSquash < 0.0 )
				{
                    if( daHeatNew[j] > 0.0 )
                        daHeatNew[j] += dStrongestSquash;
                    else
                         daHeatNew[j] = dStrongestSquash;
				}
				// grow stretch only
                else if( iGrowHeatStretch > i && dStrongestStretch > 0.0 )
				{
                    if( daHeatNew[j] < 0.0 )
                        daHeatNew[j] += dStrongestStretch;
                    else
                        daHeatNew[j] = dStrongestStretch;
				}
			}
            daHeat = daHeatNew;
		}
	}
	
	// ==================================
	// Heat Smooth
	// ==================================
	// input: daHeat
	// output: daHeat
	if( sDebug == 2 && iSmoothHeatIterations > 0 )
		MGlobal::displayInfo( MString("Debug: iSmoothHeatIterations ")+iSmoothHeatIterations );
	for( unsigned int i=0; i < iSmoothHeatIterations; i++ )
	{
		MDoubleArray daHeatNew(daHeat);
		for( unsigned int j=0; j<points.length(); j++ )
		{
			double dNeighborAvrg = 0.0;
			for( unsigned k=0; k < connectedVertices[j].length(); k++ )
				dNeighborAvrg += daHeat[connectedVertices[j][k]];
			dNeighborAvrg /= connectedVertices[j].length();
			daHeatNew[j] = daHeatNew[j]*(1.0-fSmoothHeatStrength) + dNeighborAvrg*fSmoothHeatStrength;
		}
		daHeat = daHeatNew;
	}
	
	// ==================================
	// Heat Display
	// ==================================
	// input daHeat
	// result vertexColors
	if( bDisplayColors )
	{
		MColorArray caColors;
		MIntArray iaIndexList;
		for( unsigned int i=0; i < points.length(); i++ )
		{
			// colorBase colorStretch colorSquash
			MFloatVector fvEachColor(fvColorBase);
			if( daHeat[i] > 0.0 )
				fvEachColor += (fvColorStretch - fvEachColor)*( (float)daHeat[i] );
			else if( daHeat[i] < 0.0 )
				fvEachColor += (fvColorSquash - fvEachColor)*( (float)daHeat[i]*-1 );
			MColor cEachColor( fvEachColor.x, fvEachColor.y, fvEachColor.z, 1.0 );
			caColors.append( cEachColor );
			iaIndexList.append( membership[i] );
			//fnCurrent.setVertexColor( cEachColor, membership[i] )// (setting all at once is faster)
		}
		fnCurrent.setVertexColors( caColors, iaIndexList );
		if( sDebug == 2 )
			MGlobal::displayInfo( "Debug: Show colors" );
	}
	
	// ==================================
    // Deformation Calculation
    // ==================================
    // input heatArray
    // output motionVectorArray
    MVectorArray vaVectors;
	for( unsigned int i=0; i < points.length(); i++ )
	{
        MVector vMove;
        // skip calculation for 0.0 heat
        if( daHeat[i] == 0.0 )
		{
            vaVectors.append( vMove );
            continue;
		}
        
        // ----------------------------------
        // Normal
        // ----------------------------------
        if( sDeformationType == 1 )
            vMove += currentNormals[membership[i]] * (float)(daHeat[i]*-1) * (float)dAverageEdgeLength * fScaleDeformation * fScale;// float cast to prevent warning
		
        // ----------------------------------
        // BlendShape
        // ----------------------------------
        else if( sDeformationType == 2 )
		{
            if( daHeat[i] < 0.0 )
                vMove = squashVectors[i] * (daHeat[i]*-1) * fScaleDeformation * fScale;
            else if( daHeat[i] > 0.0 )
                vMove = stretchVectors[i] * daHeat[i] * fScaleDeformation * fScale;
            // tangent spaces
            if( sTangentSpace > 0 )
                vMove *= origTangentSpaces[i].inverse() * currentTangentSpaces[i];
		}
        // save vector
        vaVectors.append( vMove );
	}
	
	// ==================================
    // Deformation Smooth
    // ==================================
    // input: motionVectorArray
    // result: motionVectorArray
	if( sDebug == 2 && iSmoothDeformationIterations > 0 )
		MGlobal::displayInfo( MString("Debug: iSmoothDeformationIterations ")+iSmoothDeformationIterations );
	for( int i=0; i < iSmoothDeformationIterations; i++ )
	{
        MVectorArray vaVectorsNew(vaVectors);
		//#ifdef _OPENMP
		//#pragma omp parallel for
		//#endif
		for( unsigned int j=0; j<points.length(); j++ )
		{
            MVector vNeighborAverage;
			for( unsigned int k=0; k < connectedVertices[j].length(); k++ )
				vNeighborAverage += vaVectors[connectedVertices[j][k]];
			if( connectedVertices[j].length() > 0 )
			{
				vNeighborAverage /= connectedVertices[j].length();
				vaVectorsNew[j] = vaVectors[j]*(1.0-fSmoothDeformationStrength) + vNeighborAverage*fSmoothDeformationStrength;
			}
		}
		vaVectors = vaVectorsNew;
	}
	
    // ==================================
    // Deformation
    // ==================================
    // input motionVectorArray, weights
    // result deformed mesh

	//iter.allPositions( points );
	unsigned int i = 0;
	for( iter.reset(); !iter.isDone(); iter.next(), i++ )
		iter.setPosition( points[i] + vaVectors[i] * weights[i] * fEnvelope );
	// 
	return stat;
}

// ----------------------------------
// CUSTOM FUNCTIONS
// ----------------------------------
MStatus prHeatDeformer::getInputMesh( MDataBlock& block, unsigned int idx, MObject* oInputMesh )
{
	MStatus stat;
	MArrayDataHandle hInput = block.outputArrayValue( input, &stat );
	CHECK_MSTATUS_AND_RETURN_IT( stat );
	hInput.jumpToElement( idx );
	MDataHandle hInputGeom = hInput.outputValue().child( inputGeom );
	*oInputMesh = hInputGeom.asMesh();
	return stat;
}

MStatus prHeatDeformer::jumpToElement(MArrayDataHandle& ahArray, unsigned int idx) {
	MStatus stat;
	stat = ahArray.jumpToElement(idx);
	if (MFAIL(stat)) 
	{
		MArrayDataBuilder builder = ahArray.builder(&stat);
		CHECK_MSTATUS_AND_RETURN_IT(stat);
		builder.addElement(idx, &stat);
		CHECK_MSTATUS_AND_RETURN_IT(stat);
		stat = ahArray.set(builder);
		CHECK_MSTATUS_AND_RETURN_IT(stat);
		stat = ahArray.jumpToElement(idx);
		CHECK_MSTATUS_AND_RETURN_IT(stat);
	}
	return stat;
}

MMatrix prHeatDeformer::getTangentSpace( MFnMesh& fnCurrentMesh, unsigned int iVertexId, MIntArray iFaceIds, MFloatVector& fvVertexNormal, short sTangentCalculation )
{
	/*
	return tangent space matrix of given iVertexId on given MFnMesh
	bSimple: 0=default (full), 1=simple (use only one tangent vector to improve performance)
	*/
    //
    // tangent
    MVector vTan;
    MVector vTmp;
	for( unsigned int i = 0; i < iFaceIds.length(); i++ )
	{	
		fnCurrentMesh.getFaceVertexTangent( iFaceIds[i], iVertexId, vTmp, MSpace::kObject );
        vTan += vTmp;
		// only one tangent for simple case
        if( sTangentCalculation == 1 )// at 9902 vertices from 20.3 to 21.2 fps
            break;
	}
	if( sTangentCalculation != 1 )
		vTan /= iFaceIds.length();
    
	// binormal from MFnMesh (slow)
    //vBin = om.MVector()
    //for eachFaceId in iFaceIds:
    //    fnCurrentMesh.getFaceVertexBinormal( eachFaceId, iVertexId, vTmp, om.MSpace.kObject )
    //    vBin += vTmp
    //vBin /= len(iFaceIds)
	
    // binormal from cross-product (faster)
    MVector vBin( vTan^fvVertexNormal );
    // matrix
	const double daTangentMatrix[4][4] = {
		vTan.x,  vTan.y,  vTan.z,  0.0,
		fvVertexNormal.x, fvVertexNormal.y, fvVertexNormal.z, 0.0,
        vBin.x,  vBin.y,  vBin.z,  0.0,
		0.0,     0.0,     0.0,     1.0 };
    MMatrix mTangent( daTangentMatrix );
    return mTangent;
}

int prHeatDeformer::binarySearch( MIntArray iaSorted, int iToLookFor )
{
	// return given int in intArray and return position (int array should be sorted and with unique values)
	int iFirst = 0;
	int iLast = iaSorted.length() - 1;
	int iLocation;
	while( iFirst <= iLast )
	{
		iLocation = (iFirst+iLast) / 2;
		if( iaSorted[iLocation] == iToLookFor )
			return iLocation;
		else if( iaSorted[iLocation] < iToLookFor )
			iFirst = iLocation+1;
		else if( iaSorted[iLocation] > iToLookFor )
			iLast = iLocation-1;
	}
	return -1;
}

// ----------------------------------
// MPX FUNCTIONS
// ----------------------------------
MStatus prHeatDeformer::setDependentsDirty( const MPlug& plug, MPlugArray &plugArray )
{
	// ----------------------------------
	// check if weight map or geo are dirty, to only get data from them if necessary 
	// ----------------------------------
	// maps
	if( plug == weights || 
		plug == aMultiplyHeatMap || plug == aMultiplyHeatSquashMap || plug == aMultiplyHeatStretchMap || 
		plug == aMaxHeatSquashMap || plug == aMaxHeatStretchMap )
	{
		unsigned int idx = 0;
		if( plug.isArray() )
			idx = plug.parent().logicalIndex();
		else
			idx = plug.array().parent().logicalIndex();
		dirtyMap_[idx] = true;
	}
	// aOrigMesh
	else if( plug == aOrigMesh )
	{
		unsigned int idx = plug.parent().logicalIndex();
		dirtyOrigMesh_[idx] = true;
	}
	// aSquashMesh
	else if( plug == aSquashMesh )
	{
		unsigned int idx = plug.parent().logicalIndex();
		dirtySquashMesh_[idx] = true;
	}
	// aStretchMesh
	else if( plug == aStretchMesh )
	{
		unsigned int idx = plug.parent().logicalIndex();
		dirtyStretchMesh_[idx] = true;
	}
	// deformationType
	else if( plug == aDeformationType )
	{
		unsigned int idx = plug.parent().logicalIndex();
		dirtySquashMesh_[idx] = true;
		dirtyStretchMesh_[idx] = true;
	}
	return MS::kSuccess;
}

void prHeatDeformer::postConstructor()
{
	setDeformationDetails( MPxDeformerNode::kDeformsColors );
}

MStatus prHeatDeformer::initialize()
{
	// variables
	MStatus stat;

	MFnTypedAttribute tAttr;
	MFnNumericAttribute nAttr;
	MFnCompoundAttribute cAttr;
	MFnGenericAttribute gAttr;
	MFnEnumAttribute eAttr;

	// -----------------------
	// aDebug
	// -----------------------
	aDebug = eAttr.create( "debug", "debug", 1 );
	eAttr.setKeyable(true);
    eAttr.addField( "Off", 0 );
    eAttr.addField( "Warnings", 1 );
	eAttr.addField( "All", 2 );
    addAttribute( aDebug );

	// -----------------------
	// aScale
	// -----------------------
	aScale = nAttr.create( "scale", "scale", MFnNumericData::kFloat, 1.0, &stat);
	nAttr.setSoftMin( 0.001 );
	nAttr.setKeyable(true);
	addAttribute( aScale );
    stat = attributeAffects( aScale, prHeatDeformer::outputGeom );

	// -----------------------
	// perMesh geometry attributes
	// -----------------------
	// aOrigMesh
	aOrigMesh = gAttr.create( "origMesh", "origMesh", &stat );
	stat = gAttr.addDataAccept( MFnMeshData::kMesh );

	// aSquashMesh
	aSquashMesh = gAttr.create( "squashMesh", "squashMesh", &stat );
	stat = gAttr.addDataAccept( MFnMeshData::kMesh );

	// aStretchMesh
	aStretchMesh = gAttr.create( "stretchMesh", "stretchMesh", &stat );
	stat = gAttr.addDataAccept( MFnMeshData::kMesh );

	// -----------------------
	// perMesh map attributes
	// -----------------------
	// aMultiplyHeatMap
	aMultiplyHeatMap = nAttr.create( "multiplyHeatMap", "multiplyHeatMap", MFnNumericData::kFloat, 1.0, &stat);
	nAttr.setMin(0.0);
	nAttr.setMax(1.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);

	// aMultiplyHeatSquash
	aMultiplyHeatSquashMap = nAttr.create( "multiplyHeatSquashMap", "multiplyHeatSquashMap", MFnNumericData::kFloat, 1.0, &stat);
	nAttr.setMin(0.0);
	nAttr.setMax(1.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);

	// aMultiplyHeatStretch
	aMultiplyHeatStretchMap = nAttr.create( "multiplyHeatStretchMap", "multiplyHeatStretchMap", MFnNumericData::kFloat, 1.0, &stat);
	nAttr.setMin(0.0);
	nAttr.setMax(1.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);

	// aMaxHeatSquashMap
	aMaxHeatSquashMap = nAttr.create( "maxHeatSquashMap", "maxHeatSquashMap", MFnNumericData::kFloat, 1.0, &stat);
	nAttr.setMin(0.0);
	nAttr.setMax(1.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);

	// aMaxHeatStretchMap
	aMaxHeatStretchMap = nAttr.create( "maxHeatStretchMap", "maxHeatStretchMap", MFnNumericData::kFloat, 1.0, &stat);
	nAttr.setMin(0.0);
	nAttr.setMax(1.0);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);

	// -----------------------
	// aPerGeometry
	// -----------------------
	aPerGeometry = cAttr.create("perGeometry", "perGeometry", &stat);
	cAttr.setArray(true);
	stat = cAttr.addChild(aOrigMesh);
	stat = cAttr.addChild(aSquashMesh);
	stat = cAttr.addChild(aStretchMesh);
	stat = cAttr.addChild(aMultiplyHeatMap);
	stat = cAttr.addChild(aMultiplyHeatSquashMap);
	stat = cAttr.addChild(aMultiplyHeatStretchMap);
	stat = cAttr.addChild(aMaxHeatSquashMap);
	stat = cAttr.addChild(aMaxHeatStretchMap);
	stat = cAttr.setUsesArrayDataBuilder(true);
	stat = addAttribute(aPerGeometry);

	// attributeAffects (perMesh) has to come after addChild/addAttribute
	stat = attributeAffects( aOrigMesh, prHeatDeformer::outputGeom );
	stat = attributeAffects( aSquashMesh, prHeatDeformer::outputGeom );
	stat = attributeAffects( aStretchMesh, prHeatDeformer::outputGeom );
	stat = attributeAffects( aMultiplyHeatMap, prHeatDeformer::outputGeom );
	stat = attributeAffects( aMultiplyHeatSquashMap, prHeatDeformer::outputGeom );
	stat = attributeAffects( aMultiplyHeatStretchMap, prHeatDeformer::outputGeom );
	stat = attributeAffects( aMaxHeatSquashMap, prHeatDeformer::outputGeom );
	stat = attributeAffects( aMaxHeatStretchMap, prHeatDeformer::outputGeom );

	// -----------------------
    // deformation type (user);
    // -----------------------
	// aDeformationTitle
	aDeformationTitle = eAttr.create( "deformationTitle", "deformationTitle", 0 );
	eAttr.setNiceNameOverride( "DEFORMATION" );
    eAttr.setKeyable(false);
	eAttr.setChannelBox(true);
    eAttr.addField( "-", 0 );
    addAttribute( aDeformationTitle );

	// aDeformationScale
	aDeformationScale = nAttr.create( "deformationScale", "deformationScale", MFnNumericData::kFloat, 1.0, &stat);
	nAttr.setSoftMin( 0.001 );
	nAttr.setKeyable(true);
	addAttribute( aDeformationScale );
    stat = attributeAffects( aDeformationScale, prHeatDeformer::outputGeom );

	// aDeformationType
    aDeformationType = eAttr.create( "deformationType", "deformationType", 0 );
    eAttr.setKeyable(true);
    eAttr.addField( "None", 0 );
    eAttr.addField( "Normal Vector", 1 );
    eAttr.addField( "BlendShape", 2 );
    addAttribute( aDeformationType );
    attributeAffects(aDeformationType, prHeatDeformer::outputGeom);
    
    // aSmoothDeformationIterations
    aSmoothDeformationIterations = nAttr.create( "iterationsSmoothDeformer", "iterationsSmoothDeformer", MFnNumericData::kInt, 0 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0 );
    nAttr.setSoftMax( 5 );
    addAttribute( aSmoothDeformationIterations );
    attributeAffects(aSmoothDeformationIterations, prHeatDeformer::outputGeom);
    // aSmoothHeatStrength
    aSmoothDeformationStrength = nAttr.create( "strengthSmoothDeformer", "strengthSmoothDeformer", MFnNumericData::kFloat, 0.5 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0.0 );
    nAttr.setMax( 1.0 );
    addAttribute( aSmoothDeformationStrength );
    attributeAffects(aSmoothDeformationStrength, prHeatDeformer::outputGeom);
    
	// aTangentSpace
	aTangentSpace = eAttr.create( "blendShapeTangentSpace", "blendShapeTangentSpace", 2 );
    eAttr.setKeyable(true);
    eAttr.addField( "Off", 0 );
    eAttr.addField( "Simple", 1 );
    eAttr.addField( "Full", 2 );
    addAttribute( aTangentSpace );
    attributeAffects(aTangentSpace, prHeatDeformer::outputGeom);

	// -----------------------
	// Heat / algorithm
	// -----------------------
	// aHeatTitle
	aHeatTitle = eAttr.create( "heatTitle", "heatTitle", 0 );
	eAttr.setNiceNameOverride( "HEAT" );
    eAttr.setKeyable(false);
	eAttr.setChannelBox(true);
    eAttr.addField( "-", 0 );
    addAttribute( aHeatTitle );

	// aDisplayColors
	aDisplayColors = nAttr.create( "displayColors", "displayColors", MFnNumericData::kBoolean, 0, &stat );
	nAttr.setKeyable(true);
	addAttribute( aDisplayColors );
	attributeAffects(aDisplayColors, prHeatDeformer::outputGeom);
	// aColorBase
	aColorBase = nAttr.createColor( "colorBase", "colorBase", &stat );
	nAttr.setDefault( 0.122, 0.122, 0.122 );
	addAttribute( aColorBase );
	attributeAffects(aColorBase, prHeatDeformer::outputGeom);
	// aColorSquash;
	aColorSquash = nAttr.createColor( "colorSquash", "colorSquash", &stat );
	nAttr.setDefault( 1.0, 0.0, 0.0 );
	addAttribute( aColorSquash );
	attributeAffects(aColorSquash, prHeatDeformer::outputGeom);
	// aColorStretch
	aColorStretch = nAttr.createColor( "colorStretch", "colorStretch", &stat );
	nAttr.setDefault( 0.0, 1.0, 0.0 );
	addAttribute( aColorStretch );
	attributeAffects(aColorStretch, prHeatDeformer::outputGeom);

	// aMeasureTypeHeat
	aMeasureTypeHeat = eAttr.create( "measureTypeHeat", "measureTypeHeat", 0 );
    eAttr.setKeyable(true);
    eAttr.addField( "Face Area", 0 );
    eAttr.addField( "Edge Length", 1 );
    addAttribute( aMeasureTypeHeat );
    attributeAffects( aMeasureTypeHeat, prHeatDeformer::outputGeom );

	// aMultiplyHeat 
    aMultiplyHeat = nAttr.create( "multiplyHeat", "multiplyHeat", MFnNumericData::kFloat, 1.0 );
    nAttr.setSoftMin(0.0);
    nAttr.setKeyable(true);
    addAttribute( aMultiplyHeat );
	attributeAffects(aMultiplyHeat, prHeatDeformer::outputGeom);
    // aMultiplyHeatSquash
    aMultiplyHeatSquash = nAttr.create( "squashMultiplyHeat", "squashMultiplyHeat", MFnNumericData::kFloat, 1.0 );
    nAttr.setSoftMin(0.0);
    nAttr.setKeyable(true);
    addAttribute( aMultiplyHeatSquash );
    attributeAffects(aMultiplyHeatSquash, prHeatDeformer::outputGeom);
    // aMultiplyHeatStretch
    aMultiplyHeatStretch = nAttr.create( "stretchMultiplyHeat", "stretchMultiplyHeat", MFnNumericData::kFloat, 1.0 );
    nAttr.setSoftMin(0.0);
    nAttr.setKeyable(true);
    addAttribute( aMultiplyHeatStretch );
    attributeAffects(aMultiplyHeatStretch, prHeatDeformer::outputGeom);
    
    // aMaxHeat 
    aMaxHeat = nAttr.create( "maxHeat", "maxHeat", MFnNumericData::kBoolean, 1 );
    nAttr.setKeyable(true);
    addAttribute( aMaxHeat );
    attributeAffects(aMaxHeat, prHeatDeformer::outputGeom);
    // aMaxHeatSquash
    aMaxHeatSquash = nAttr.create( "squashMaxHeat", "squashMaxHeat", MFnNumericData::kFloat, 1.0 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0.0 );
    addAttribute( aMaxHeatSquash );
    attributeAffects(aMaxHeatSquash, prHeatDeformer::outputGeom);
    // aMaxHeatStretch
    aMaxHeatStretch = nAttr.create( "stretchMaxHeat", "stretchMaxHeat", MFnNumericData::kFloat, 1.0 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0.0 );
    addAttribute( aMaxHeatStretch );
    attributeAffects(aMaxHeatStretch, prHeatDeformer::outputGeom);

    // aGrowHeat
    aGrowHeat = nAttr.create( "growHeat", "growHeat", MFnNumericData::kInt, 0 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0 );
    nAttr.setSoftMax( 5 );
    addAttribute( aGrowHeat );
    attributeAffects(aGrowHeat, prHeatDeformer::outputGeom);
    // aGrowHeatSquash
    aGrowHeatSquash = nAttr.create( "squashGrowHeat", "squashGrowHeat", MFnNumericData::kInt, 0 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0 );
    nAttr.setSoftMax( 5 );
    addAttribute( aGrowHeatSquash );
    attributeAffects(aGrowHeatSquash, prHeatDeformer::outputGeom);
    // aGrowHeatStretch
    aGrowHeatStretch = nAttr.create( "stretchGrowHeat", "stretchGrowHeat", MFnNumericData::kInt, 0 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0 );
    nAttr.setSoftMax( 5 );
    addAttribute( aGrowHeatStretch );
    attributeAffects(aGrowHeatStretch, prHeatDeformer::outputGeom);

    // aSmoothHeatIterations
    aSmoothHeatIterations = nAttr.create( "iterationsSmoothHeat", "iterationsSmoothHeat", MFnNumericData::kInt, 0 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0 );
    nAttr.setSoftMax( 5 );
    addAttribute( aSmoothHeatIterations );
    attributeAffects(aSmoothHeatIterations, prHeatDeformer::outputGeom);
    // aSmoothHeatStrength
    aSmoothHeatStrength = nAttr.create( "strengthSmoothHeat", "strengthSmoothHeat", MFnNumericData::kFloat, 0.5 );
    nAttr.setKeyable(true);
    nAttr.setMin( 0.0 );
    nAttr.setMax( 1.0 );
    addAttribute( aSmoothHeatStrength );
    attributeAffects(aSmoothHeatStrength, prHeatDeformer::outputGeom);

	// -----------------------
	// make paintable
	// -----------------------
	MGlobal::executeCommand("makePaintable -attrType multiFloat -sm deformer prHeatDeformer weights");
	MGlobal::executeCommand("makePaintable -attrType multiFloat -sm deformer prHeatDeformer multiplyHeatMap");
	MGlobal::executeCommand("makePaintable -attrType multiFloat -sm deformer prHeatDeformer multiplyHeatSquashMap");
	MGlobal::executeCommand("makePaintable -attrType multiFloat -sm deformer prHeatDeformer multiplyHeatStretchMap");
	MGlobal::executeCommand("makePaintable -attrType multiFloat -sm deformer prHeatDeformer maxHeatSquashMap");
	MGlobal::executeCommand("makePaintable -attrType multiFloat -sm deformer prHeatDeformer maxHeatStretchMap");

	return stat;
}

void* prHeatDeformer::creator()
{
	return new prHeatDeformer();
}

prHeatDeformer::prHeatDeformer() {}
prHeatDeformer::~prHeatDeformer() {}
