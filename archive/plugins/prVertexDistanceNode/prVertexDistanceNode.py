'''
########################################################################
#                                                                      #
#             prVertexDistanceNode.py                                  #
#                                                                      #
#             Copyright (C) 2011  Parzival Roethlein                   #
#                                                                      #
#             Email: pa.roethlein@gmail.com                            #
#                                                                      #
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# This program is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# See http://www.gnu.org/licenses/gpl.html for a copy of the GNU       #
# General Public License.                                              #
#                                                                      #
########################################################################


V E R S I O N S:
2011-01-25 / 0.9.0: release
2011-02-03 / 0.9.1: switched distances from object- to world-space
2011-02-12 / 0.9.1: added c++ code and .mll for maya (win32): 2009, 2011 


D E S C R I P T I O N:
- Calculates the distance between vertex-pairs.
- This can be useful when driving corrective blendShapes that can not be 
  driven by a single/few attribute(s).
- May also be useful as Python API example with input and output arrays.


A T T R I B U T E S:
input:
- vertex: 2D-array, for vertex pairs
-- myNode.vertex[0].vertex0, myNode.vertex[0].vertex1
- divide: divides all distance values
-- myNode.divide
output:
- distance: 1D-array
-- myNode.distance[0]


U S A G E:
First load the plug-in via Window->Settings->Prefs->Plug-in Manager
Then you should be able to normally apply the deformer:
(With mesh selected) execute (MEL): deformer -type "prVertexDistanceNode"


F E E D B A C K:
Bugs, questions and suggestions to pa.roethlein@gmail.com


'''
'''

# test plug-in (with plug-in loaded)
def prTestVertexDistance():
    import maya.cmds as mc
    mc.file(new=True, f=True)
    #mc.unloadPlugin( "prVertexDistanceNode.py" )
    #mc.loadPlugin( "prVertexDistanceNode.py" )
    myPlane = mc.polyPlane(ch=0, sx=1, sy=1, width=4, height=4)[0]
    mc.move( 2, 0, 0, myPlane+".vtx[*]", r=True )
    mc.distanceDimension( sp=(0,0,3.5), ep=(1,0,3.5) )
    mc.distanceDimension( sp=(0,0,-3.5), ep=(1,0,-3.5) )
    mc.select( myPlane )
    myDeformer = mc.deformer( type='prVertexDistanceNode' )[0]
    mc.setAttr( myDeformer+'.vertex[0].vertex0', 0 )
    mc.setAttr( myDeformer+'.vertex[0].vertex1', 1 )
    mc.connectAttr( myDeformer+".distance[0]", "locator2.tx")
prTestVertexDistance()

'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeTypeName = "prVertexDistanceNode"
vertexDistanceNodeId = OpenMaya.MTypeId(0x0010A519)

# node definition
class prVertexDistanceNode(OpenMayaMPx.MPxDeformerNode):
    # class variables / attributes
    aDivide = OpenMaya.MObject()
    aVertex = OpenMaya.MObject()
    aDistance = OpenMaya.MObject()
    
    # constructor
    def __init__(self):
    	OpenMayaMPx.MPxDeformerNode.__init__(self)
    
    # deform
    def deform(self,dataBlock,geomIter,matrix,multiIndex):
        # get input mesh 
        hInput = dataBlock.outputArrayValue( self.input )
        hInput.jumpToElement( multiIndex )
        hInputGeom = hInput.outputValue().child( self.inputGeom )
        oInputGeom = hInputGeom.asMesh()
        fnPoint = OpenMaya.MFnMesh( oInputGeom )
        # attribute handles
        hDivide = dataBlock.inputValue( self.aDivide )
        hVertex = dataBlock.inputArrayValue( self.aVertex )
        hDistance = dataBlock.outputArrayValue( self.aDistance )
        # attribute values
        vDivide = hDivide.asFloat()
        # MArrayDataBuilder: 
        #    value of third argument (numElements) does not seem to matter (in Python ?!)
        dbDistance = OpenMaya.MArrayDataBuilder( dataBlock, self.aDistance, hVertex.elementCount() )
        # calculate (loop through vertex 2D-array)
        for x in range( hVertex.elementCount() ):
            hVertex.jumpToArrayElement( x )
            # get vertices
            iVtx0, iVtx1 = hVertex.inputValue().asInt2()
            p1 = OpenMaya.MPoint()
            p2 = OpenMaya.MPoint()
            fnPoint.getPoint(iVtx0, p1, OpenMaya.MSpace.kWorld )
            fnPoint.getPoint(iVtx1, p2, OpenMaya.MSpace.kWorld )
            # calculate distance
            vecP1toP2 = OpenMaya.MVector( p1.x-p2.x, p1.y-p2.y, p1.z-p2.z  )
            fDistance = vecP1toP2.length() / vDivide
            # set distance
            hDistanceBuilder = dbDistance.addElement( hVertex.elementIndex() )
            hDistanceBuilder.setFloat( fDistance )
            hDistance.set( dbDistance )
    # end deform
#

# creator
def nodeCreator():
	return OpenMayaMPx.asMPxPtr( prVertexDistanceNode() )

# initializer
def nodeInitializer():
    # add attributes
    nAttr = OpenMaya.MFnNumericAttribute()
    #    aDivide
    prVertexDistanceNode.aDivide = nAttr.create( "divide", "div", OpenMaya.MFnNumericData.kFloat, 1.0 )
    nAttr.setKeyable(True)
    prVertexDistanceNode.addAttribute( prVertexDistanceNode.aDivide )
    #    aVertex
    prVertexDistanceNode.aVertex = nAttr.create( "vertex", "vtx", OpenMaya.MFnNumericData.k2Int )
    nAttr.setArray(True)
    nAttr.setUsesArrayDataBuilder(True)
    prVertexDistanceNode.addAttribute( prVertexDistanceNode.aVertex )
    #    aDistance
    nAttr = OpenMaya.MFnNumericAttribute()
    prVertexDistanceNode.aDistance = nAttr.create( "distance", "dst", OpenMaya.MFnNumericData.kFloat )
    nAttr.setStorable(False)
    nAttr.setWritable(False)
    nAttr.setArray(True)
    nAttr.setUsesArrayDataBuilder(True)
    prVertexDistanceNode.addAttribute( prVertexDistanceNode.aDistance )
    # affects
    prVertexDistanceNode.attributeAffects(prVertexDistanceNode.aVertex, prVertexDistanceNode.aDistance)
    prVertexDistanceNode.attributeAffects(prVertexDistanceNode.aDivide, prVertexDistanceNode.aDistance)
    
    inputAr = OpenMayaMPx.cvar.MPxDeformerNode_input
    prVertexDistanceNode.attributeAffects(inputAr, prVertexDistanceNode.aDistance)
    
    outgeoAr = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    prVertexDistanceNode.attributeAffects(prVertexDistanceNode.aVertex, outgeoAr)
    prVertexDistanceNode.attributeAffects(prVertexDistanceNode.aDivide, outgeoAr)

# initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject, "Parzival Roethlein", "0.9.1")
	try:
		mplugin.registerNode( kPluginNodeTypeName, vertexDistanceNodeId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kDeformerNode )
	except:
		sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterNode( vertexDistanceNodeId )
	except:
		sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )