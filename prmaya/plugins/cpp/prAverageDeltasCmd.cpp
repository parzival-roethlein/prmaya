
#include <maya/MGlobal.h>
#include <maya/MPxCommand.h>
#include <maya/MFnPlugin.h>

class MArgList;

class prAverageDeltasCmd : public MPxCommand
{

public:
	prAverageDeltasCmd();
	virtual		~prAverageDeltasCmd();

	MStatus		doIt(const MArgList&);
	MStatus		redoIt();
	MStatus		undoIt();
	bool		isUndoable() const;

	static		void* creator();

private:
	// Store the data you will need to undo the command here
	//
};



MStatus prAverageDeltasCmd::doIt( const MArgList& )
//
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
//
{
	MStatus stat = MS::kSuccess;


	// Typically, the doIt() method only collects the infomation required
	// to do/undo the action and then stores it in class members.  The
	// redo method is then called to do the actuall work.  This prevents
	// code duplication.
	//
	return redoIt();
}

MStatus prAverageDeltasCmd::redoIt()
//
//	Description:
//		implements redo for the MEL prAverageDeltasCmd command.
//
//		This method is called when the user has undone a command of this type
//		and then redoes it.  No arguments are passed in as all of the necessary
//		information is cached by the doIt method.
//
//	Return Value:
//		MS::kSuccess - command succeeded
//		MS::kFailure - redoIt failed.  this is a serious problem that will
//                     likely cause the undo queue to be purged
//
{
	// Since this class is derived off of MPxCommand, you can use the
	// inherited methods to return values and set error messages
	//
	setResult( "prAverageDeltasCmd command executed!!!\n" );

	return MS::kSuccess;
}

MStatus prAverageDeltasCmd::undoIt()
//
//	Description:
//		implements undo for the MEL prAverageDeltasCmd command.
//
//		This method is called to undo a previous command of this type.  The
//		system should be returned to the exact state that it was it previous
//		to this command being executed.  That includes the selection state.
//
//	Return Value:
//		MS::kSuccess - command succeeded
//		MS::kFailure - redoIt failed.  this is a serious problem that will
//                     likely cause the undo queue to be purged
//
{

	// You can also display information to the command window via MGlobal
	//
    MGlobal::displayInfo( "prAverageDeltasCmd command undone!\n" );

	return MS::kSuccess;
}

void* prAverageDeltasCmd::creator()
//
//	Description:
//		this method exists to give Maya a way to create new objects
//      of this type.
//
//	Return Value:
//		a new object of this type
//
{
	return new prAverageDeltasCmd();
}

prAverageDeltasCmd::prAverageDeltasCmd()
//
//	Description:
//		prAverageDeltasCmd constructor
//
{}

prAverageDeltasCmd::~prAverageDeltasCmd()
//
//	Description:
//		prAverageDeltasCmd destructor
//
{
}

bool prAverageDeltasCmd::isUndoable() const
//
//	Description:
//		this method tells Maya this command is undoable.  It is added to the
//		undo queue if it is.
//
//	Return Value:
//		true if this command is undoable.
//
{
	return true;
}

MStatus initializePlugin(MObject obj)
//
//	Description:
//		this method is called when the plug-in is loaded into Maya.  It
//		registers all of the services that this plug-in provides with
//		Maya.
//
//	Arguments:
//		obj - a handle to the plug-in object (use MFnPlugin to access it)
//
{
	MStatus   status;
	MFnPlugin plugin(obj, "", "2018", "Any");

	status = plugin.registerCommand("prAverageDeltasCmd", prAverageDeltasCmd::creator);
	if (!status) {
		status.perror("registerCommand");
		return status;
	}

	return status;
}

MStatus uninitializePlugin(MObject obj)
//
//	Description:
//		this method is called when the plug-in is unloaded from Maya. It
//		deregisters all of the services that it was providing.
//
//	Arguments:
//		obj - a handle to the plug-in object (use MFnPlugin to access it)
//
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
