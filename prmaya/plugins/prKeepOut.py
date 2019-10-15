"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Array version of Mayas "keepOut" with changed/added features.
- Instead of one ray and one target muscleSkin, unlimited number of rays with unlimited number of surfaces
- Defines intersection ray from two positions (start, end) instead of a position + vector
- Works with default Maya surfaces instead of converting to muscleSkin
- parentInverseMatrix to adjust output to target space
- TODO support nurbsSurfaces and primitives as inputGeometry
- TODO smooth collide
- TODO smooth offset falloff

ATTRIBUTES
prKeepOut.enabled
prKeepOut.offset
prKeepOut.inputGeometry[0]
prKeepOut.input[0]
prKeepOut.input[0].enabledExtra
prKeepOut.input[0].offsetExtra
prKeepOut.input[0].inputGeometryExtra[0]
prKeepOut.input[0].position1
prKeepOut.input[0].position2
prKeepOut.input[0].parentInverseMatrix
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
        prKeepOut.enabled = numericAttr.create('enabled', 'enabled', om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prKeepOut.addAttribute(prKeepOut.enabled)
        prKeepOut.attributeAffects(prKeepOut.enabled, prKeepOut.output)

        prKeepOut.offsetExtendsPositions = numericAttr.create('offsetExtendsPositions', 'offsetExtendsPositions', om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prKeepOut.addAttribute(prKeepOut.offsetExtendsPositions)
        prKeepOut.attributeAffects(prKeepOut.offsetExtendsPositions, prKeepOut.output)

        prKeepOut.offset = numericAttr.create('offset', 'offset', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prKeepOut.addAttribute(prKeepOut.offset)
        prKeepOut.attributeAffects(prKeepOut.offset, prKeepOut.output)

        prKeepOut.inputGeometry = genericAttr.create('inputGeometry', 'inputGeometry')
        genericAttr.addDataType(om.MFnMeshData.kMesh)
        genericAttr.addDataType(om.MFnNurbsSurfaceData.kNurbsSurface)
        genericAttr.array = True
        prKeepOut.addAttribute(prKeepOut.inputGeometry)
        prKeepOut.attributeAffects(prKeepOut.inputGeometry, prKeepOut.output)

        prKeepOut.enabledExtra = numericAttr.create('enabledExtra', 'enabledExtra', om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prKeepOut.offsetExtra = numericAttr.create('offsetExtra', 'offsetExtra', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prKeepOut.position1 = numericAttr.createPoint('position1', 'position1')
        numericAttr.keyable = True
        prKeepOut.position2 = numericAttr.createPoint('position2', 'position2')
        numericAttr.keyable = True
        prKeepOut.inputGeometryExtra = genericAttr.create('inputGeometryExtra', 'inputGeometryExtra')
        genericAttr.addDataType(om.MFnMeshData.kMesh)
        genericAttr.addDataType(om.MFnNurbsSurfaceData.kNurbsSurface)
        genericAttr.array = True
        prKeepOut.parentInverseMatrix = matrixAttr.create('parentInverseMatrix', 'parentInverseMatrix', type=matrixAttr.kFloat)
        matrixAttr.keyable = True

        prKeepOut.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prKeepOut.enabledExtra)
        compoundAttr.addChild(prKeepOut.offsetExtra)
        compoundAttr.addChild(prKeepOut.position1)
        compoundAttr.addChild(prKeepOut.position2)
        compoundAttr.addChild(prKeepOut.inputGeometryExtra)
        compoundAttr.addChild(prKeepOut.parentInverseMatrix)
        compoundAttr.array = True
        prKeepOut.addAttribute(prKeepOut.input)
        prKeepOut.attributeAffects(prKeepOut.enabledExtra, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.offsetExtra, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.position1, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.position2, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.parentInverseMatrix, prKeepOut.output)
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

        enabled = dataBlock.inputValue(self.enabled).asBool()
        offsetExtendsPositions = dataBlock.inputValue(self.offsetExtendsPositions).asBool()
        offset = dataBlock.inputValue(self.offset).asFloat()

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()

        indices = []
        position1_list = []
        position2_list = []
        inverseMatrices = {}
        finalOffsets = []
        enablesExtra = []

        raySources = []
        rayDirections = []

        # get rays
        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            inputTargetHandle = inputArrayHandle.inputValue()
            index = inputArrayHandle.elementLogicalIndex()
            indices.append(index)
            position1 = om.MFloatPoint(inputTargetHandle.child(self.position1).asFloat3())
            position1_list.append(position1)
            position2 = om.MFloatPoint(inputTargetHandle.child(self.position2).asFloat3())
            position2_list.append(position2)
            finalOffset = offset + inputTargetHandle.child(self.offsetExtra).asFloat()
            raySource = position1
            rayDirection = position2 - position1
            if offsetExtendsPositions and finalOffset:
                offsetVector = rayDirection.normal() * finalOffset
                if finalOffset > 0:
                    rayDirection += offsetVector
                elif finalOffset < 0:
                    raySource += offsetVector
            raySources.append(raySource)
            rayDirections.append(rayDirection)
            finalOffsets.append(finalOffset)
            inverseMatrices[index] = inputTargetHandle.child(self.parentInverseMatrix).asFloatMatrix()
            enablesExtra.append(inputTargetHandle.child(self.enabledExtra).asBool())

        closestHits = {i: None for i in indices}
        offsetVectors = {i: None for i in indices}
        if enabled:
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
                    for index, raySource, rayDirection, finalOffset, enabledExtra in zip(
                            indices, raySources, rayDirections, finalOffsets, enablesExtra):
                        if not enabledExtra:
                            continue
                        hit = meshFn.closestIntersection(raySource, rayDirection, om.MSpace.kWorld, 1, False)[0]
                        if hit == om.MFloatPoint():
                            continue
                        if closestHits[index] is None or \
                                (hit - raySource).length() < (closestHits[index] - raySource).length():
                            closestHits[index] = hit
                            if finalOffset:
                                closestHitVector = raySource - hit
                                if finalOffset > closestHitVector.length():
                                    offsetVectors[index] = closestHitVector
                                else:
                                    offsetVectors[index] = closestHitVector.normal() * finalOffset
                elif targetType == om.MFnNurbsSurfaceData.kNurbsSurface:
                    pass

        # set output
        for index, hit in closestHits.iteritems():
            output_handle = output_builder.addElement(index)
            if hit is None:
                hit = position2_list[indices.index(index)]
            elif offsetVectors[index]:
                hit += offsetVectors[index]
            hit *= inverseMatrices[index]
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
                editorTemplate -label "enabled" -addControl "enabled";
                editorTemplate -label "offset" -addControl "offset";
                editorTemplate -label "input" -addControl "input";
                editorTemplate -label "inputGeometry" -addControl "inputGeometry";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        //editorTemplate -suppress "input.inputGeometryExtra"; // not working
        //editorTemplate -suppress "input.parentInverseMatrix"; // not working
        //editorTemplate -suppress "output";
    };
    ''')

