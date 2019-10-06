"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Array version of Mayas "decomposeMatrix" with added features and fixed rotateOrder bug

USE CASES
- Replace multiple decomposeMatrix nodes (+multMatrix) with fewer prDecomposeMatrix nodes
- If you need another rotateOrder than xyz (decomposeMatrix.inputRotateOrder is not working)

USAGE
(MEL): createNode prDecomposeMatrix

ATTRIBUTES
prDecomposeMatrix1.input[0].inputMatrix
prDecomposeMatrix1.input[0].inputInverseMatrix
prDecomposeMatrix1.input[0].inputRotateOrder
prDecomposeMatrix1.output[0].outputTranslate
prDecomposeMatrix1.output[0].outputRotate
prDecomposeMatrix1.output[0].outputScale
prDecomposeMatrix1.output[0].outputShear
prDecomposeMatrix1.output[0].outputQuat

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

        # output
        prDecomposeMatrix.outTranslate = numericAttr.createPoint('outTranslate', 'outTranslate')
        numericAttr.writable = False

        prDecomposeMatrix.output = compoundAttr.create('output', 'output')
        compoundAttr.addChild(prDecomposeMatrix.outTranslate)
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
        if plug not in [self.outTranslate]:
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

            rotateOrder = inputTargetHandle.child(self.inputRotateOrder).asShort()

            outTranslate = [rotateOrder, rotateOrder, rotateOrder]
            outTranslateHandle.set3Float(outTranslate[0], outTranslate[1], outTranslate[2])

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
        //editorTemplate -suppress "output";
    };
    ''')
