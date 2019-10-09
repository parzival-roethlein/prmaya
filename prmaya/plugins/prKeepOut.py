"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Array version of Mayas "keepOut" with added features.
- get first intersection with shape from input[].position1 to input[].position2
- works with multiple default Maya surface types: mesh, nurbsSurface, primitives
- offset
- smooth collide
- smooth offset falloff

ATTRIBUTES
prKeepOut.enabled
prKeepOut.inputOffset
prKeepOut.inputGeometry[0]
prKeepOut.input[0]
prKeepOut.input[0].inputOffsetExtra
prKeepOut.input[0].inputGeometryExtra[0]
prKeepOut.input[0].inputPosition1
prKeepOut.input[0].inputPosition2
prKeepOut.input[0].inputParentInverseMatrix
prKeepOut.output[0].outputX
prKeepOut.output[0].outputY
prKeepOut.output[0].outputZ

LINKS
- Demo:
TODO
- Making-of:
TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
"""

import sys

import maya.api.OpenMaya as om


class prKeepOut(om.MPxNode):
    nodeTypeName = "prKeepOut"
    nodeTypeId = om.MTypeId(0x0004C268)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        genericAttr = om.MFnGenericAttribute()
        matrixAttr = om.MFnMatrixAttribute()

        # output
        prKeepOut.output = numericAttr.createPoint('output', 'output')
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        numericAttr.writable = False
        prKeepOut.addAttribute(prKeepOut.output)

        # input
        prKeepOut.inputEnabled = numericAttr.create('inputEnabled', 'inputEnabled', om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prKeepOut.addAttribute(prKeepOut.inputEnabled)
        prKeepOut.attributeAffects(prKeepOut.inputEnabled, prKeepOut.output)

        prKeepOut.inputOffset = numericAttr.create('inputOffset', 'inputOffset', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prKeepOut.addAttribute(prKeepOut.inputOffset)
        prKeepOut.attributeAffects(prKeepOut.inputOffset, prKeepOut.output)

        prKeepOut.inputGeometry = genericAttr.create('inputGeometry', 'inputGeometry')
        genericAttr.addDataType(om.MFnMeshData.kMesh)
        genericAttr.addDataType(om.MFnNurbsSurfaceData.kNurbsSurface)
        genericAttr.array = True
        prKeepOut.addAttribute(prKeepOut.inputGeometry)
        prKeepOut.attributeAffects(prKeepOut.inputGeometry, prKeepOut.output)

        prKeepOut.inputEnabledExtra = numericAttr.create('inputEnabledExtra', 'inputEnabledExtra', om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prKeepOut.inputOffsetExtra = numericAttr.create('inputOffsetExtra', 'inputOffsetExtra', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prKeepOut.inputPosition1 = numericAttr.createPoint('inputPosition1', 'inputPosition1')
        numericAttr.keyable = True
        prKeepOut.inputPosition2 = numericAttr.createPoint('inputPosition2', 'inputPosition2')
        numericAttr.keyable = True
        prKeepOut.inputGeometryExtra = genericAttr.create('inputGeometryExtra', 'inputGeometryExtra')
        genericAttr.addDataType(om.MFnMeshData.kMesh)
        genericAttr.addDataType(om.MFnNurbsSurfaceData.kNurbsSurface)
        genericAttr.array = True
        prKeepOut.inputParentInverseMatrix = matrixAttr.create('inputParentInverseMatrix', 'inputParentInverseMatrix')
        matrixAttr.keyable = True

        prKeepOut.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prKeepOut.inputEnabledExtra)
        compoundAttr.addChild(prKeepOut.inputOffsetExtra)
        compoundAttr.addChild(prKeepOut.inputPosition1)
        compoundAttr.addChild(prKeepOut.inputPosition2)
        compoundAttr.addChild(prKeepOut.inputGeometryExtra)
        compoundAttr.addChild(prKeepOut.inputParentInverseMatrix)
        compoundAttr.array = True
        prKeepOut.addAttribute(prKeepOut.input)
        prKeepOut.attributeAffects(prKeepOut.inputOffsetExtra, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.inputPosition1, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.inputPosition2, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.inputParentInverseMatrix, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.inputGeometryExtra, prKeepOut.output)

    @staticmethod
    def creator():
        return prKeepOut()

    def __init__(self):
        om.MPxNode.__init__(self)

    def displayWarning(self, error, index=None):
        nodeName = om.MFnDependencyNode(self.thisMObject()).name()
        if index is None:
            message = '"{0}": {1}'.format(nodeName, error)
        else:
            message = '"{0}.input[{1}]": {2}'.format(nodeName, index, error)
        om.MGlobal.displayWarning(message)

    def compute(self, plug, dataBlock):
        if plug not in [self.output]:
            self.displayWarning(error='Unknown plug: {}'.format(plug))
            return

        inputEnabled = dataBlock.inputValue(self.inputEnabled).asBool()
        offset = dataBlock.inputValue(self.inputOffset).asFloat()

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()

        indices = []
        raySources = []
        rayTargets = []
        rayDirections = []
        inverseMatrices = []
        offsets = []
        enableds = []

        # get rays
        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            inputTargetHandle = inputArrayHandle.inputValue()

            indices.append(inputArrayHandle.elementLogicalIndex())
            position1 = om.MFloatPoint(inputTargetHandle.child(self.inputPosition1).asFloat3())
            position2 = om.MFloatPoint(inputTargetHandle.child(self.inputPosition2).asFloat3())
            inverseMatrices.append(inputTargetHandle.child(self.inputParentInverseMatrix).asMatrix())
            offsets.append(offset+inputTargetHandle.child(self.inputOffsetExtra).asFloat())
            raySources.append(position1)
            rayTargets.append(position2)
            rayDirections.append(position2-position1)
            enableds.append(inputTargetHandle.child(self.inputEnabledExtra).asBool())

        closestHits = {i: None for i in indices}
        if inputEnabled:
            inputGeometryArrayHandle = dataBlock.inputArrayValue(self.inputGeometry)
            for i in range(len(inputGeometryArrayHandle)):
                inputGeometryArrayHandle.jumpToPhysicalElement(i)
                inputGeometryHandle = inputGeometryArrayHandle.inputValue()
                targetData = inputGeometryHandle.data()
                if targetData.isNull():
                    continue
                targetType = inputGeometryHandle.type()
                if targetType == om.MFnMeshData.kMesh:
                    meshFn = om.MFnMesh(targetData)
                    for index, raySource, rayDirection in zip(indices, raySources, rayDirections):
                        closestHit = meshFn.closestIntersection(raySource, rayDirection, om.MSpace.kWorld, 1, False)[0]
                        if closestHit != om.MFloatPoint():
                            if closestHits[index] is None:
                                closestHits[index] = closestHit
                            elif (closestHit - raySource).length() < (closestHits[index] - raySource).length():
                                closestHits[index] = closestHit
                elif targetType == om.MFnNurbsSurfaceData.kNurbsSurface:
                    pass

        # set output
        for index, hit in closestHits.iteritems():
            output_handle = output_builder.addElement(index)
            if hit is None:
                hit = rayTargets[indices.index(index)]
            output_handle.set3Float(hit[0], hit[1], hit[2])

        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prKeepOut.nodeTypeName, prKeepOut.nodeTypeId, prKeepOut.creator, prKeepOut.initialize)
    except:
        sys.stderr.write('Failed to register node: %s' % prKeepOut.nodeTypeName)
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prKeepOut.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: %s' % prKeepOut.nodeTypeName)
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprKeepOutTemplate(string $nodeName)
    {
        AEswatchDisplay $nodeName;
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prKeepOut Attributes" -collapse 0;
                editorTemplate -label "inputEnabled" -addControl "inputEnabled";
                editorTemplate -label "inputOffset" -addControl "inputOffset";
                editorTemplate -label "input" -addControl "input";
                editorTemplate -label "inputGeometry" -addControl "inputGeometry";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "input.inputGeometryExtra"; // not working
        editorTemplate -suppress "input.inputParentInverseMatrix"; // not working
        //editorTemplate -suppress "output";
    };
    ''')

