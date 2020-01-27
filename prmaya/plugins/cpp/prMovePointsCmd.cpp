#include <map>
#include <iostream>

#include <maya/MGlobal.h>
#include <maya/MPxCommand.h>
#include <maya/MFnPlugin.h>

#include <maya/MSelectionList.h>
#include <maya/MGlobal.h>
#include <maya/MArgList.h>
#include <maya/MString.h>
#include <maya/MVector.h>
#include <maya/MItMeshVertex.h>
#include <maya/MDagPath.h>
#include <maya/MIntArray.h>
#include <maya/MFnMesh.h>

//typedef std::map<int, MVector> DeltaDict;

class prMovePointsCmd : public MPxCommand
{
public:
	prMovePointsCmd();
	virtual		~prMovePointsCmd();
	MStatus		doIt(const MArgList& args);
	MStatus		redoIt();
	MStatus		undoIt();
	bool		isUndoable() const;
	static		void* creator();
private:
	//MItMeshVertex drivenIter;
	MDagPath meshDagPath;
	int space;
	MIntArray deltaVertexIds;
	MVectorArray deltas;
	
	MStatus		addDeltas(bool undoCall = false);
};


MStatus prMovePointsCmd::doIt(const MArgList& args){
	MStatus stat = MS::kSuccess;

	MString mesh = args.asString(0, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	//MGlobal::displayInfo(MString("mesh: ") + mesh);

	space = args.asInt(1, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	//MGlobal::displayInfo(MString("space: ") + space);

	double minDeltaLength = args.asDouble(2, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	//MGlobal::displayInfo(MString("minDeltaLength: ") + minDeltaLength);
	
	unsigned int i = 3;
	MIntArray vertexIds = args.asIntArray(i, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	//MGlobal::displayInfo(MString("vertexIds.length(): ") + vertexIds.length());
	if (args.length() - 4 != vertexIds.length()) {
		//MGlobal::displayError(MString("missmatching number of vertexIds and vectors (or an argument is missing)"));
		return MS::kFailure;
	}

	MSelectionList selection;
	stat = selection.add(mesh);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	stat = selection.getDagPath(0, meshDagPath);
	CHECK_MSTATUS_AND_RETURN_IT(stat);

	for (i = 4; i < args.length(); i++) {
		MVector delta = args.asVector(i, 3, &stat);
		CHECK_MSTATUS_AND_RETURN_IT(stat);
		if (delta.length() < minDeltaLength)
			continue;
		deltaVertexIds.append(vertexIds[i - 4]);
		deltas.append(delta);
	}
	//MGlobal::displayInfo(MString("deltas.length(): ") + deltas.length());
	return redoIt();
}

MStatus prMovePointsCmd::redoIt(){
	setResult( "prMovePointsCmd command executed!!\n" );
	addDeltas();
	return MS::kSuccess;
}

MStatus prMovePointsCmd::undoIt()
{
    MGlobal::displayInfo( "prMovePointsCmd command undone!\n" );
	addDeltas(true);
	return MS::kSuccess;
}

MStatus prMovePointsCmd::addDeltas(bool undoCall) {
	MStatus stat;
	//MGlobal::displayInfo("1234add deltas: " + deltas.length());
	
	//MItMeshVertex meshIter(meshDagPath);
	MFnMesh meshIter(meshDagPath);
	int prevIndex;
	MPoint position;
	for (unsigned int i = 0; i < deltas.length();i++)
	{
		//MGlobal::displayInfo(MString("\ni: ")+i);
		//MGlobal::displayInfo(MString("deltaVertexIds[i] ") + deltaVertexIds[i]);
		//MGlobal::displayInfo(MString("prevIndex ") + prevIndex);
		//prevIndex = meshIter.setIndex(deltaVertexIds[i], prevIndex);
		//position  = meshIter.position(MSpace::kObject);
		meshIter.getPoint(deltaVertexIds[i], position);
		if (undoCall) {
			position -= deltas[i];
		}
		else {
			position += deltas[i];
		}
		//meshIter.setPosition(position, MSpace::kObject);
		meshIter.setPoint(deltaVertexIds[i], position);

		
		
	}
	return MS::kSuccess;

}




void* prMovePointsCmd::creator(){return new prMovePointsCmd();}
prMovePointsCmd::prMovePointsCmd(){}
prMovePointsCmd::~prMovePointsCmd(){}
bool prMovePointsCmd::isUndoable() const{return true;}
MStatus initializePlugin(MObject obj)
{
	MStatus   status;
	MFnPlugin plugin(obj, "Parzival Roethlein", "0.0.1", "Any");

	status = plugin.registerCommand("prMovePointsCmd", prMovePointsCmd::creator);
	if (!status) {
		status.perror("registerCommand");
		return status;
	}

	return status;
}
MStatus uninitializePlugin(MObject obj)
{
	MStatus   status;
	MFnPlugin plugin(obj);

	status = plugin.deregisterCommand("prMovePointsCmd");
	if (!status) {
		status.perror("deregisterCommand");
		return status;
	}

	return status;
}
