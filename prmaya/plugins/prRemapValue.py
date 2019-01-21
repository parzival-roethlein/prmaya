"""
DESCRIPTION
array version of maya default remapValue node

USE CASES
...

USAGE
...

ATTRIBUTES
...

LINKS
...

TODO


"""

import sys
import math

import maya.api.OpenMaya as om
import maya.cmds as mc


class prRemapValue(om.MPxNode):
    nodeTypeName = "prRemapValue"
    nodeTypeId = om.MTypeId(0x0004C263)  # local, not save
    
    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        rampAttr = om.MRampAttribute()
        
        # output
        prRemapValue.outValue = numericAttr.create('outValue', 'outValue', om.MFnNumericData.kFloat)
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        # numericAttr.storable = False
        
        # input
        prRemapValue.inputValue = numericAttr.create('inputValue', 'inputValue', om.MFnNumericData.kFloat)
        numericAttr.array = True
        prRemapValue.addAttribute(prRemapValue.inputValue)
        prRemapValue.attributeAffects(prRemapValue.inputValue, prRemapValue.outValue)

        # settings
        prRemapValue.value = rampAttr.createCurveRamp('value', 'value')
        prRemapValue.addAttribute(prRemapValue.value)
        prRemapValue.attributeAffects(prRemapValue.value, prRemapValue.outValue)
    
    @staticmethod
    def creator():
        return prRemapValue()
    
    def __init__(self):
        om.MPxNode.__init__(self)
    
    def compute(self, plug, dataBlock):
        thisNode = self.thisMObject()
        if plug not in [prRemapValue.outValue]:
            print 'unknown plug: {}'.format(plug)
            return
        
        counter = dataBlock.inputValue(prRemapValue.counter).asInt()
        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        
        distributionEnabled = dataBlock.inputValue(self.distributionEnabled).asBool()
        if distributionEnabled:
            distribution = om.MRampAttribute(thisNode, self.distribution)
        
        outputArrayHandle = dataBlock.outputArrayValue(self.output)
        outputBuilder = outputArrayHandle.builder()
        
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            outputHandle = outputBuilder.addElement(index)
            outputArrayHandle.set(outputBuilder)
            inputHandle = inputArrayHandle.inputValue()
            curveHandle = inputHandle.child(self.inputCurve)
            curveData = curveHandle.data()
            if curveData.isNull():
                continue
            
            curveFn = om.MFnNurbsCurve(curveData)
            curveLength = curveFn.length()
            stepLength = 1.0 / (counter - 1 if counter > 2 else 1)
            positions = []
            tangents = []
            for x in range(counter):
                if distributionEnabled:
                    distributionValue = distribution.getValueAtPosition(x * stepLength)
                    parameter = curveFn.findParamFromLength(distributionValue * curveLength)
                else:
                    parameter = curveFn.findParamFromLength(x * stepLength * curveLength)
                positions.append(curveFn.getPointAtParam(parameter, space=om.MSpace.kWorld))
                tangents.append(curveFn.tangent(parameter, space=om.MSpace.kWorld))
            
            outTranslateArrayHandle = om.MArrayDataHandle(outputHandle.child(self.outputTranslate))
            outTranslateBuilder = outTranslateArrayHandle.builder()
            for x, position in enumerate(positions):
                outTranslateHandle = outTranslateBuilder.addElement(x)
                outTranslateHandle.set3Float(position[0], position[1], position[2])
            outTranslateArrayHandle.set(outTranslateBuilder)
            outTranslateArrayHandle.setAllClean()
            
            if plug == prRemapValue.outputMatrix:
                # TODO FIX TEMP CODE
                worldUpMatrix = inputHandle.child(self.worldUpMatrix).asMatrix()
                normals = [om.MVector(list(worldUpMatrix)[4:7])]
                bitangents = [om.MVector(list(worldUpMatrix)[7:10])]
                for x in range(counter - 1):
                    bitangent = tangents[x] ^ tangents[x + 1]
                    if bitangent.length() == 0:
                        normal = normals[x]
                    else:
                        bitangent.normalize()
                        angle = math.radians(math.acos(tangents[x] * tangents[x + 1]))
                        normal = normals[x].rotateBy(om.MQuaternion(angle, bitangent))
                        # normal = normal[x] * getRotationMatrix(angle, bitangent)
                    normals.append(normal)
                    bitangents.append(bitangent)
                outputMatrixArrayHandle = om.MArrayDataHandle(outputHandle.child(self.outputMatrix))
                outputMatrixBuilder = outputMatrixArrayHandle.builder()
                for x in range(counter):
                    matrix = om.MMatrix((list(tangents[x]) + [0],
                                         list(normals[x]) + [0],
                                         list(bitangents[x]) + [0],
                                         list(positions[x])))
                    outputMatrixHandle = outputMatrixBuilder.addElement(x)
                    outputMatrixHandle.setMMatrix(matrix)
                outputMatrixArrayHandle.set(outputMatrixBuilder)
                outputMatrixArrayHandle.setAllClean()
        
        # outputArrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prRemapValue.nodeTypeName, prRemapValue.nodeTypeId,
                              prRemapValue.creator, prRemapValue.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prRemapValue.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prRemapValue.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prRemapValue.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprRemapValueTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prRemapValue Attributes" -collapse 0;
                editorTemplate -label "inputValue" -addControl "inputValue";
                AEaddRampControl ($nodeName+".value");
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "output";
    };
    ''')

