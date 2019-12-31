"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Array version of Mayas "decomposeMatrix" with added features.
- "output..." attributes shortened to "out..."
- inputInverseMatrix added
- inputRotateOrder attribute working. It is (was?) bugged in Mayas decomposeMatrix, by always acting like xyz

USE CASES
- Replace multiple decomposeMatrix nodes (+multMatrix) with fewer prDecomposeMatrix nodes


USAGE
(MEL): createNode prDecomposeMatrix

ATTRIBUTES
prDecomposeMatrix.input[0].inputMatrix
prDecomposeMatrix.input[0].inputInverseMatrix
prDecomposeMatrix.input[0].inputRotateOrder
prDecomposeMatrix.output[0].outTranslate
prDecomposeMatrix.output[0].outRotate
prDecomposeMatrix.output[0].outScale
prDecomposeMatrix.output[0].outShear
prDecomposeMatrix.output[0].outQuat

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- test performance difference with bool attributes (.calculateTranslate, .calculateRotate, ...)
- optional cleanup (icon, aeTemplate array attr, nodeBehavior attr)
"""


import sys

import maya.api.OpenMaya as om


class prDecomposeMatrix(om.MPxNode):
    nodeTypeName = "prDecomposeMatrix"
    nodeTypeId = om.MTypeId(0x0004C271)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        matrixAttr = om.MFnMatrixAttribute()
        enumAttr = om.MFnEnumAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        unitAttr = om.MFnUnitAttribute()

        # output
        prDecomposeMatrix.outTranslate = numericAttr.createPoint('outTranslate', 'outTranslate')
        numericAttr.writable = False

        prDecomposeMatrix.outRotateX = unitAttr.create('outRotateX', 'outRotateX', om.MFnUnitAttribute.kAngle)
        unitAttr.writable = False
        prDecomposeMatrix.outRotateY = unitAttr.create('outRotateY', 'outRotateY', om.MFnUnitAttribute.kAngle)
        unitAttr.writable = False
        prDecomposeMatrix.outRotateZ = unitAttr.create('outRotateZ', 'outRotateZ', om.MFnUnitAttribute.kAngle)
        unitAttr.writable = False
        prDecomposeMatrix.outRotate = compoundAttr.create('outRotate', 'outRotate')
        compoundAttr.writable = False
        compoundAttr.addChild(prDecomposeMatrix.outRotateX)
        compoundAttr.addChild(prDecomposeMatrix.outRotateY)
        compoundAttr.addChild(prDecomposeMatrix.outRotateZ)

        prDecomposeMatrix.outScale = numericAttr.createPoint('outScale', 'outScale')
        numericAttr.writable = False

        prDecomposeMatrix.outShear = numericAttr.createPoint('outShear', 'outShear')
        numericAttr.writable = False

        prDecomposeMatrix.outQuatX = numericAttr.create('outQuatX', 'outQuatX', om.MFnNumericData.kFloat)
        unitAttr.writable = False
        prDecomposeMatrix.outQuatY = numericAttr.create('outQuatY', 'outQuatY', om.MFnNumericData.kFloat)
        unitAttr.writable = False
        prDecomposeMatrix.outQuatZ = numericAttr.create('outQuatZ', 'outQuatZ', om.MFnNumericData.kFloat)
        unitAttr.writable = False
        prDecomposeMatrix.outQuatW = numericAttr.create('outQuatW', 'outQuatW', om.MFnNumericData.kFloat)
        unitAttr.writable = False
        prDecomposeMatrix.outQuat = compoundAttr.create('outQuat', 'outQuat')
        compoundAttr.writable = False
        compoundAttr.addChild(prDecomposeMatrix.outQuatX)
        compoundAttr.addChild(prDecomposeMatrix.outQuatY)
        compoundAttr.addChild(prDecomposeMatrix.outQuatZ)
        compoundAttr.addChild(prDecomposeMatrix.outQuatW)

        prDecomposeMatrix.output = compoundAttr.create('output', 'output')
        compoundAttr.addChild(prDecomposeMatrix.outTranslate)
        compoundAttr.addChild(prDecomposeMatrix.outRotate)
        compoundAttr.addChild(prDecomposeMatrix.outScale)
        compoundAttr.addChild(prDecomposeMatrix.outShear)
        compoundAttr.addChild(prDecomposeMatrix.outQuat)
        compoundAttr.writable = False
        compoundAttr.array = True
        compoundAttr.usesArrayDataBuilder = True
        prDecomposeMatrix.addAttribute(prDecomposeMatrix.output)

        # input
        prDecomposeMatrix.inputRotateOrder = enumAttr.create('inputRotateOrder', 'inputRotateOrder', 0)
        enumAttr.addField('xyz', 0)
        enumAttr.addField('yzx', 1)
        enumAttr.addField('zxy', 2)
        enumAttr.addField('xzy', 3)
        enumAttr.addField('yxz', 4)
        enumAttr.addField('zyx', 5)
        enumAttr.keyable = True
        prDecomposeMatrix.addAttribute(prDecomposeMatrix.inputRotateOrder)
        prDecomposeMatrix.attributeAffects(prDecomposeMatrix.inputRotateOrder, prDecomposeMatrix.output)

        prDecomposeMatrix.inputMatrix = matrixAttr.create('inputMatrix', 'inputMatrix')
        matrixAttr.keyable = True

        prDecomposeMatrix.inputInverseMatrix = matrixAttr.create('inputInverseMatrix', 'inputInverseMatrix')
        matrixAttr.keyable = True

        prDecomposeMatrix.input = compoundAttr.create('input', 'input')
        compoundAttr.addChild(prDecomposeMatrix.inputRotateOrder)
        compoundAttr.addChild(prDecomposeMatrix.inputMatrix)
        compoundAttr.addChild(prDecomposeMatrix.inputInverseMatrix)
        compoundAttr.array = True
        prDecomposeMatrix.addAttribute(prDecomposeMatrix.input)
        prDecomposeMatrix.attributeAffects(prDecomposeMatrix.inputMatrix, prDecomposeMatrix.output)
        prDecomposeMatrix.attributeAffects(prDecomposeMatrix.inputInverseMatrix, prDecomposeMatrix.output)
        prDecomposeMatrix.attributeAffects(prDecomposeMatrix.inputRotateOrder, prDecomposeMatrix.output)

    @staticmethod
    def creator():
        return prDecomposeMatrix()

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
        if plug not in [self.output,
                        self.outTranslate,
                        self.outRotate, self.outRotateX, self.outRotateY, self.outRotateZ,
                        self.outScale,
                        self.outShear,
                        self.outQuat, self.outQuatX, self.outQuatY, self.outQuatZ, self.outQuatW]:
            self.displayWarning(error='Unknown plug: {}'.format(plug))
            return

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()
        inputArrayHandle = dataBlock.inputArrayValue(self.input)

        for i in range(len(inputArrayHandle)):
            inputArrayHandle.jumpToPhysicalElement(i)
            index = inputArrayHandle.elementLogicalIndex()
            inputTargetHandle = inputArrayHandle.inputValue()
            outputHandle = output_builder.addElement(index)
            outTranslateHandle = outputHandle.child(self.outTranslate)
            outRotateHandle = outputHandle.child(self.outRotate)
            outScaleHandle = outputHandle.child(self.outScale)
            outShearHandle = outputHandle.child(self.outShear)
            outQuatHandle = outputHandle.child(self.outQuat)
            rotateOrder = inputTargetHandle.child(self.inputRotateOrder).asShort()
            inputMatrix = inputTargetHandle.child(self.inputMatrix).asMatrix()
            inputInverseMatrix = inputTargetHandle.child(self.inputInverseMatrix).asMatrix()

            inputTransMatrix = om.MTransformationMatrix(inputMatrix*inputInverseMatrix)

            # translate
            translate = inputTransMatrix.translation(om.MSpace.kWorld)
            outTranslateHandle.set3Float(*translate)
            outTranslateHandle.setClean()

            # rotate
            inputTransMatrix.reorderRotation(rotateOrder + 1)
            rotation = inputTransMatrix.rotation()
            outRotateHandle.set3Double(rotation[0], rotation[1], rotation[2])
            outRotateHandle.setClean()

            # scale
            scale = inputTransMatrix.scale(om.MSpace.kWorld)
            outScaleHandle.set3Float(*scale)
            outScaleHandle.setClean()

            # shear
            shear = inputTransMatrix.shear(om.MSpace.kWorld)
            outShearHandle.set3Float(*shear)
            outShearHandle.setClean()

            # quat
            quaternion = inputTransMatrix.rotation(asQuaternion=True)
            outQuatXHandle = outQuatHandle.child(self.outQuatX)
            outQuatXHandle.setFloat(quaternion.x)
            outQuatYHandle = outQuatHandle.child(self.outQuatY)
            outQuatYHandle.setFloat(quaternion.y)
            outQuatZHandle = outQuatHandle.child(self.outQuatZ)
            outQuatZHandle.setFloat(quaternion.z)
            outQuatWHandle = outQuatHandle.child(self.outQuatW)
            outQuatWHandle.setFloat(quaternion.w)
            outQuatHandle.setClean()

        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prDecomposeMatrix.nodeTypeName, prDecomposeMatrix.nodeTypeId,
                              prDecomposeMatrix.creator, prDecomposeMatrix.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prDecomposeMatrix.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prDecomposeMatrix.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prDecomposeMatrix.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprDecomposeMatrixTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prDecomposeMatrix Attributes" -collapse 0;
                editorTemplate -label "input" -addControl "input";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "output";
    };
    ''')
