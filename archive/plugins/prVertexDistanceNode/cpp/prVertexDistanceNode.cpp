// ==========================================================================
// Information/ReadMe in prVertexDistanceNode.py
// ==========================================================================
#include <maya/MPxDeformerNode.h> 
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnPlugin.h>
#include <maya/MTypeId.h> 
#include <maya/MFnMesh.h>

class prVertexDistanceNode : public MPxDeformerNode
{
public:
	prVertexDistanceNode();
	virtual ~prVertexDistanceNode();

	static void* creator();
	static MStatus initialize();
    virtual MStatus deform(MDataBlock& block, MItGeometry& iter, const MMatrix& mat, unsigned int multiIndex);
public:
	// attributes
	static MObject aDivide;
	static MObject aVertex;
	static MObject aDistance;
	static MTypeId id;
};

MTypeId prVertexDistanceNode::id( 0x0010A519 );

// local attributes
MObject prVertexDistanceNode::aDivide;
MObject prVertexDistanceNode::aVertex;
MObject prVertexDistanceNode::aDistance;

prVertexDistanceNode::prVertexDistanceNode() {}
prVertexDistanceNode::~prVertexDistanceNode() {}

void* prVertexDistanceNode::creator()
{
	return new prVertexDistanceNode();
}

MStatus prVertexDistanceNode::initialize()
{
	// attribute initialization
	MFnNumericAttribute nAttr;
	//	aDivide
	aDivide = nAttr.create( "divide", "div", MFnNumericData::kFloat, 1.0 );
	nAttr.setKeyable(true);
	addAttribute( aDivide );
	//	aVertex
	aVertex = nAttr.create( "vertex", "vtx", MFnNumericData::k2Int );
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);
	addAttribute( aVertex );
	//	aDistance
	aDistance = nAttr.create( "distance", "dst", MFnNumericData::kFloat );
	nAttr.setStorable(false);
	nAttr.setWritable(false);
	nAttr.setArray(true);
	nAttr.setUsesArrayDataBuilder(true);
	addAttribute( aDistance );
	// affects
	attributeAffects( prVertexDistanceNode::aVertex, prVertexDistanceNode::aDistance );
	attributeAffects( prVertexDistanceNode::aDivide, prVertexDistanceNode::aDistance );

	attributeAffects( prVertexDistanceNode::input, prVertexDistanceNode::aDistance );

	attributeAffects( prVertexDistanceNode::aVertex, prVertexDistanceNode::outputGeom );
	attributeAffects( prVertexDistanceNode::aDivide, prVertexDistanceNode::outputGeom );

	return MStatus::kSuccess;
}


MStatus prVertexDistanceNode::deform( MDataBlock& block, MItGeometry& iter, const MMatrix& /*m*/, unsigned int multiIndex )
// Arguments:
//   block		: the datablock of the node
//	 iter		: an iterator for the geometry to be deformed
//   m    		: matrix to transform the point into world space
//	 multiIndex : the index of the geometry that we are deforming
{
	MStatus stat;
	// get input mesh
	MArrayDataHandle hInput = block.outputArrayValue( input );
	hInput.jumpToElement( multiIndex );
	MDataHandle hInputGeom = hInput.outputValue().child( inputGeom );
	MObject oInputGeom = hInputGeom.asMesh();
	MFnMesh fnPoint( oInputGeom );
	// attribute handles
	MDataHandle envData = block.inputValue(envelope, &stat);
	if (MS::kSuccess != stat) return stat;
	MDataHandle hDivide = block.inputValue( aDivide, &stat );
    if (MS::kSuccess != stat) return stat;
	MArrayDataHandle hVertex = block.inputArrayValue( aVertex, &stat );
    if (MS::kSuccess != stat) return stat;
	MArrayDataHandle hDistance = block.outputArrayValue( aDistance, &stat );
    if (MS::kSuccess != stat) return stat;
	// values
	float env = envData.asFloat();
	float vDivide = hDivide.asFloat();
	// arrayDataBuilder
	MArrayDataBuilder dbDistance( &block, aDistance, hVertex.elementCount(), &stat );
	if (MS::kSuccess != stat) return stat;
	//
	float fDistance;
	// functionality
	for( int x=0; x<hVertex.elementCount(); x++ )
	{
		hVertex.jumpToArrayElement( x );
		// get vertices
		int iVtx0 = hVertex.inputValue().asInt2()[0];
		int iVtx1 = hVertex.inputValue().asInt2()[1];
		MPoint p1, p2;
		fnPoint.getPoint( iVtx0, p1, MSpace::kWorld );
		fnPoint.getPoint( iVtx1, p2, MSpace::kWorld );
		// calculate distance
		MVector vecP1toP2( p1.x-p2.x, p1.y-p2.y, p1.z-p2.z );
		fDistance = vecP1toP2.length() / vDivide;
		// set distance
		MDataHandle hDistanceBuilder = dbDistance.addElement( hVertex.elementIndex() );
		hDistanceBuilder.setFloat( fDistance );
		hDistance.set( dbDistance );
	}
	return stat;
}

// standard initialization procedures
MStatus initializePlugin( MObject obj )
{
	MStatus result;
	MFnPlugin plugin( obj, "Parzival Roethlein", "0.9.1", "Any");
	result = plugin.registerNode( "prVertexDistanceNode", prVertexDistanceNode::id, prVertexDistanceNode::creator, 
								  prVertexDistanceNode::initialize, MPxNode::kDeformerNode );

	return result;
}

MStatus uninitializePlugin( MObject obj)
{
	MStatus result;
	MFnPlugin plugin( obj );
	result = plugin.deregisterNode( prVertexDistanceNode::id );
	return result;
}