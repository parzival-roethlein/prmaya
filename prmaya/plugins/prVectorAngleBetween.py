"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
array version of maya node "angleBetween"
differences: attribute names

USE CASES
...

USAGE
(MEL): createNode prVector

ATTRIBUTES
prVectorAngleBetween1.input[0].input1
prVectorAngleBetween1.input[0].input1.input1X
prVectorAngleBetween1.input[0].input1.input1Y
prVectorAngleBetween1.input[0].input1.input1Z
prVectorAngleBetween1.input[0].input2
prVectorAngleBetween1.input[0].input2.input2X
prVectorAngleBetween1.input[0].input2.input2Y
prVectorAngleBetween1.input[0].input2.input2Z
prVectorAngleBetween1.output[0].outputAxis
prVectorAngleBetween1.output[0].outputAxis.outputAxisX
prVectorAngleBetween1.output[0].outputAxis.outputAxisY
prVectorAngleBetween1.output[0].outputAxis.outputAxisZ
prVectorAngleBetween1.output[0].outputAngle #### group outputs, like mayas angleBetween?
prVectorAngleBetween1.output[0].outputEuler
prVectorAngleBetween1.output[0].outputEuler.outputEulerX
prVectorAngleBetween1.output[0].outputEuler.outputEulerY
prVectorAngleBetween1.output[0].outputEuler.outputEulerZ

LINKS
- Demo: TODO
- Making-of: TODO
- Donate: (This was written in my spare time. If you found it useful in Maya or for coding, consider supporting the author)
https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7X4EJ8Z7NUSQW

TODO
- custom aeTemplate for array input attr
- node behavior attrs
- icons
"""
