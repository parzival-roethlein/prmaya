/*
D E S C R I P T I O N:
Heat (stretch/compression) driven mesh deformation
Create secondary automated deformation like wrinkles on skin or clothing.
Or for squash/stretch, fake preserving volume, etc

U S A G E:
- First load the plug-in via Window->Settings->Prefs->Plug-in Manager
- Automated setup:
  ..... and execute MEL command: "prHeatDeformer"
- Manual setup:
  Select driven mesh, then execute (MEL): deformer -type "prHeatDeformer"
  Now ... connections have to be made:
  1. ... TODO

V E R S I O N S:
2013-02-11 / 0.0.4: usability (wrapper script, aeTemplate, UI)
2013-01-27 / 0.0.3: all features working
2013-01-25 / 0.0.2: data getting done, paintable attributes, dirty optimization
2013-01-23 / 0.0.1: cpp start
2012-12-05 / 0.0.1: python prototype done (normal/blendshape, smooth, grow, tangent)
2012-11-16 / 0.0.0: python prototype start 

T O D O:
- C:/Program Files/Autodesk/Maya2012.5/scripts/others/setDrivenKeyWindow.mel line 751: Attribute name not recognized
- scale attribute, multiply vectors
- test on production meshes (with multiple shapes)
- dirty each map, to improve painting speed
- openMP loops
- (tweak) thisNode name in print messages, so user knows where they are coming from
- (error check) if orig/squash/stretch have same vertexcount as currentGeo

- (feature) paintable grow / smooth heat / smooth deformation maps?
- (comfort) when displayColor attributes get activated, use dirtyMethod to toggle each shape "displayColors" attribute?
- (maybe) ramp for squash heat and ramp for stretchheat (range is 0 to squashMaxnormal/stretchMaxNormal) so with smooth/gaussian curve, the trigger point is not as obvious
- (performance) get edge length from point positions
- (performance) grow and smooth heat in same loop?
- (performance) create fake tangent space from point positions (use two neighbors, maybe use 0 neighbor and 2 neighbor, for better plane, less problematic)
- (performance) use custom vectorArray? for speed

- (feature) angle heat? (maybe just use poseDeformer/reader?)
- (feature) direction blendshapes (uv based/tangent)
- (maybe) paint default squashHeat / default stretchHeat (0.0-1.0) multiply attr for each
- (maybe) maybe adjust edge length to give similar heat as face area or the other way? (face area scales faster)

R E L A T E D:
ati paper, maya muscleSkinDeformer relax/wrinkle function, fStretch, soup tensionBlendShape

A T T R I B U T E S:
...

T E S T:
////////////////////////////////////////
def prHeatDeformer(arg=None):
    import maya.cmds as mc
    import maya.mel as mm
    mc.file(new=True, f=True)
    if( arg ):
        try:
            mc.unloadPlugin( "prHeatDeformer.mll" )
        except:
            pass
    else:
        #mc.loadPlugin( r"C:\Users\prothlein\Documents\Visual Studio 2008\Projects\prHeatDeformer\prHeatDeformer.mll" )
        mc.loadPlugin( r"E:\Visual Studio 2010\Projects\prHeatDeformer\prHeatDeformer.mll" )
        mc.polySphere(sx=100, sh=100)
        mc.polySphere(sx=100, sh=100)
        mc.polySphere(sx=100, sh=100)
        mc.polySphere(sx=100, sh=100)
        mc.setAttr( 'pSphere1.tx', 3 )
        mc.setAttr( 'pSphere2.tx', 5 )
        mc.setAttr( 'pSphere3.tx', 7 )
        mc.setAttr( "pSphereShape4.displayColors", 1);
        mc.deformer( type='prHeatDeformer' )
        mc.connectAttr( "pSphereShape1.outMesh", "prHeatDeformer1.perGeometry[0].origMesh" )
        mc.connectAttr( "pSphereShape2.outMesh", "prHeatDeformer1.perGeometry[0].squashMesh" )
        mc.connectAttr( "pSphereShape3.outMesh", "prHeatDeformer1.perGeometry[0].stretchMesh" )
        mc.setAttr( 'prHeatDeformer1.deformationType', 2 )
        mc.setAttr( 'prHeatDeformer1.debug', 2 )
prHeatDeformer(1) # unload
prHeatDeformer() # load
////////////////////////////////////////
*/
#ifndef _prHeatDeformer
#define _prHeatDeformer

#include <maya/MPxDeformerNode.h>
#include <maya/MTypeId.h> 

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MFnGenericAttribute.h>
#include <maya/MFnEnumAttribute.h>

#include <maya/MFnMeshData.h>
#include <maya/MFnMesh.h>

#include <maya/MItMeshVertex.h>
#include <maya/MItMeshEdge.h>
#include <maya/MItMeshPolygon.h>
#include <maya/MItGeometry.h>

#include <maya/MPlug.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFloatArray.h>
#include <maya/MPointArray.h>
#include <maya/MMatrixArray.h>

#include <maya/MGlobal.h>
#include <map>

#include <maya/MThreadUtils.h>
#include <maya/MPointArray.h>

class prHeatDeformer : public MPxDeformerNode
{
	public:
		prHeatDeformer();
		virtual ~prHeatDeformer(); 
		static  void* creator();
		static MStatus initialize();
		virtual MStatus deform(MDataBlock& block, MItGeometry& iter, const MMatrix& mat, unsigned int mIndex);
		virtual void postConstructor();
		virtual MStatus setDependentsDirty( const MPlug& plug, MPlugArray &plugArray );
		// default
		static MTypeId id;
		// code
		static MObject aDebug;
		// deformer
		static MObject aScale;
		// aPerGeometry attributes
		//	geo
		static MObject aOrigMesh;
		static MObject aSquashMesh;
		static MObject aStretchMesh;
		//	maps
		static MObject aMultiplyHeatMap;
		static MObject aMultiplyHeatSquashMap;
		static MObject aMultiplyHeatStretchMap;
		static MObject aMaxHeatSquashMap;
		static MObject aMaxHeatStretchMap;
		//	aPerGeometry
		static MObject aPerGeometry;
		// deformation type
		static MObject aDeformationTitle;
		static MObject aDeformationScale;
		static MObject aDeformationType;
		static MObject aSmoothDeformationIterations;
		static MObject aSmoothDeformationStrength;
		static MObject aTangentSpace;
		// heat / algorithm
		static MObject aHeatTitle;
		static MObject aDisplayColors;
		static MObject aColorBase;
		static MObject aColorSquash;
		static MObject aColorStretch;
		static MObject aMeasureTypeHeat;
		static MObject aMultiplyHeat;
		static MObject aMultiplyHeatSquash;
		static MObject aMultiplyHeatStretch;
		static MObject aMaxHeat;
		static MObject aMaxHeatSquash;
		static MObject aMaxHeatStretch;
		static MObject aGrowHeat;
		static MObject aGrowHeatSquash;
		static MObject aGrowHeatStretch;
		static MObject aSmoothHeatIterations;
		static MObject aSmoothHeatStrength;
	private:
		MStatus getInputMesh( MDataBlock& block, unsigned int idx, MObject* oInputMesh );
		MStatus jumpToElement(MArrayDataHandle& ahArray, unsigned int idx);
		MMatrix getTangentSpace( MFnMesh& fnCurrentMesh, unsigned int iVertexId, MIntArray iFaceIds, MFloatVector& fvVertexNormal, short sTangentCalculation );
		int binarySearch( MIntArray iaSorted, int iToLookFor );
		// store per mesh attributes for performance
		std::map<unsigned int, bool> initialized_;
		std::map<unsigned int, MIntArray> membership_;
		// maps
		std::map<unsigned int, bool> dirtyMap_;
		std::map<unsigned int, MFloatArray> weights_;// var[geoId][weight1, ..]
		std::map<unsigned int, MFloatArray> multiplyHeatMap_;
		std::map<unsigned int, MFloatArray> multiplyHeatSquashMap_;
		std::map<unsigned int, MFloatArray> multiplyHeatStretchMap_;
		std::map<unsigned int, MFloatArray> maxHeatSquashMap_;
		std::map<unsigned int, MFloatArray> maxHeatStretchMap_;
		// origMesh (incl general geo data)
		std::map<unsigned int, bool> dirtyOrigMesh_;
		std::map<unsigned int, double> dAverageEdgeLength_;
		std::map<unsigned int, std::map<unsigned int, MIntArray>> connectedVertices_;// var[geoId][vertId][neighborId1, ..]
		std::map<unsigned int, std::map<unsigned int, MIntArray>> connectedEdges_;
		std::map<unsigned int, std::map<unsigned int, MIntArray>> connectedFaces_;
		std::map<unsigned int, MPointArray> origPoints_;
		std::map<unsigned int, MMatrixArray> origTangentSpaces_;
		std::map<unsigned int, MDoubleArray> origConnectedEdgeLengths_;
		std::map<unsigned int, MDoubleArray> origConnectedFaceAreas_;
		// squash/stretch mesh
		std::map<unsigned int, bool> dirtySquashMesh_;
		std::map<unsigned int, MVectorArray> squashVectors_;
		std::map<unsigned int, bool> dirtyStretchMesh_;
		std::map<unsigned int, MVectorArray> stretchVectors_;
};
#endif