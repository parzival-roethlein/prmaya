#include "prHeatDeformer.h"
#include <maya/MFnPlugin.h> 

// aetemplate layout
void prHeatDeformerAETemplate()
{
	MString ae("");
	//
	ae+= "global proc AEprHeatDeformerTemplate( string $nodeName )";
	ae+= "{\n";
	ae+= "AEswatchDisplay  $nodeName;\n";
	ae+= "editorTemplate -beginScrollLayout;\n";
	// envelope
	ae+= "AEgeometryFilterCommon $nodeName;\n";
	// setup
	ae+= "editorTemplate -beginLayout \"Setup Attributes\" -collapse 1;\n";
	ae+= "editorTemplate -addControl \"debug\";\n";
	ae+= "editorTemplate -addControl \"scale\";\n";
	ae+= "editorTemplate -endLayout;\n";
	// deformation
	ae+= "editorTemplate -beginLayout \"Deformation Attributes\" -collapse 0;\n";
	ae+= "editorTemplate -addControl \"deformationScale\";\n";
	ae+= "editorTemplate -addControl \"deformationType\";\n";
	ae+= "editorTemplate -addControl \"iterationsSmoothDeformer\";\n";
	ae+= "editorTemplate -addControl \"strengthSmoothDeformer\";\n";
	ae+= "editorTemplate -addControl \"blendShapeTangentSpace\";\n";
	ae+= "editorTemplate -endLayout;\n";
	// heat
	ae+= "editorTemplate -beginLayout \"Heat Attributes\" -collapse 0;\n";
	ae+= "editorTemplate -addControl \"displayColors\";\n";
	ae+= "editorTemplate -addControl \"colorBase\";\n";
	ae+= "editorTemplate -addControl \"colorSquash\";\n";
	ae+= "editorTemplate -addControl \"colorStretch\";\n";
	ae+= "editorTemplate -addControl \"measureTypeHeat\";\n";
	ae+= "editorTemplate -addControl \"multiplyHeat\";\n";
	ae+= "editorTemplate -addControl \"squashMultiplyHeat\";\n";
	ae+= "editorTemplate -addControl \"stretchMultiplyHeat\";\n";
	ae+= "editorTemplate -addControl \"maxHeat\";\n";
	ae+= "editorTemplate -addControl \"squashMaxHeat\";\n";
	ae+= "editorTemplate -addControl \"stretchMaxHeat\";\n";
	ae+= "editorTemplate -addControl \"growHeat\";\n";
	ae+= "editorTemplate -addControl \"squashGrowHeat\";\n";
	ae+= "editorTemplate -addControl \"stretchGrowHeat\";\n";
	ae+= "editorTemplate -addControl \"iterationsSmoothHeat\";\n";
	ae+= "editorTemplate -addControl \"strengthSmoothHeat\";\n";
	ae+= "editorTemplate -endLayout;\n";
	// extra (all missing attributes)
	ae+= "editorTemplate -addExtraControls;\n";
	// node behavior
	ae+= "AEgeometryFilterInclude $nodeName;\n";
	// hide
	ae+= "editorTemplate -suppress \"weightList\";\n";
	// end
	ae+= "editorTemplate -endScrollLayout;\n";
	ae+= "};";
	//
	MGlobal::executeCommand( ae );
}

// wrapper proc for deformer creation
void prHeatDeformerCreate()
{
	MString cr("");
	//
	cr+= "global proc string prHeatDeformer()";
	cr+= "{ \n";
	cr+= "  // get selection \n";
	cr+= "  string $sel[] = `ls -sl`; \n";
	cr+= "  // check selection \n";
	cr+= "  if( size($sel) != 1 ||  size($sel) != size(`ls -sl -type \"transform\"`) ) \n";
	cr+= "    error \"Script requires one selected transform or mesh.\"; \n";
	cr+= "  // create deformer \n";
	cr+= "  string $def[] = `deformer -type prHeatDeformer $sel[0]`; \n";
	cr+= "  // get all shapes \n";
	cr+= "  string $allShapes[] = `listRelatives -f -children -shapes $sel[0]`; \n";
	cr+= "  // get shapes without orig/intermediate \n";
	cr+= "  string $shapes[] = `listRelatives -f -ni -children -shapes $sel[0]`; \n";
	cr+= "  // display colors checkbox, for heat display \n";
	cr+= "  int $j; \n";
	cr+= "  for( $j=0; $j < size($shapes); $j++ ) \n";
	cr+= "    setAttr ($shapes[$j]+\".displayColors\") 1; \n";
	cr+= "  // check shapes / origs \n";
	cr+= "  if( size($shapes) * 2 != size($allShapes)  ) \n";
	cr+= "    error \"Could not create connections because intermediate shape cound does not match normal shape count.\"; \n";
	cr+= "  // connect orig meshes in orig/squash/stretch attributes \n";
	cr+= "  int $difference = size($allShapes) - size($shapes); \n";
	cr+= "  int $i; \n";
	cr+= "  for( $i=0; $i < $difference; $i++ ) \n";
	cr+= "  { \n";
	cr+= "    connectAttr ($allShapes[size($shapes)+$i]+\".outMesh\") ($def[0]+\".perGeometry[\"+$i+\"].origMesh\"); \n";
	cr+= "    connectAttr ($allShapes[size($shapes)+$i]+\".outMesh\") ($def[0]+\".perGeometry[\"+$i+\"].squashMesh\"); \n";
	cr+= "    connectAttr ($allShapes[size($shapes)+$i]+\".outMesh\") ($def[0]+\".perGeometry[\"+$i+\"].stretchMesh\"); \n";
	cr+= "  } \n";
	cr+= "  return $def[0]; \n";
	cr+= "}; ";
	//
	MGlobal::executeCommand( cr );
}

MStatus initializePlugin( MObject obj )
{ 
	MStatus stat;
	MFnPlugin plugin( obj, "Parzival Roethlein", "0.0.5", "Any" );

	stat = plugin.registerNode( "prHeatDeformer", prHeatDeformer::id, prHeatDeformer::creator, prHeatDeformer::initialize, MPxNode::kDeformerNode );
	if (!stat) 
	{
		stat.perror("registerNode");
		return stat;
	}
	//
	prHeatDeformerAETemplate();
	prHeatDeformerCreate();
	//
	return stat;
}

MStatus uninitializePlugin( MObject obj)
{
	MStatus stat;
	MFnPlugin plugin( obj );
	stat = plugin.deregisterNode( prHeatDeformer::id );
	if (!stat) 
	{
		stat.perror("deregisterNode");
		return stat;
	}
	return stat;
}