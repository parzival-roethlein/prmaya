// ==========================================================================
// Information/ReadMe in prAttractNode.py
//
// Uses openMP
//
// P E R F O R M A N C E:
// In my test openMP improves performance by 10-30%
// Performance comparison in fps (frames per second) with polygon attractor
// System: Core2Duo 2.6Ghz, 2GB RAM, Windows7 64bit
// [attract, closestVertex, projectOnNormal, all]
//                                    no-openMP / openMP
// -   1k vertices: [  MAX, 115.0, 105.0, 95.0] / [  MAX,   MAX, 116.0, 110.0]
// -   5k vertices: [ 42.0,  35.0,  30.2, 26.6] / [ 55.0,  47.0,  38.0,  35.0]
// -  10k vertices: [ 23.0,  18.8,  16.0, 13.8] / [ 31.6,  26.3,  20.8,  19.0]
// - 100k vertices: [  2.4,   2.0,   1.6,  1.4] / [  3.4,   2.8,   2.2,   2.0]
// ==========================================================================
// plug-in classes
#include <maya/MFnPlugin.h>
#include <maya/MTypeId.h>
#include <maya/MPxDeformerNode.h>
// attributes
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnGenericAttribute.h>
#include <maya/MFnMatrixAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MRampAttribute.h>
// variables
#include <maya/MFnMesh.h>
#include <maya/MMatrix.h>
#include <maya/MFloatArray.h>
#include <maya/MIntArray.h>
#include <maya/MGlobal.h>
#include <maya/MString.h>
#include <maya/MDagPath.h>
#include <maya/MPlugArray.h>
#include <maya/MFnMeshData.h>
#include <maya/MMeshIntersector.h>
#include <maya/MFnNurbsCurve.h>
#include <maya/MFnNurbsSurface.h>
#include <maya/MFnNurbsCurveData.h>
#include <maya/MFnNurbsSurfaceData.h>
#include <maya/MItGeometry.h>
// openMP
#include <maya/MThreadUtils.h>
#include <maya/MPointArray.h>

// ----------------------
// header
class prAttractNode : public MPxDeformerNode
{
public:
	prAttractNode();
	virtual ~prAttractNode();
	static void* creator();
	static MStatus initialize();
	virtual MStatus accessoryNodeSetup( MDagModifier& cmd );
    virtual MStatus deform( MDataBlock& block, MItGeometry& iter, const MMatrix& mat, unsigned int multiIndex );
public:
	static MTypeId id;
	// attributes
	//	user
	static MObject aWarnings;
	static MObject aMaxDistance;
	static MObject aFalloff;
	static MObject aMaxDistanceUv;
	static MObject aProjectOnNormal;
	static MObject aNormalDirectionLimit;
	static MObject aClosestVertex;
	//	deformer
	static MObject aInputMatrix;
	static MObject aInputTarget;
};

// ----------------------
// cpp
MTypeId prAttractNode::id( 0x0010A51A );

// user attributes
MObject prAttractNode::aWarnings;
MObject prAttractNode::aMaxDistance;
MObject prAttractNode::aFalloff;
MObject prAttractNode::aMaxDistanceUv;
MObject prAttractNode::aProjectOnNormal;
MObject prAttractNode::aNormalDirectionLimit;
MObject prAttractNode::aClosestVertex;
// deformer attributes
MObject prAttractNode::aInputMatrix;
MObject prAttractNode::aInputTarget;

prAttractNode::prAttractNode() {}
prAttractNode::~prAttractNode() {}

void* prAttractNode::creator()
{
	return new prAttractNode();
}

MStatus prAttractNode::initialize()
{
	// attribute initialization
	MFnGenericAttribute gAttr;
	MFnNumericAttribute nAttr;
	MFnMatrixAttribute mAttr;
	MRampAttribute rAttr;
	MFnEnumAttribute eAttr;

	// aWarning
	aWarnings = nAttr.create( "showWarnings", "showWarnings", MFnNumericData::kBoolean, 1 );
    addAttribute( aWarnings );
	// aMaxDistance
	aMaxDistance = nAttr.create( "maxDistance", "maxDistance", MFnNumericData::kFloat, 1.0 );
    nAttr.setKeyable(true);
    nAttr.setMin(0.0);
    addAttribute( aMaxDistance );
	attributeAffects( prAttractNode::aMaxDistance, prAttractNode::outputGeom );
	// aFalloff
    aFalloff = rAttr.createCurveRamp( "falloff", "falloff" );
    addAttribute( aFalloff );
	attributeAffects( prAttractNode::aFalloff, prAttractNode::outputGeom );
    // aMaxDistanceUv
    aMaxDistanceUv = rAttr.createCurveRamp( "maxDistanceUv", "maxDistanceUv" );
    addAttribute( aMaxDistanceUv );
	attributeAffects( prAttractNode::aMaxDistanceUv, prAttractNode::outputGeom );
	//
	// aProjectOnNormal
	aProjectOnNormal = nAttr.create( "projectOnNormal", "projectOnNormal", MFnNumericData::kFloat, 0.0 );
    nAttr.setKeyable(true);
    nAttr.setMin(0.0);
	nAttr.setMax(1.0);
    addAttribute( aProjectOnNormal );
	attributeAffects( prAttractNode::aProjectOnNormal, prAttractNode::outputGeom );

	// aNormalDirectionLimit
	aNormalDirectionLimit = eAttr.create( "normalDirectionLimit", "normalDirectionLimit", 0 );
	eAttr.setKeyable(true);
    eAttr.addField( "Off", 0 );
    eAttr.addField( "Only positive", 1 );
    eAttr.addField( "Only negative", 2 );
    addAttribute( aNormalDirectionLimit );
    attributeAffects( prAttractNode::aNormalDirectionLimit, prAttractNode::outputGeom );

	// aClosestVertex
	aClosestVertex = nAttr.create( "closestVertex", "closestVertex", MFnNumericData::kFloat, 0.0 );
    nAttr.setKeyable(true);
    nAttr.setMin(0.0);
	nAttr.setMax(1.0);
    addAttribute( aClosestVertex );
	attributeAffects( prAttractNode::aClosestVertex, prAttractNode::outputGeom );
	
    // aInputTarget
    aInputTarget = gAttr.create( "inputTarget", "inputTarget" );
    gAttr.setWritable(true);
    gAttr.setReadable(false);
	gAttr.addDataAccept( MFnData::kNurbsCurve );
	gAttr.addDataAccept( MFnData::kNurbsSurface );
	gAttr.addDataAccept( MFnData::kMesh );
	gAttr.addDataAccept( MFnData::kMatrix );
    addAttribute( aInputTarget );
	attributeAffects( prAttractNode::aInputTarget, prAttractNode::outputGeom );
    // aInputMatrix
    aInputMatrix = mAttr.create( "inputMatrix", "inputMatrix" );
    mAttr.setWritable(true);
    mAttr.setReadable(false);
    addAttribute( aInputMatrix );
	attributeAffects( prAttractNode::aInputMatrix, prAttractNode::outputGeom );
    
	// paintable
	MGlobal::executeCommand( "makePaintable -attrType multiFloat -shapeMode deformer prAttractNode weights;" );
	
	return MStatus::kSuccess;
}
//
MStatus prAttractNode::deform( MDataBlock& block, MItGeometry& iter, const MMatrix& mat, unsigned int multiIndex )
{
	// ----------------------
	MThreadUtils::syncNumOpenMPThreads();

	// ----------------------
	MStatus stat;
	MObject thisNode = thisMObject();

	// ----------------------
	// get attributes
	// envelope
	MDataHandle hEnvelope = block.inputValue( envelope, &stat);
	if ( stat != MS::kSuccess ) return stat;
	float fEnvelope = hEnvelope.asFloat();
	if( fEnvelope == 0.0 )
		return stat;
	// aMaxDistance
	MDataHandle hMaxDistance = block.inputValue( aMaxDistance, &stat);
	if ( stat != MS::kSuccess ) return stat;
	float fMaxDistance = hMaxDistance.asFloat();
	if( fMaxDistance == 0.0 )
		return stat;
	MDataHandle hWarnings = block.inputValue( aMaxDistance, &stat);
	if ( stat != MS::kSuccess ) return stat;
	bool warnings = hWarnings.asBool();
	// aFalloff
	MRampAttribute rampFalloff( thisNode, aFalloff, &stat );
	if ( stat != MS::kSuccess ) return stat;
	// aMaxDistanceUv
	MRampAttribute rampMaxDistUv( thisNode, aMaxDistanceUv, &stat );
	if ( stat != MS::kSuccess ) return stat;
	// aProjectOnNormal
	MDataHandle hProjectOnNormal = block.inputValue( aProjectOnNormal, &stat);
	if ( stat != MS::kSuccess ) return stat;
	float fProjectOnNormal = hProjectOnNormal.asFloat();
	// inputGeom (for fProjectOnNormal)
	MFnMesh mfInputGeom;
	if( fProjectOnNormal > 0.0 )
	{
		MArrayDataHandle hInput = block.outputArrayValue( input, &stat );
		if ( stat != MS::kSuccess ) return stat;
		hInput.jumpToElement( multiIndex );
		MDataHandle hInputGeom = hInput.outputValue().child( inputGeom );
		MObject oInputGeom = hInputGeom.asMesh();
		mfInputGeom.setObject( oInputGeom );
	}
	// aNormalDirectionLimit
	MDataHandle hNormalDirectionLimit = block.inputValue( aNormalDirectionLimit, &stat );
	if ( stat != MS::kSuccess ) return stat;
	short sNormalDirectionLimit = hNormalDirectionLimit.asShort();
	// aClosestVertex
    MDataHandle hClosestVertex = block.inputValue( aClosestVertex );
	float fClosestVertex = hClosestVertex.asFloat();
	// aInputMatrix
	MDataHandle hInputMatrix = block.inputValue( aInputMatrix, &stat );
	if ( stat != MS::kSuccess ) return stat;
	MMatrix matInputMatrix = hInputMatrix.asMatrix();
	MPlug plugInputMatrix( thisNode, aInputMatrix );
	if( plugInputMatrix.isConnected() == false )
	{
		if( warnings ) 
			MGlobal::executeCommand( "print \"\\nMissing incoming connection to aInputMatrix.\"" );
		return stat;
	}
	// aInputTarget
	MDataHandle hinputTarget = block.inputValue( aInputTarget );
	MPlug pluginputTarget( thisNode, aInputTarget );
	if( pluginputTarget.isConnected() == false )
	{
		if( warnings )
			MGlobal::executeCommand( "print \"\\nMissing incoming connection to aInputTarget.\"" );
		return stat;
	}

	// ----------------------
	// get dag
	MPlugArray plugarinputTarget;
	pluginputTarget.connectedTo( plugarinputTarget, true, false, &stat);
	if ( stat != MS::kSuccess ) return stat;
	MPlug plugDaginputTarget = plugarinputTarget[0];
	MObject oDaginputTarget = plugDaginputTarget.node();
	MFnDagNode fnDaginputTarget( oDaginputTarget );
	MDagPath dagPathinputTarget;
	fnDaginputTarget.getPath( dagPathinputTarget );

	// ----------------------
	// determine inputTarget type
	MFnData::Type typeinputTarget = hinputTarget.type();
	MString strinputTargetType;
	MMeshIntersector fnTargetPoly;// poly
	MFnMesh fnMesh;// poly
	MFnNurbsCurve fnTargetNurbsCurve;// curve
	MFnNurbsSurface fnTargetNurbsSurface;// nurbs
	if( typeinputTarget == MFnMeshData::kMesh )
	{
		strinputTargetType = "mesh";
		MObject oInputPoly;
		oInputPoly = hinputTarget.data();
		stat = fnTargetPoly.create( oInputPoly, matInputMatrix );
		if(stat!=MS::kSuccess)return stat;
		stat = fnMesh.setObject( oInputPoly );
		if(stat!=MS::kSuccess)return stat;
	}
	else if( typeinputTarget == MFnNurbsCurveData::kNurbsCurve )
	{
		strinputTargetType = "curve";
		stat = fnTargetNurbsCurve.setObject( dagPathinputTarget );
		if(stat!=MS::kSuccess)return stat;
	}
	else if( typeinputTarget == MFnNurbsSurfaceData::kNurbsSurface )
	{
		strinputTargetType = "nurbs";
		stat = fnTargetNurbsSurface.setObject( dagPathinputTarget );
		if(stat!=MS::kSuccess)return stat;
	}

	// ----------------------
	// store indices (for case of removed vertices [edit membership])
	MIntArray iaIterIndices;
	while( ! iter.isDone() )
	{
		iaIterIndices.append( iter.index() );
		iter.next();
	}
	iter.reset();

	// ----------------------
	// loop variables
	
	const MMatrix matInverse = mat.inverse();
	const double dCurveTolerance = 0.000001;
	
	float wPt, fRampMaxDist, fRampFalloff;
	double dUValue, dPercent, loopVecLength, closestLength, dVecDotProduct;
	MPoint ptClosest, pt, loopPt;
	MPointOnMesh ptomMesh;
	float2 fUvValue;
	MVector loopVec, closestVector, vecMove;
	MIntArray faceVertices;
	bool failed = false;// OpenMP

	// store vertices
	MPointArray verts;
	iter.allPositions( verts );
	int nPoints = verts.length();
	
	// ----------------------
	// loop
	#ifdef _OPENMP
	#pragma omp parallel for if(nPoints>900 && strinputTargetType=="mesh") \
							private( stat, wPt, fRampMaxDist, fRampFalloff, dUValue, dPercent, loopVecLength, closestLength, dVecDotProduct, ptClosest, pt, loopPt, ptomMesh, fUvValue, loopVec, closestVector, vecMove, faceVertices )
	#endif
	for( int i=0; i<nPoints; i++ )
	{
		if( failed ) continue;
		// weight, skip calculation if zero
		wPt = weightValue( block, multiIndex, iaIterIndices[i] );
		if( wPt == 0.0 ) continue;
		pt = verts[i];
		// set to worldspace
		pt *= mat;
		// polyMesh
		if( strinputTargetType == "mesh" )
		{
			// get closest point
			stat = fnTargetPoly.getClosestPoint( pt, ptomMesh );
			if(stat!=MS::kSuccess){ failed=true; continue; }
			ptClosest = ptomMesh.getPoint();
			// get u value
			#pragma omp critical
			stat = fnMesh.getUVAtPoint( ptClosest, fUvValue, MSpace::kWorld );
			if(stat!=MS::kSuccess){ failed=true; continue; }
			dUValue = fUvValue[0];
			// closest vertex
			if( fClosestVertex > 0.0 )
			{
				stat = fnMesh.getPolygonVertices( ptomMesh.faceIndex(), faceVertices );
				if(stat!=MS::kSuccess){ failed=true; continue; }
				closestLength = 0.0;// for if condition
				for( unsigned int eachVert=0; eachVert<faceVertices.length(); eachVert++ )
				{
					stat = fnMesh.getPoint( faceVertices[eachVert], loopPt, MSpace::kWorld );
					if(stat!=MS::kSuccess){ failed=true; continue; }
					loopVec = loopPt - ptClosest;
					loopVecLength = loopVec.length();
					if( eachVert == 0 || loopVecLength < closestLength )
					{
						closestVector = loopVec;
						closestLength = loopVecLength;
					}
				}
				// adjust vector with closestVertex value
                closestVector *= fClosestVertex;
                ptClosest += closestVector;
			}
			// set to worldspace
			ptClosest *= matInputMatrix;
		}
		else if( strinputTargetType == "curve" )
		{
			// get closest point and u value
			//#pragma omp critical// for tests without condition "mesh"
			ptClosest = fnTargetNurbsCurve.closestPoint( pt, &dUValue, dCurveTolerance, MSpace::kWorld, &stat );
			if(stat!=MS::kSuccess){ failed=true; continue; }
		}
		else if( strinputTargetType == "nurbs" )
		{
			// get closest point and u value
			//#pragma omp critical// for tests without condition "mesh"
			ptClosest = fnTargetNurbsSurface.closestPoint( pt, &dUValue, NULL, false, dCurveTolerance, MSpace::kWorld, &stat );
			if(stat!=MS::kSuccess){ failed=true; continue; }
		}
		// move vector
		vecMove = ptClosest - pt;
		rampMaxDistUv.getValueAtPosition( (float)dUValue, fRampMaxDist, &stat );
		if(stat!=MS::kSuccess){ failed=true; continue; }
		// max distance each
		float fMaxDistanceEach = fMaxDistance * fRampMaxDist;
		if( vecMove.length() < fMaxDistanceEach )
		{
			dPercent = vecMove.length() / fMaxDistanceEach;
			rampFalloff.getValueAtPosition( (float)(1.0-dPercent), fRampFalloff, &stat );
			if(stat!=MS::kSuccess){ failed=true; continue; }
			vecMove *= fRampFalloff;
			
			if( fProjectOnNormal > 0.0 )
			{
				// get normal
				#pragma omp critical
				stat = mfInputGeom.getVertexNormal( iaIterIndices[i], loopVec, MSpace::kWorld );
				if(stat!=MS::kSuccess){ failed=true; continue; }
				// normalize
				loopVec.normalize();
				// project move vector on normal
				dVecDotProduct = vecMove * loopVec;
				loopVec *= dVecDotProduct;
				if( sNormalDirectionLimit == 1 && dVecDotProduct <= 0 )
					loopVec *= 0;
				else if( sNormalDirectionLimit == 2 && dVecDotProduct > 0 )
					loopVec *= 0;
				// blend
				vecMove = vecMove*(1.0-fProjectOnNormal) + loopVec*fProjectOnNormal;
			}
			// adjust with envelope and painted weight
			vecMove *= fEnvelope * wPt;
			// new pos
			pt += vecMove;
			// back to object space
			pt *= matInverse;
			// save new position
			verts[i] = pt;
		}
	}// end for
	if( failed )
	{
		MGlobal::executeCommand( "print \"\\nomp parallel status failure.\"" );
		return MStatus::kFailure;
	}
	// set new positions
	iter.setAllPositions(verts);
	return stat;
}

MStatus prAttractNode::accessoryNodeSetup(MDagModifier& cmd)
{
	// initialize ramps
	MStatus stat;
	MObject thisNode = thisMObject();
	//
	// aFalloff
	MRampAttribute rampFalloff( thisNode, prAttractNode::aFalloff, &stat );
	
	MFloatArray f1,f2;// position, value
	MIntArray i1;// interpolation

	f1.append(float(0.0));
    f1.append(float(1.0));
    
    f2.append(float(0.0));
    f2.append(float(1.0));
    
	i1.append(MRampAttribute::kSmooth);
	i1.append(MRampAttribute::kSmooth);
    
    rampFalloff.addEntries(f1,f2,i1);
	//
    // aMaxDistanceUv
	MRampAttribute rampMaxDistUv( thisNode, prAttractNode::aMaxDistanceUv );
    
	f1.clear();
	f2.clear();
	i1.clear();
	
    f1.append(float(0.5));
    f2.append(float(1.0));
	i1.append(MRampAttribute::kSmooth);
    
    rampMaxDistUv.addEntries(f1,f2,i1);
	//
	//
    return stat;
}

// aetemplate to be called in initializePlugin,
//  if there is a better way to source mel procs with cpp api please let me know
void prAttractNodeAETemplate()
{
	MString ae("");
	//
	ae+= "global proc AEprAttractNodeTemplate( string $nodeName )";
	ae+= "{\n";
	ae+= "AEswatchDisplay $nodeName;\n";
	ae+= "editorTemplate -beginScrollLayout;\n";
	ae+= "// include/call base class/node attributes\n";
	ae+= "AEgeometryFilterCommon $nodeName;\n";
	ae+= "// custom attributes\n";
	ae+= "editorTemplate -beginLayout \"prAttractNode Attributes\" -collapse 0;\n";
	ae+= "    editorTemplate -addControl \"maxDistance\";\n";
	ae+= "    AEaddRampControl ($nodeName+\".falloff\");\n";
	ae+= "    AEaddRampControl ($nodeName+\".maxDistanceUv\");\n";
	ae+= "editorTemplate -beginLayout \"Normal Vector\" -collapse 0;\n";
	ae+= "    editorTemplate -addControl \"projectOnNormal\";\n";
	ae+= "    editorTemplate -addControl \"normalDirectionLimit\";\n";
	ae+= "editorTemplate -beginLayout \"Polygon Attractor\" -collapse 0;\n";
	ae+= "    editorTemplate -addControl \"closestVertex\";\n";
	ae+= "editorTemplate -endLayout;\n";
	ae+= "// add missing attrs (should be none)\n";
	ae+= "editorTemplate -addExtraControls;\n";
	ae+= "// node behavior\n";
	ae+= "AEgeometryFilterInclude $nodeName;\n";
	ae+= "editorTemplate -endScrollLayout;\n";
	ae+= "// hide attrs from \n";
	ae+= "editorTemplate -suppress \"weightList\";\n";
	ae+= "editorTemplate -suppress \"inputTarget\";\n";
	ae+= "editorTemplate -suppress \"inputMatrix\";\n";
	ae+= "};";
	//
	MGlobal::executeCommand( ae );
}


// wrapper proc for deformer creation
void prAttractNodeCreate()
{
	MString cr("");
	//
	cr+= "global proc prAttractNode()";
	cr+= "{ \n";
	cr+= "string $sel[] = `ls -sl -type \"transform\"`; \n";
	cr+= "if( size($sel) != 2 ) \n";
	cr+= " error \"Script requires two transforms to be selected.\"; \n";
	cr+= "string $driverShapes[] = `listRelatives -children $sel[0]`; \n";
	cr+= "string $drivenShapes[] = `listRelatives -children $sel[1]`; \n";
	cr+= "string $drivenShapeType = objectType($driverShapes[0]); \n";
	cr+= "if( $drivenShapeType != \"mesh\" && \n";
	cr+= "	  $drivenShapeType != \"nurbsCurve\" && \n";
	cr+= "	  $drivenShapeType != \"nurbsSurface\" ) \n";
	cr+= "	    error (\"Invalid driver shape type. Should be mesh/nurbsCurve/nurbsSurface, but got: \"+objectType($driverShapes[0])); \n";
	cr+= "if( objectType($drivenShapes[0]) != \"mesh\" ) \n";
	cr+= " error (\"Invalid driven shape type. Should be mesh. Instead got: \"+objectType($drivenShapes[0])); \n";
	cr+= "string $def[] = `deformer -type prAttractNode $sel[1]`; \n";
	cr+= "connectAttr( $sel[0]+\".matrix\", $def[0]+\".inputMatrix\" ); \n";
	cr+= "if( $drivenShapeType == \"mesh\" ) \n";
	cr+= " connectAttr( $driverShapes[0]+\".outMesh\", $def[0]+\".inputTarget\" ); \n";
	cr+= "else \n";
	cr+= " connectAttr( $driverShapes[0]+\".local\", $def[0]+\".inputTarget\" ); \n";
	cr+= "};";
	//
	MGlobal::executeCommand( cr );
}

// standard initialization procedures
MStatus initializePlugin( MObject obj )
{
	MStatus result;
	MFnPlugin plugin( obj, "Parzival Roethlein", "0.9.4", "Any");
	result = plugin.registerNode( "prAttractNode", prAttractNode::id, prAttractNode::creator, prAttractNode::initialize, MPxNode::kDeformerNode );
	//
	prAttractNodeAETemplate();
	prAttractNodeCreate();
	//
	return result;
}

MStatus uninitializePlugin( MObject obj)
{
	MStatus result;
	MFnPlugin plugin( obj );
	result = plugin.deregisterNode( prAttractNode::id );
	return result;
}