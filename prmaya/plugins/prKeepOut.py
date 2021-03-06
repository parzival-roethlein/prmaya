"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Improved array version of Mayas "keepOut" node
Array:
- unlimited number of rays per node instead of just one
- unlimited number of target shapes instead of just one
Improvements:
- uses standard maya shapes as targets (mesh, nurbsSurface) instead one muscleSkin
- Intersection ray generated from two positions (start, end) instead of a position + vector
- parentInverseMatrix to put the output translation into the driven transform space
- offsetExtendsPosition: extend position1 for ray calculations with negative offset

ATTRIBUTES
prKeepOut.enabled
prKeepOut.offset
prKeepOut.offsetExtendsPosition
prKeepOut.inputGeometry[0]
prKeepOut.input[0]
prKeepOut.input[0].enabledExtra
prKeepOut.input[0].offsetExtra
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
https://pazrot3d.blogspot.com/2019/12/prkeepoutpy-making-of.html
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- nurbsSurface currently only works in objectSpace (maya bug?)
- make enabled a blendable attribute
- support primitives as inputGeometry
- smooth collide
- smooth offset falloff
- optimize/cleanup (at the very end!!!!)
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

        prKeepOut.offset = numericAttr.create('offset', 'offset', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        prKeepOut.addAttribute(prKeepOut.offset)
        prKeepOut.attributeAffects(prKeepOut.offset, prKeepOut.output)

        prKeepOut.offsetExtendsPosition = numericAttr.create('offsetExtendsPosition', 'offsetExtendsPosition', om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prKeepOut.addAttribute(prKeepOut.offsetExtendsPosition)
        prKeepOut.attributeAffects(prKeepOut.offsetExtendsPosition, prKeepOut.output)

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
        prKeepOut.parentInverseMatrix = matrixAttr.create('parentInverseMatrix', 'parentInverseMatrix', type=matrixAttr.kFloat)
        matrixAttr.keyable = True

        prKeepOut.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prKeepOut.enabledExtra)
        compoundAttr.addChild(prKeepOut.offsetExtra)
        compoundAttr.addChild(prKeepOut.position1)
        compoundAttr.addChild(prKeepOut.position2)
        compoundAttr.addChild(prKeepOut.parentInverseMatrix)
        compoundAttr.array = True
        prKeepOut.addAttribute(prKeepOut.input)
        prKeepOut.attributeAffects(prKeepOut.enabledExtra, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.offsetExtra, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.position1, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.position2, prKeepOut.output)
        prKeepOut.attributeAffects(prKeepOut.parentInverseMatrix, prKeepOut.output)

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
        offsetExtendsPosition = dataBlock.inputValue(self.offsetExtendsPosition).asBool()
        offset = dataBlock.inputValue(self.offset).asFloat()
        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()

        # get ray data
        indices = []
        enablesExtra = []
        inverseMatrices = []

        raySources = []
        rayDirections = []
        hitPositions = []
        hitDistances = []
        offsetVectors = []

        inputArrayHandle = dataBlock.inputArrayValue(self.input)
        for x in range(len(inputArrayHandle)):
            # get maya array input attributes
            inputArrayHandle.jumpToPhysicalElement(x)
            inputTargetHandle = inputArrayHandle.inputValue()
            index = inputArrayHandle.elementLogicalIndex()
            indices.append(index)
            position1 = om.MFloatPoint(inputTargetHandle.child(self.position1).asFloat3())
            position2 = om.MFloatPoint(inputTargetHandle.child(self.position2).asFloat3())
            eachOffset = offset + inputTargetHandle.child(self.offsetExtra).asFloat()
            inverseMatrices.append(inputTargetHandle.child(self.parentInverseMatrix).asFloatMatrix())
            enablesExtra.append(inputTargetHandle.child(self.enabledExtra).asBool())
            if not enabled or not enablesExtra[-1]:
                eachOffset = 0

            # calculate ray
            rayDirection = position2 - position1
            offsetVectors.append(rayDirection.normal() * eachOffset)
            if offsetExtendsPosition and eachOffset < 0:
                position1 += offsetVectors[-1]
                rayDirection -= offsetVectors[-1]
            hitDistances.append(rayDirection.length())
            raySources.append(position1)
            rayDirections.append(rayDirection)
            hitPositions.append(position2)

        if enabled:

            # geometry loop
            inputGeometryArrayHandle = dataBlock.inputArrayValue(self.inputGeometry)
            for physicalGeoIndex in range(len(inputGeometryArrayHandle)):
                inputGeometryArrayHandle.jumpToPhysicalElement(physicalGeoIndex)
                inputGeometryHandle = inputGeometryArrayHandle.inputValue()
                targetData = inputGeometryHandle.data()
                if targetData.isNull():
                    continue
                targetType = inputGeometryHandle.type()
                if targetType == om.MFnMeshData.kMesh:
                    meshFn = om.MFnMesh(targetData)
                    def getClosestHit(source, direction):
                        meshHit = meshFn.closestIntersection(source, direction, om.MSpace.kWorld, 1, False)[0]
                        if meshHit == om.MFloatPoint():
                            return None
                        return meshHit
                elif targetType == om.MFnNurbsSurfaceData.kNurbsSurface:
                    nurbsFn = om.MFnNurbsSurface(targetData)
                    def getClosestHit(source, direction):
                        nurbsHit = nurbsFn.intersect(om.MPoint(source), om.MVector(direction), om.MSpace.kWorld)
                        if nurbsHit is None:
                            return None
                        return om.MFloatPoint(nurbsHit[0])
                else:
                    raise ValueError('unknown targetType: {}'.format(targetType))

                # ray loop
                for x, (index, enabledExtra, raySource, rayDirection) in enumerate(zip(
                        indices, enablesExtra, raySources, rayDirections)):
                    if not enabledExtra:
                        continue
                    hit = getClosestHit(raySource, rayDirection)
                    if hit is None:
                        continue
                    hitDistance = (hit - raySource).length()
                    if hitDistance < hitDistances[x]:
                        hitPositions[x] = hit
                        hitDistances[x] = hitDistance

        # set output
        for index, hitPosition, offsetVector, inverseMatrix in zip(
                indices, hitPositions, offsetVectors, inverseMatrices):
            output_handle = output_builder.addElement(index)
            outputPosition = (hitPosition - offsetVector) * inverseMatrix
            output_handle.set3Float(outputPosition[0], outputPosition[1], outputPosition[2])

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
                editorTemplate -label "offsetExtendsPosition" -addControl "offsetExtendsPosition";
                editorTemplate -label "input" -addControl "input";
                editorTemplate -label "inputGeometry" -addControl "inputGeometry";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        //editorTemplate -suppress "input.parentInverseMatrix"; // not working
        //editorTemplate -suppress "output";
    };
    ''')

