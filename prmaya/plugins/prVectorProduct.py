"""
SOURCE
https://github.com/parzival-roethlein/prmaya

DESCRIPTION
array version of mayas "vectorProduct" node.
added features:
- added one inputMatrix attr for all inputs
- added inputScalar to multiply all outputs with

USE CASES
...

USAGE
(MEL): createNode prVectorProduct

ATTRIBUTES
prVectorProduct1.operation
prVectorProduct1.normalizeOutput
prVectorProduct1.inputMatrix
prVectorProduct1.inputScalar
prVectorProduct1.input[0].matrix
prVectorProduct1.input[0].input1
prVectorProduct1.input[0].input1.input1X
prVectorProduct1.input[0].input1.input1Y
prVectorProduct1.input[0].input1.input1Z
prVectorProduct1.input[0].input2
prVectorProduct1.input[0].input2.input2X
prVectorProduct1.input[0].input2.input2Y
prVectorProduct1.input[0].input2.input2Z
prVectorProduct1.output[0]
prVectorProduct1.output[0].outputX
prVectorProduct1.output[0].outputY
prVectorProduct1.output[0].outputZ

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

