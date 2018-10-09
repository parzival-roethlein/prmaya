"""
# DESCRIPTION
This deformer does attract mesh vertices to either: matrix (point), polygons, curves or nurbs-surfaces.
Use cases:
- Match shape of geometries with different topology
- Interactively snap vertices (closest vertex option)
- Sticky lips deformation in animation

# USAGE
The Python version (prAttractNode.py) should run on all Operation Systems and Maya
versions (tested on 2008-2015). The cpp version has to be compiled but runs faster.
- First load the plug-in via Window->Settings->Prefs->Plug-in Manager
- Automated setup:
  Select driver then driven. Then execute MEL command: "prAttractNode"
- Manual setup:
  Select driven mesh, then execute (MEL): deformer -type "prAttractNode"
  Now two connections have to be made
  1. driverTransform.worldMatrix[0] >>> prAttractNode1.inputMatrix
  2. driverShape.outShape >>> prAttractNode1.inputShape

# ATTRIBUTES
default:
- envelope: Multiply deformation effect. (For sticky lips: Increase over 1.0, to overshoot vertices, to have closed geometry after smoothing)
- weights (paintable): Same effect as envelope, but paintable per vertex. Points with zero weights are not calculated and improve performance.
control:
- maxDistance: Only vertices closer than maxDistance get attracted
- projectOnNormal: Project deformation on vertex normal
- normalDirectionLimit: When projectOnNormal is on, limit deformation to positive or negative normal direction
- falloff: Amount of attraction depending on distance (scaled to maxDistance)
- maxDistanceUv: Rescale maxDistance, depending on U value of closest point on target
- closestVertex: When target is polygon, move to closest vertex instead of closest point on surface
rig:
- inputMatrix: pPlane1.worldMatrix[0] / nurbsCircle1.worldMatrix[0] / nurbsPlane1.worldMatrix[0]
- inputShape: pPlaneShape1.outMesh / nurbsCircleShape1.local / nurbsPlaneShape1.local

# TODO
- make it work in maya 2018
- point target (use existing matrix attribute)
# TODO MAYBE
- creation script should work with vertex selection
- (maybe) time dependent falloff

# VERSIONS
2012-12-22 / 0.9.4: closest vertex for polygon target / project on normal (+/- limit)
2012-04-24 / 0.9.3: fixed cpp version weights problem, when removing vertices from deformer
2012-01-30 / 0.9.3: added openMP multithreading to cpp version, maxDistanceUv for poly fixed
2012-01-25 / 0.9.3: cpp version, createPrAttractNode def, merged inputShape attrs, ramp init 
2011-11-09 / 0.9.2: added switch for curve/polygon/nurbs target
2011-06-23 / 0.9.1: fixed to work in Maya 2012
2011-02-17 / 0.9.0: release

# LINKS
- Demo and tutorial video with link to latest version
https://vimeo.com/20002149
- Background information on my blog
http://pazrot3d.blogspot.com/2012/01/openmp-and-maya-api.html
- This was written in my spare time. If you found it useful for rigging or coding, consider supporting the author:
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

# CODE
This is a list of things others might learn from the code. I only mention stuff that I could 
not find anywhere else and that is often useful:
- How/Where to properly initialize a ramp attribute
- How to setup everything in a single .py/.mll file, for easy installation. (aeTemplate, wrapper script)
- (C++) OpenMP usage (see blogpost under L I N K S)
- How to use the MFnGenericAttribute to allow for mesh, nurbs, nurbscurve inputs into the same attribute

# REFERENCE
- I saw a video, to have vertices attracted by a curve for sticky lips on http://www.chadvernon.com
- How to read ramp attribute with Python API: jlCollisionDeformer https://vimeo.com/13150202

# PERFORMANCE
driver..-..vtx:...cpp./.python
polygon -   1k: 130.0 / 11.7
polygon -   5k:  55.0 /  2.4
polygon -  10k:  31.6 /  1.1
polygon - 100k:   3.4 /  0.2
curve   -   1k: 103.0 / 17.4
curve   -  10k:  15.8 /  2.0
NurbsSF -   1k:  21.3 / 10.5
NurbsSF -  10k:   2.4 /  1.1

# TEST
- To test the plug-in, run the following code in the script editor (Python tab):
####################
def prTestAttract(switch_arg):
    import maya.mel as mm
    import maya.cmds as mc
    mc.file(new=True, f=True)
    mm.eval( 'setWireframeOnShadedOption true modelPanel4;' )
    #mc.unloadPlugin( "prAttractNode.py" )
    mc.loadPlugin( r"E:\eclipseworkspace\git\prtools\plug-ins\prAttractNode\prAttractNode.py" )
    #mc.unloadPlugin( "prAttractNode.mll" )
    #mc.loadPlugin( r"E:\Visual Studio 2010\Projects\prAttractionNode\prAttractNode.mll" )
    mc.polySphere(sx=20, sy=20, r=1)[0]
    myDef = mc.deformer( type='prAttractNode' )[0]
    shapeAttr = None
    trans = None
    if( switch_arg == 'poly' ):
        trans = mc.polyPlane(sx=2, sy=2)[0]
        shapeAttr = mc.listRelatives(trans, children=1)[0]+'.outMesh'
    elif( switch_arg == 'curve' ):
        trans = mc.curve( p=[(-2,0.5,0), (-1,0.5,0), (0,0.5,0), (1,0.5,0)], k=[0,0,0,1,1,1] )
        shapeAttr = mc.listRelatives(trans, children=1)[0]+'.local'
    elif( switch_arg == 'nurbs' ):
        trans = mc.nurbsPlane()[0]
        shapeAttr = mc.listRelatives(trans, children=1)[0]+'.local'
    mc.connectAttr( shapeAttr, myDef+'.inputShape' )
    mc.connectAttr( trans+'.worldMatrix[0]', myDef+'.inputMatrix' )
prTestAttract( 'poly' )
#prTestAttract( 'curve' )
#prTestAttract( 'nurbs' )
####################

"""

import sys

import maya.OpenMaya as om
import maya.OpenMayaMPx as OpenMayaMPx
import maya.mel as mm


class prAttractNode(OpenMayaMPx.MPxDeformerNode):
    # plug-in
    pluginName = "prAttractNode"
    pluginId = om.MTypeId(0x0010A51A)
    # node
    aDebug = om.MObject()
    # attributes: control deformation
    aMaxDistance = om.MObject()
    aMaxDistanceUv = om.MObject()
    aFalloff = om.MObject()
    aClosestVertex = om.MObject()
    aProjectOnNormal = om.MObject()
    aNormalDirectionLimit = om.MObject()
    # attributes: input connection
    aInputMatrix = om.MObject()
    aInputShape = om.MObject()

    # code variable
    __membership = {}
    __weights = {}
    __weights_dirty = {}

    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)

    def setDependentsDirty(self, plug, plugArray):
        if plug == self.weights:
            # check if weights map is dirty, to reload it in deform
            self.__weights_dirty[plug.parent().logicalIndex()] = True

    def deform(self, block, iter, matrix, multiIndex):
        thisNode = self.thisMObject()

        # #################
        # get attributes
        # #################
        # aDebug
        debug_level = block.inputValue(self.aDebug).asShort()
        if debug_level == 2:
            self.debug_message(thisNode, 'deform start')
        # envelope
        env = block.inputValue(OpenMayaMPx.cvar.MPxDeformerNode_envelope).asFloat()
        if env == 0.0:
            if debug_level == 2:
                self.debug_message(thisNode, 'No calculation, because of envelope 0.0')
            return
        # aMaxDistance
        maxDist = block.inputValue(self.aMaxDistance).asFloat()
        if maxDist == 0.0:
            if debug_level == 2:
                self.debug_message(thisNode, 'No calculation, because of maxDist 0.0')
            return
        # aProjectOnNormal
        projectOnNormal = block.inputValue(self.aProjectOnNormal).asFloat()
        if projectOnNormal:
            # aNormalDirectionLimit
            normalDirectionLimit = block.inputValue(self.aNormalDirectionLimit).asShort()
            # inputGeom
            hInput = block.outputArrayValue(self.input)
            hInput.jumpToElement(multiIndex)
            hInputGeom = hInput.outputValue().child(self.inputGeom)
            oInputGeom = hInputGeom.asMesh()
            mfInputGeom = om.MFnMesh(oInputGeom)
        # aFalloff
        hFalloff = om.MRampAttribute(thisNode, self.aFalloff)
        # aMaxDistanceUv
        hMaxDistUv = om.MRampAttribute(thisNode, self.aMaxDistanceUv)
        # aClosestVertex
        closestVertex = block.inputValue(self.aClosestVertex).asFloat()
        # aInputMatrix (for refresh/eval/dirty and MMeshIntersector)
        mInputMatrix = block.inputValue(self.aInputMatrix).asMatrix()
        plugInputMatrix = om.MPlug(thisNode, self.aInputMatrix)
        if not plugInputMatrix.isConnected():
            if debug_level >= 1:
                self.debug_message(thisNode, 'No calculation, because of missing incoming connection to .inputMatrix')
            return

        # determine target type
        inputShapeType = None
        fnTarget = None
        #     look for shapes
        dhInputShape = block.inputValue(self.aInputShape)
        fnDagNode = self.getConnectedDagNode(self.aInputShape)
        if fnDagNode:
            if dhInputShape.type() == om.MFnMeshData.kMesh:
                inputShapeType = 'mesh'
                # MMeshIntersector for performance
                oInputPoly = dhInputShape.data()
                fnTarget = om.MMeshIntersector()
                fnTarget.create(oInputPoly, mInputMatrix)
                # MFnMesh for UV and closest vertex
                meshInputPoly = om.MFnMesh(oInputPoly)
            elif dhInputShape.type() == om.MFnNurbsCurveData.kNurbsCurve:
                inputShapeType = 'curve'
                fnTarget = om.MFnNurbsCurve(fnDagNode)
            elif dhInputShape.type() == om.MFnNurbsSurfaceData.kNurbsSurface:
                inputShapeType = 'nurbs'
                fnTarget = om.MFnNurbsSurface(fnDagNode)
        else:
            # found no shape, only use matrix transformation as target
            inputShapeType = 'matrix'
            fnTarget = om.MTransformationMatrix(mInputMatrix).getTranslation()
        if debug_level == 2:
            self.debug_message(thisNode, ('Using target: ' + inputShapeType))

        # #################
        # get dirty attributes
        # #################
        iter_count = iter.count()
        if iter_count == 0:
            return
        # membership 
        #     first call check
        if multiIndex not in self.__membership:
            if debug_level == 2:
                self.debug_message(thisNode, 'First call, initialize self.__membership[multiIndex]')
            self.__membership[multiIndex] = []
        #     count changed check
        if iter_count != len(self.__membership[multiIndex]):
            if debug_level == 2:
                self.debug_message(thisNode, 'Store membership vertex ids in self.__membership[multiIndex]')
            self.__membership[multiIndex] = []
            # store all membership vertex ids
            while not iter.isDone():
                self.__membership[multiIndex].append(iter.index())
                iter.next()
            iter.reset()
        # weights
        if multiIndex not in self.__weights_dirty:
            # first call
            if debug_level == 2:
                self.debug_message(thisNode, 'First call, initialize self.__weights_dirty[multiIndex]')
            self.__weights_dirty[multiIndex] = True
        if self.__weights_dirty[multiIndex]:
            # store weights
            if debug_level == 2:
                self.debug_message(thisNode, 'Store weights in self.__weights[multiIndex]')
            self.__weights[multiIndex] = []
            for each in self.__membership[multiIndex]:
                self.__weights[multiIndex].append(self.weightValue(block, multiIndex, each))
            self.__weights_dirty[multiIndex] = False

        # #################
        # loop variables
        # #################
        d_util = om.MScriptUtil()
        d_util.createFromDouble(0.0)
        d_ptr = d_util.asDoublePtr()

        f_util = om.MScriptUtil()
        f_util.createFromDouble(0.0)
        f_ptr = f_util.asFloatPtr()

        f2_util = om.MScriptUtil()
        f2_util.createFromList([0.0, 0.0], 2)
        f2_ptr = f2_util.asFloat2Ptr()

        loopPoint = om.MPoint()  # closestVertex
        loopVec = om.MVector()  # closestVertex, projectOnNormal

        matrixInverse = matrix.inverse()
        paAllPoints = om.MPointArray()

        # #################
        # loop
        # #################
        x = 0
        while not iter.isDone():
            iterIndex = self.__membership[multiIndex][x]

            # get painted weight
            ptWeight = self.__weights[multiIndex][x]
            if ptWeight == 0.0:
                continue
            # set point to world space
            pt = iter.position()
            pt *= matrix

            # #################
            # get closest point
            # #################
            closePt = None
            dUValue = None
            # #################
            # polyMesh
            if inputShapeType == 'mesh':
                ptOM = om.MPointOnMesh()
                fnTarget.getClosestPoint(pt, ptOM)
                # u value
                closePt = om.MPoint(ptOM.getPoint())
                meshInputPoly.getUVAtPoint(closePt, f2_ptr, om.MSpace.kWorld)
                dUValue = f2_util.getFloat2ArrayItem(f2_ptr, 0, 0)
                # closest vertex
                if closestVertex:
                    faceVertices = om.MIntArray()
                    meshInputPoly.getPolygonVertices(ptOM.faceIndex(), faceVertices)
                    closestVector = None
                    closestLength = None
                    for eachVertex in faceVertices:
                        meshInputPoly.getPoint(eachVertex, loopPoint, om.MSpace.kWorld)
                        loopVec = loopPoint - closePt
                        loopVecLength = loopVec.length()
                        if closestLength is None:
                            closestVector = om.MVector(loopVec)
                            closestLength = loopVecLength
                        elif loopVecLength < closestLength:
                            closestVector = om.MVector(loopVec)
                            closestLength = loopVecLength
                    # adjust vector with closestVertex value
                    closestVector *= closestVertex
                    closePt += closestVector
                # set closest point to worldspace
                closePt *= mInputMatrix
            # #################
            # curveLocal
            elif inputShapeType == 'curve':
                closePt = fnTarget.closestPoint(pt, d_ptr, 0.00001, om.MSpace.kWorld)
                dUValue = om.MScriptUtil.getDouble(d_ptr)
            # #################
            # nurbsLocal
            elif inputShapeType == 'nurbs':
                closePt = fnTarget.closestPoint(pt, d_ptr, None, False, 0.00001, om.MSpace.kWorld)
                dUValue = om.MScriptUtil.getDouble(d_ptr)
            else:
                print 'no matching shape type'
                return
            # #################
            # make it a local vector for the vertex
            vecMove = closePt - pt
            # adjust maxDistance with aMaxDistanceUv attribute
            hMaxDistUv.getValueAtPosition(dUValue, f_ptr)
            maxDistLocal = maxDist * om.MScriptUtil.getFloat(f_ptr)
            # check if vertex is in range
            if vecMove.length() < maxDistLocal:
                # adjust with aFalloff
                dPercent = vecMove.length() / maxDistLocal
                hFalloff.getValueAtPosition(float(1.0 - dPercent), f_ptr)
                valueFalloff = om.MScriptUtil.getFloat(f_ptr)
                vecMove *= valueFalloff
                # adjust with aProjectOnNormal
                if projectOnNormal:
                    # get normal
                    mfInputGeom.getVertexNormal(iterIndex, loopVec, om.MSpace.kWorld)
                    # normalize
                    loopVec.normalize()
                    # project move vector on normal
                    dVecDotProduct = vecMove * loopVec
                    loopVec *= dVecDotProduct
                    if normalDirectionLimit == 1 and dVecDotProduct <= 0:
                        # only positive
                        loopVec *= 0
                    elif normalDirectionLimit == 2 and dVecDotProduct > 0:
                        # only negative
                        loopVec *= 0
                    # blend 
                    vecMove = vecMove * (1 - projectOnNormal) + loopVec * projectOnNormal
                    #
                # adjust with envelope and painted value
                vecMove *= env * ptWeight
                # new position
                pt += vecMove
                # back to object space
                pt *= matrixInverse
                # save point position
                paAllPoints.append(pt)
            #
            x += 1
            iter.next()
        # end while
        iter.setAllPositions(paAllPoints)

    # deform

    # accessoryNodeSetup used to initialize the ramp attributes
    #     postConstructor does always get executed once when opening szene with node
    #     and it also does not know about values inside of rampattr during postConstructor
    def accessoryNodeSetup(self, cmd):
        thisNode = self.thisMObject()
        # aFalloff
        hFalloff = om.MRampAttribute(thisNode, self.aFalloff)

        a1 = om.MFloatArray()  # positions
        b1 = om.MFloatArray()  # values
        c1 = om.MIntArray()  # interpolations

        a1.append(float(0.0))
        a1.append(float(1.0))

        b1.append(float(0.0))
        b1.append(float(1.0))

        c1.append(om.MRampAttribute.kSmooth)
        c1.append(om.MRampAttribute.kSmooth)

        hFalloff.addEntries(a1, b1, c1)

        # aMaxDistanceUv
        hMaxDistUv = om.MRampAttribute(thisNode, self.aMaxDistanceUv)

        as1 = om.MFloatArray()  # positions
        bs1 = om.MFloatArray()  # values
        cs1 = om.MIntArray()  # interpolations

        as1.append(float(0.5))
        bs1.append(float(1.0))
        cs1.append(om.MRampAttribute.kSmooth)

        hMaxDistUv.addEntries(as1, bs1, cs1)

    # custom functions
    def getConnectedDagNode(self, attr_arg):
        plugArg = om.MPlug(self.thisMObject(), attr_arg)
        dagPath = om.MDagPath()
        if plugArg.isConnected():
            plugArr = om.MPlugArray()
            plugArg.connectedTo(plugArr, True, False)
            plugDag = om.MPlug(plugArr[0])
            oDagNode = plugDag.node()
            fnDagNode = om.MFnDagNode(oDagNode)
            fnDagNode.getPath(dagPath)
            return dagPath
        else:
            return None

    @staticmethod
    def debug_message(thisNode_arg, msg_arg):
        fnThis = om.MFnDependencyNode(thisNode_arg)
        nameThis = fnThis.name()
        mm.eval('warning "' + nameThis + '.debug: ' + msg_arg + '"')


def nodeInitializer():
    # default attr
    outgeoAr = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    # attribute type variables
    gAttr = om.MFnGenericAttribute()
    nAttr = om.MFnNumericAttribute()
    mAttr = om.MFnMatrixAttribute()
    rAttr = om.MRampAttribute()
    eAttr = om.MFnEnumAttribute()

    # aDebug
    prAttractNode.aDebug = eAttr.create("debug", "debug", 2)
    eAttr.setChannelBox(True)
    eAttr.addField("Off", 0)
    eAttr.addField("Warnings", 1)
    eAttr.addField("Show all", 2)
    prAttractNode.addAttribute(prAttractNode.aDebug)
    prAttractNode.attributeAffects(prAttractNode.aDebug, outgeoAr)
    # aMaxDistance
    prAttractNode.aMaxDistance = nAttr.create("maxDistance", "maxDistance", om.MFnNumericData.kFloat, 1)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    prAttractNode.addAttribute(prAttractNode.aMaxDistance)
    prAttractNode.attributeAffects(prAttractNode.aMaxDistance, outgeoAr)
    # aFalloff
    prAttractNode.aFalloff = rAttr.createCurveRamp("falloff", "falloff")
    prAttractNode.addAttribute(prAttractNode.aFalloff)
    prAttractNode.attributeAffects(prAttractNode.aFalloff, outgeoAr)
    # aMaxDistanceUv
    prAttractNode.aMaxDistanceUv = rAttr.createCurveRamp("maxDistanceUv", "maxDistanceUv")
    prAttractNode.addAttribute(prAttractNode.aMaxDistanceUv)
    prAttractNode.attributeAffects(prAttractNode.aMaxDistanceUv, outgeoAr)
    # aProjectOnNormal
    prAttractNode.aProjectOnNormal = nAttr.create("projectOnNormal", "projectOnNormal", om.MFnNumericData.kFloat, 0.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    prAttractNode.addAttribute(prAttractNode.aProjectOnNormal)
    prAttractNode.attributeAffects(prAttractNode.aProjectOnNormal, outgeoAr)
    # aNormalDirectionLimit
    prAttractNode.aNormalDirectionLimit = eAttr.create("normalDirectionLimit", "normalDirectionLimit", 0)
    eAttr.setKeyable(True)
    eAttr.addField("Off", 0)
    eAttr.addField("Only positive", 1)
    eAttr.addField("Only negative", 2)
    prAttractNode.addAttribute(prAttractNode.aNormalDirectionLimit)
    prAttractNode.attributeAffects(prAttractNode.aNormalDirectionLimit, outgeoAr)
    # aClosestVertex
    prAttractNode.aClosestVertex = nAttr.create("closestVertex", "closestVertex", om.MFnNumericData.kFloat, 0.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    prAttractNode.addAttribute(prAttractNode.aClosestVertex)
    prAttractNode.attributeAffects(prAttractNode.aClosestVertex, outgeoAr)

    # aInputShape
    prAttractNode.aInputShape = gAttr.create("inputShape", "inputShape")
    gAttr.setReadable(False)
    gAttr.addDataAccept(om.MFnNurbsCurveData.kNurbsCurve)
    gAttr.addDataAccept(om.MFnNurbsSurfaceData.kNurbsSurface)
    gAttr.addDataAccept(om.MFnMeshData.kMesh)
    prAttractNode.addAttribute(prAttractNode.aInputShape)
    prAttractNode.attributeAffects(prAttractNode.aInputShape, outgeoAr)
    # aInputMatrix
    prAttractNode.aInputMatrix = mAttr.create("inputMatrix", "inputMatrix")
    mAttr.setReadable(False)
    prAttractNode.addAttribute(prAttractNode.aInputMatrix)
    prAttractNode.attributeAffects(prAttractNode.aInputMatrix, outgeoAr)

    # paintable
    import maya.cmds as mc
    mc.makePaintable('prAttractNode', 'weights', attrType='multiFloat', shapeMode='deformer')


def nodeCreator():
    return OpenMayaMPx.asMPxPtr(prAttractNode())


def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Parzival Roethlein", "0.9.5")
    try:
        mplugin.registerNode(prAttractNode.pluginName, prAttractNode.pluginId, nodeCreator, nodeInitializer,
                             OpenMayaMPx.MPxNode.kDeformerNode)
    except:
        sys.stderr.write("Failed to register node: %s\n" % prAttractNode.pluginName)


def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(prAttractNode.pluginId)
    except:
        sys.stderr.write("Failed to unregister node: %s\n" % prAttractNode.pluginName)


# AEtemeplate for MRampAttributes and custom functions for deformer creation+connections
mm.eval('''
global proc AEprAttractNodeTemplate( string $nodeName )
{
    AEswatchDisplay $nodeName;
    editorTemplate -beginScrollLayout;
        // include/call base class/node attributes
        AEgeometryFilterCommon $nodeName;
        // custom attributes
        editorTemplate -beginLayout "prAttractNode Attributes" -collapse 0;
            editorTemplate -addControl "maxDistance";
            AEaddRampControl ($nodeName+".falloff");
            AEaddRampControl ($nodeName+".maxDistanceUv");
        editorTemplate -beginLayout "Normal Vector" -collapse 0;
            editorTemplate -addControl "projectOnNormal";
            editorTemplate -addControl "normalDirectionLimit";
        editorTemplate -beginLayout "Polygon Attractor" -collapse 0;
            editorTemplate -addControl "closestVertex";
        editorTemplate -endLayout;
        // add missing attrs (should be none)
        editorTemplate -addExtraControls;
        // node behavior
        AEgeometryFilterInclude $nodeName;
    editorTemplate -endScrollLayout;
    // hide attrs from 
    editorTemplate -suppress "weightList";
    editorTemplate -suppress "inputShape";
    editorTemplate -suppress "inputMatrix";
};

global proc prAttractNode()
{
    string $sel[] = `ls -sl -type "transform"`;
    if( size($sel) != 2 )
        error "Script requires two transforms to be selected.";
    
    string $driverShapes[] = `listRelatives -children $sel[0]`;
    string $drivenShapes[] = `listRelatives -children $sel[1]`;
    string $drivenShapeType = objectType($driverShapes[0]);
    if( $drivenShapeType != "mesh" &&
        $drivenShapeType != "nurbsCurve" &&
        $drivenShapeType != "nurbsSurface" )
        error ("Invalid driver shape type. Should be mesh/nurbsCurve/nurbsSurface, but got: "+objectType($driverShapes[0]));
    if( objectType($drivenShapes[0]) != "mesh" )
        error ("Invalid driven shape type. Should be mesh. Instead got: "+objectType($drivenShapes[0]));
    
    string $def[] = `deformer -type prAttractNode $sel[1]`;
    connectAttr( $sel[0]+".worldMatrix[0]", $def[0]+".inputMatrix" );
    if( $drivenShapeType == "mesh" )
        connectAttr( $driverShapes[0]+".outMesh", $def[0]+".inputShape" );
    else
        connectAttr( $driverShapes[0]+".local", $def[0]+".inputShape" );
};
''')
