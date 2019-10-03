"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
Array version of Mayas "motionPath" node: .uValue[], .output[].outTranslate
Differences:
- motionPath.uValue = prMotionPath.uValue[0]: made into array
- motionPath.geometryPath = prMotionPath.inputCurve: renamed
- motionPath.allCoordinates = prMotionPath.output[0].outTranslate: made into array, renamed
  motionPath.xCoordinate = prMotionPath.output[0].outTranslateX (+Y, Z): renamed
- prMotionPath.fractionMode: connectable, True by default

USE CASES
- Replace multiple motionPath nodes with one prMotionPath nodes

USAGE
(MEL): createNode prMotionPath

ATTRIBUTES
prMotionPath.inputCurve
prMotionPath.uValue[0]
prMotionPath.output[0].outTranslate
prMotionPath.output[0].outTranslateX
prMotionPath.output[0].outTranslateY
prMotionPath.output[0].outTranslateZ

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- uValue aeTemplate buttons
- prMotionPath.inputWorldMatrix (of curve), prMotionPath.inputInverseMatrix (for output[] space)
- all motionPath features
- maybe show output in aeTemplate (but has to be custom to prevent "Add New Item" button)
- optional cleanup (icon, aeTemplate array attr, nodeBehavior attr)
"""


import sys

import maya.api.OpenMaya as om


class prMotionPath(om.MPxNode):
    nodeTypeName = "prMotionPath"
    nodeTypeId = om.MTypeId(0x0004C270)  # local, not save

    @staticmethod
    def initialize():
        numericAttr = om.MFnNumericAttribute()
        compoundAttr = om.MFnCompoundAttribute()
        typedAttr = om.MFnTypedAttribute()

        # output
        prMotionPath.outTranslate = numericAttr.createPoint('outTranslate', 'outTranslate')
        numericAttr.writable = False

        prMotionPath.output = compoundAttr.create('output', 'output')
        compoundAttr.addChild(prMotionPath.outTranslate)
        compoundAttr.array = True
        compoundAttr.usesArrayDataBuilder = True
        prMotionPath.addAttribute(prMotionPath.output)

        # input
        prMotionPath.inputCurve = typedAttr.create('inputCurve', 'inputCurve',
                                                   om.MFnNurbsCurveData.kNurbsCurve)
        prMotionPath.addAttribute(prMotionPath.inputCurve)
        prMotionPath.attributeAffects(prMotionPath.inputCurve, prMotionPath.outTranslate)

        prMotionPath.fractionMode = numericAttr.create('fractionMode', 'fractionMode',
                                                       om.MFnNumericData.kBoolean, True)
        numericAttr.keyable = True
        prMotionPath.addAttribute(prMotionPath.fractionMode)
        prMotionPath.attributeAffects(prMotionPath.fractionMode, prMotionPath.outTranslate)

        prMotionPath.uValue = numericAttr.create('uValue', 'uValue', om.MFnNumericData.kFloat, 0.0)
        numericAttr.keyable = True
        numericAttr.array = True
        numericAttr.usesArrayDataBuilder = True
        prMotionPath.addAttribute(prMotionPath.uValue)
        prMotionPath.attributeAffects(prMotionPath.uValue, prMotionPath.outTranslate)

    @staticmethod
    def creator():
        return prMotionPath()

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

        curveHandle = dataBlock.inputValue(self.inputCurve)
        curveData = curveHandle.data()
        if curveData.isNull():
            return
        curveFn = om.MFnNurbsCurve(curveData)

        fractionMode = dataBlock.inputValue(self.fractionMode).asBool()
        if fractionMode:
            uValueMult = curveFn.length()
        else:
            uValueMult = 1.0

        output_arrayHandle = dataBlock.outputArrayValue(self.output)
        output_builder = output_arrayHandle.builder()
        uValueArrayHandle = dataBlock.inputArrayValue(self.uValue)
        for i in range(len(uValueArrayHandle)):
            uValueArrayHandle.jumpToPhysicalElement(i)
            index = uValueArrayHandle.elementLogicalIndex()
            outputHandle = output_builder.addElement(index)
            outTranslateHandle = outputHandle.child(self.outTranslate)

            uValue = uValueArrayHandle.inputValue().asFloat() * uValueMult
            parameter = curveFn.findParamFromLength(uValue)

            outTranslate = curveFn.getPointAtParam(parameter, space=om.MSpace.kWorld)
            outTranslateHandle.set3Float(outTranslate[0], outTranslate[1], outTranslate[2])

        output_arrayHandle.set(output_builder)
        output_arrayHandle.setAllClean()
        dataBlock.setClean(plug)


def initializePlugin(obj):
    pluginFn = om.MFnPlugin(obj, 'Parzival Roethlein', '0.0.1')
    try:
        pluginFn.registerNode(prMotionPath.nodeTypeName, prMotionPath.nodeTypeId,
                              prMotionPath.creator, prMotionPath.initialize)
    except:
        sys.stderr.write('Failed to register node: {0}'.format(prMotionPath.nodeTypeName))
        raise
    evalAETemplate()


def uninitializePlugin(obj):
    pluginFn = om.MFnPlugin(obj)
    try:
        pluginFn.deregisterNode(prMotionPath.nodeTypeId)
    except:
        sys.stderr.write('Failed to deregister node: {0}'.format(prMotionPath.nodeTypeName))
        raise


def maya_useNewAPI():
    pass


def evalAETemplate():
    import maya.mel as mm
    mm.eval('''
    global proc AEprMotionPathTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prMotionPath Attributes" -collapse 0;
                editorTemplate -label "inputCurve" -addControl "inputCurve";
                editorTemplate -label "fractionMode" -addControl "fractionMode";
                editorTemplate -label "uValue" -addControl "uValue";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
        editorTemplate -suppress "output";
    };
    ''')
