"""
DESCRIPTION
"Parallel Transport Approach to Curve Framing"
https://pdfs.semanticscholar.org/7e65/2313c1f8183a0f43acce58ae8d8caf370a6b.pdf
Tutorial:
https://vimeo.com/251091418

USE CASES

USAGE

ATTRIBUTES

LINKS



TODO:
make creation script work with double array outputs
translation distribution ramp attr

TODO LATER :
nodeState / frozen functionality
outputMatrix:
- make upMatrix upVector perpendicular to first tangent
- fix unstable twist when rotations are zero
- user defined aim+up vector

TODO MAYBE:
- (input[x] -> output[x]) index based dirty propagation
- check if outputMatrix to MFnData.kMatrixArray ?
- aetemplate outputMatrix scroll layout
"""

import sys
import math

import maya.api.OpenMaya as om
import maya.cmds as mc


class prCurveMatrix(om.MPxNode):
    nodeTypeName = "prCurveMatrix"
    nodeTypeId = om.MTypeId(0x0004C261)  # local, not save

    @staticmethod
    def initialize():
        typedAttr = om.MFnTypedAttribute()
        matrixAttr = om.MFnMatrixAttribute()
        numericAttr = om.MFnNumericAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        
        # output
        prCurveMatrix.outputTranslate = numericAttr.createPoint('outputTranslate', 'outputTranslate')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        numericAttr.storable = False
        
        prCurveMatrix.outputMatrix = matrixAttr.create('outputMatrix', 'outputMatrix',
                                                       matrixAttr.kDouble)
        matrixAttr.array = True
        matrixAttr.usesArrayDataBuilder = True
        matrixAttr.writable = False
        matrixAttr.storable = False

        prCurveMatrix.output = compoundAttr.create('output', 'output')
        compoundAttr.addChild(prCurveMatrix.outputTranslate)
        compoundAttr.addChild(prCurveMatrix.outputMatrix)
        compoundAttr.array = True
        compoundAttr.usesArrayDataBuilder = True
        prCurveMatrix.addAttribute(prCurveMatrix.output)
        
        # global settings
        prCurveMatrix.counter = numericAttr.create('counter', 'counter', om.MFnNumericData.kInt, 5)
        numericAttr.keyable = True
        prCurveMatrix.addAttribute(prCurveMatrix.counter)
        prCurveMatrix.attributeAffects(prCurveMatrix.counter, prCurveMatrix.outputTranslate)
        prCurveMatrix.attributeAffects(prCurveMatrix.counter, prCurveMatrix.outputMatrix)
        
        # input
        prCurveMatrix.worldUpMatrix = matrixAttr.create('worldUpMatrix', 'worldUpMatrix',
                                                        matrixAttr.kDouble)
        
        prCurveMatrix.inputCurve = typedAttr.create('inputCurve', 'inputCurve',
                                                    om.MFnNurbsCurveData.kNurbsCurve)
        
        prCurveMatrix.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prCurveMatrix.worldUpMatrix)
        compoundAttr.addChild(prCurveMatrix.inputCurve)
        compoundAttr.array = True
        prCurveMatrix.addAttribute(prCurveMatrix.input)
        prCurveMatrix.attributeAffects(prCurveMatrix.inputCurve, prCurveMatrix.outputTranslate)
        prCurveMatrix.attributeAffects(prCurveMatrix.inputCurve, prCurveMatrix.outputMatrix)
        prCurveMatrix.attributeAffects(prCurveMatrix.worldUpMatrix, prCurveMatrix.outputTranslate)
        prCurveMatrix.attributeAffects(prCurveMatrix.worldUpMatrix, prCurveMatrix.outputMatrix)
    
    @staticmethod
    def creator():
        return prCurveMatrix()
    
    def __init__(self):
        om.MPxNode.__init__(self)
    
    def compute(self, plug, dataBlock):
        # print '\nplug : {}'.format(plug)
        if (plug != prCurveMatrix.output and plug != prCurveMatrix.outputMatrix and
                plug != prCurveMatrix.outputTranslate):
            return
        
        counter = dataBlock.inputValue(prCurveMatrix.counter).asInt()
        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        outputArrayHandle = dataBlock.outputArrayValue(self.output)
        outputBuilder = outputArrayHandle.builder()
        
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            inputHandle = inputArrayHandle.inputValue()
            curveHandle = inputHandle.child(self.inputCurve)
            curveData = curveHandle.data()
            
            index = inputArrayHandle.elementLogicalIndex()
            outputHandle = outputBuilder.addElement(index)
            outputArrayHandle.set(outputBuilder)
            
            if curveData.isNull():
                # print '{0} : no curve'.format(index)
                continue
            # print '{0} : curve'.format(index)
            
            curveFn = om.MFnNurbsCurve(curveData)
            stepLength = curveFn.length() / (counter-1)  # TODO make it work for counter < 2
            positions = []
            tangents = []
            for x in range(counter):
                parameter = curveFn.findParamFromLength(x*stepLength)
                positions.append(curveFn.getPointAtParam(parameter, space=om.MSpace.kWorld))
                tangents.append(curveFn.tangent(parameter, space=om.MSpace.kWorld))
            
            outputTranslateArrayHandle = om.MArrayDataHandle(outputHandle.child(self.outputTranslate))
            outputTranslateBuilder = outputTranslateArrayHandle.builder()
            for x, position in enumerate(positions):
                outputTranslateHandle = outputTranslateBuilder.addElement(x)
                outputTranslateHandle.set3Float(position[0], position[1], position[2])
            outputTranslateArrayHandle.set(outputTranslateBuilder)
            outputTranslateArrayHandle.setAllClean()
            
            # TODO WIP START
            worldUpMatrix = inputHandle.child(self.worldUpMatrix).asMatrix()
            normals = [om.MVector(list(worldUpMatrix)[4:7])]
            bitangents = [om.MVector(list(worldUpMatrix)[7:10])]
            for x in range(counter-1):
                bitangent = tangents[x] ^ tangents[x+1]
                if bitangent.length() == 0:
                    normal = normals[x]
                else:
                    bitangent.normalize()
                    angle = math.radians(math.acos(tangents[x] * tangents[x+1]))
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
            # TODO WIP END
            
        # print('output len : {}'.format(len(outputArrayHandle)))
        # outputArrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.2')
    try:
        pluginFn.registerNode(prCurveMatrix.nodeTypeName, prCurveMatrix.nodeTypeId,
                              prCurveMatrix.creator, prCurveMatrix.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prCurveMatrix.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prCurveMatrix.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prCurveMatrix.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprCurveMatrixTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prPyMath Attributes" -collapse 0;
                editorTemplate -label "counter" -addControl "counter";
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "output";
    };
    ''')


def fromCurves(curves=None):
    """create one curveMatrix for all curves"""
    curves = (mc.ls(curves, type=['transform', 'nurbsCurve']) or
              mc.ls(sl=True, type=['transform', 'nurbsCurve']))
    if not curves:
        return None
    curveMatrix = mc.createNode('prCurveMatrix')
    for x, curve in enumerate(curves):
        mc.connectAttr('{0}.worldSpace'.format(curve),
                       '{0}.input[{1}].inputCurve'.format(curveMatrix, x))
    return curveMatrix


def fromEachCurve(curves=None):
    """create one curveMatrix for each curve"""
    curveMatrices = []
    curves = (mc.ls(curves, type=['transform', 'nurbsCurve']) or
              mc.ls(sl=True, type=['transform', 'nurbsCurve']))
    for curve in curves:
        curveMatrices.append(fromCurves(curve))
    return curveMatrices


def getConnectedInputIndices(curveMatrix):
    """return all .input[x] indices with connected inputCurve"""
    indices = []
    for index in mc.getAttr('{0}.input'.format(curveMatrix), multiIndices=True):
        if not mc.listConnections('{0}.input[{1}].inputCurve'.format(curveMatrix, index), destination=False):
            continue
        indices.append(index)
    return indices


def transformFromOutputTranslate(curveMatrix=None, transformType='locator'):
    """create a connected transform for each output.outputTranslate"""
    curveMatrix = (mc.ls(curveMatrix, type='prCurveMatrix') or
                   mc.ls(sl=True, type='prCurveMatrix') or
                   [None])[0]
    locators = []
    if not curveMatrix:
        return locators
    for index in getConnectedInputIndices(curveMatrix):
        for x in range(mc.getAttr('{0}.counter'.format(curveMatrix))):
            transform = mc.createNode(transformType)
            if mc.ls(transform, type='shape'):
                transform = mc.listRelatives(transform, parent=True)[0]
            mc.connectAttr('{0}.output[{1}].outputTranslate[{2}]'.format(curveMatrix, index, x),
                           '{0}.translate'.format(transform))
            mc.rename(transform,
                      '{0}_output{1}_translate{2}_{3}'.format(curveMatrix, index, x, transformType))
    return locators


def transformFromOutputMatrix(curveMatrix=None, transformType='locator', showLocalAxis=True):
    """create a connected transform for each output.outputMatrix"""
    curveMatrix = (mc.ls(curveMatrix, type='prCurveMatrix') or
                   mc.ls(sl=True, type='prCurveMatrix') or
                   [None])[0]
    transforms = []
    for index in getConnectedInputIndices(curveMatrix):
        for x in range(mc.getAttr('{0}.counter'.format(curveMatrix))):
            decomposeMat = mc.createNode('decomposeMatrix')
            decomposeMat = mc.rename(decomposeMat,
                                     '{0}_output{1}_matrix{2}_decomposeMatrix'.format(curveMatrix, index, x))
            mc.connectAttr('{0}.output[{1}].outputMatrix[{2}]'.format(curveMatrix, index, x),
                           '{0}.inputMatrix'.format(decomposeMat))
            if transformType:
                transform = mc.createNode(transformType)
                if mc.ls(transform, type='shape'):
                    transform = mc.listRelatives(transform, parent=True)[0]
                mc.connectAttr('{0}.outputTranslate'.format(decomposeMat),
                               '{0}.translate'.format(transform))
                mc.connectAttr('{0}.outputRotate'.format(decomposeMat),
                               '{0}.rotate'.format(transform))
                mc.rename(transform,
                          '{0}_output{1}_matrix{2}_{3}'.format(curveMatrix, index, x, transformType))
                transforms.append(transform)
    mc.toggle(transforms, localAxis=showLocalAxis)
    return transforms

