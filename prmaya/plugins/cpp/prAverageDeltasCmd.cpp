#include <map>
#include <iostream>

#include <maya/MGlobal.h>
#include <maya/MPxCommand.h>
#include <maya/MFnPlugin.h>

#include <maya/MGlobal.h>
#include <maya/MArgList.h>
#include <maya/MString.h>
#include <maya/MVector.h>
#include <maya/MItMeshVertex.h>
#include <maya/MDagPath.h>
#include <maya/MIntArray.h>

typedef std::map<int, MVector> DeltaDict;

class prAverageDeltasCmd : public MPxCommand
{
public:
	prAverageDeltasCmd();
	virtual		~prAverageDeltasCmd();
	MStatus		doIt(const MArgList& args);
	MStatus		redoIt();
	MStatus		undoIt();
	bool		isUndoable() const;
	static		void* creator();
private:
	//MItMeshVertex drivenIter;
	MDagPath drivenMDagPath;
	DeltaDict deltas;
	int space;
};


MStatus prAverageDeltasCmd::doIt(const MArgList& args)
//	Description:
//		implements the MEL prAverageDeltasCmd command.
//
//	Arguments:
//		args - the argument list that was passes to the command from MEL
//
//	Return Value:
//		MS::kSuccess - command succeeded
//		MS::kFailure - command failed (returning this value will cause the
//                     MEL script that is being run to terminate unless the
//                     error is caught using a "catch" statement.
{
	MStatus stat = MS::kSuccess;

	MString baseMesh = args.asString(0, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	MGlobal::displayInfo(MString("baseMesh: ") + baseMesh);

	MString drivenMesh = args.asString(1, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	MGlobal::displayInfo(MString("drivenMesh: ") + drivenMesh);
	
	int space = args.asInt(2, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	MGlobal::displayInfo(MString("space: ") + space);

	unsigned int i = 3;
	MIntArray vertexIds = args.asIntArray(i, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	MGlobal::displayInfo(MString("vertexIds.length(): ") + vertexIds.length());

	i = 4;
	MDoubleArray vertexWeights = args.asDoubleArray(i, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	MGlobal::displayInfo(MString("vertexWeights.length(): ") + vertexWeights.length());

	double weight = args.asDouble(5, &stat);
	CHECK_MSTATUS_AND_RETURN_IT(stat);
	MGlobal::displayInfo(MString("weight: ") + weight);

	return redoIt();
}

MStatus prAverageDeltasCmd::redoIt()
//	Return Value:
//		MS::kSuccess - command succeeded
//		MS::kFailure - redoIt failed.  this is a serious problem that will
//                     likely cause the undo queue to be purged
{
	// Since this class is derived off of MPxCommand, you can use the
	// inherited methods to return values and set error messages
	setResult( "prAverageDeltasCmd command executed!!\n" );

	return MS::kSuccess;
}

MStatus prAverageDeltasCmd::undoIt()
//	Return Value:
//		MS::kSuccess - command succeeded
//		MS::kFailure - redoIt failed.  this is a serious problem that will
//                     likely cause the undo queue to be purged
{

	// You can also display information to the command window via MGlobal
    MGlobal::displayInfo( "prAverageDeltasCmd command undone!\n" );
	return MS::kSuccess;
}

void* prAverageDeltasCmd::creator(){return new prAverageDeltasCmd();}

prAverageDeltasCmd::prAverageDeltasCmd(){}

prAverageDeltasCmd::~prAverageDeltasCmd(){}

bool prAverageDeltasCmd::isUndoable() const{return true;}

MStatus initializePlugin(MObject obj)
{
	MStatus   status;
	MFnPlugin plugin(obj, "Parzival Roethlein", "0.0.1", "Any");

	status = plugin.registerCommand("prAverageDeltasCmd", prAverageDeltasCmd::creator);
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

	status = plugin.deregisterCommand("prAverageDeltasCmd");
	if (!status) {
		status.perror("deregisterCommand");
		return status;
	}

	return status;
}
