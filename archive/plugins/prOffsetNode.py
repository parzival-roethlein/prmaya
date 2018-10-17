'''
########################################################################
#                                                                      #
#             prOffsetNode.py                                          #
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

D E S C R I P T I O N:
- Open source Maya plug-in (deformer) implemented with Python.
- Python version of the offsetNode.cpp that comes with the Maya API Devkit.
- May help someone at learning the Python API syntax.
- Specifically "deform", "accessoryAttribute" and "accessoryNodeSetup". 

V E R S I O N S:
2011-02-10 / 0.9.0: created

U S A G E:
First load the plug-in via Window->Settings->Prefs->Plug-in Manager
Then you should be able to normally apply the deformer:
(With mesh selected) execute (MEL): deformer -type "prOffsetNode"

F E E D B A C K:
Bugs, questions and suggestions to pa.roethlein@gmail.com

T E S T:
- To test the plug-in, execute the following code in the script editor (Python tab):
# #########################
def prOffsetNodeTest():
    import maya.cmds as mc
    mc.file(new=True, f=True)
    mc.unloadPlugin( "prOffsetNode.py" )
    mc.loadPlugin( "prOffsetNode.py" )
    myCube = mc.polyCube(ch=0)[0]
    myOffsetNode = mc.deformer( type='prOffsetNode' )[0]
prOffsetNodeTest()
# #########################
'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeTypeName = "prOffsetNode"
offsetNodeId = OpenMaya.MTypeId(0x0010A518)# not save

# node definition
class prOffsetNode(OpenMayaMPx.MPxDeformerNode):
    # class variables / attributes
    aOffsetMatrix = OpenMaya.MObject()
    
    # constructor
    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
    
    # automatically create locator
    def accessoryNodeSetup( self, cmd ):
        objLoc = cmd.createNode( 'locator', OpenMaya.MObject().kNullObj )
        fnLoc = OpenMaya.MFnDependencyNode( objLoc )
        attrMat = fnLoc.attribute( 'matrix' )
        result = cmd.connect( objLoc, attrMat, self.thisMObject(), self.aOffsetMatrix )
        return result# unnecessary in python?
    
    # deletes deformer if node that is connected to self.aOffsetMatrix is deleted
    def accessoryAttribute( self ):
        return self.aOffsetMatrix
    
    # functionality
    def deform(self,block,iter,m,multiIndex):
        # attribute handles
        hEnvelope = block.inputValue( OpenMayaMPx.cvar.MPxDeformerNode_envelope )
        hOffsetMatrix = block.inputValue( self.aOffsetMatrix )
        # attribute values
        env = hEnvelope.asFloat()
        omat = hOffsetMatrix.asMatrix()
        omatinv = omat.inverse()
        # loop
        while not iter.isDone():
            pt = iter.position()
            pt *= omatinv
            
            weight = self.weightValue( block, multiIndex, iter.index() )
            
            # offset algorithm
            pt.y = pt.y + env*weight
            
            pt *= omat
            iter.setPosition(pt)
            iter.next()
        # end while
        #return OpenMaya.MStatus.kSuccess# can be skipped in python
    # end deform
# end class

# creator
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( prOffsetNode() )

# initializer
def nodeInitializer():
    # add attributes
    nAttr = OpenMaya.MFnMatrixAttribute()
    #    aDivide
    prOffsetNode.aOffsetMatrix = nAttr.create( "locateMatrix", "lm" )
    nAttr.setConnectable(True)
    prOffsetNode.addAttribute( prOffsetNode.aOffsetMatrix )
    # affects
    outgeoAr = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
    prOffsetNode.attributeAffects(prOffsetNode.aOffsetMatrix, outgeoAr)

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Parzival Roethlein", "0.9.0")
    try:
        mplugin.registerNode( kPluginNodeTypeName, offsetNodeId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kDeformerNode )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( offsetNodeId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )