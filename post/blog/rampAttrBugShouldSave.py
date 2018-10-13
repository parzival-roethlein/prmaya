"""
"Maya API ramp attribute bug?"
https://pazrot3d.blogspot.com/2018/10/maya-api-ramp-attribute-bug.html

workaround code sample
"""
import OpenMayaMPx

def shouldSave(self, plug, result):
    if plug == self.myRampAttr1:
        # return anything except 'unknown' to trigger save
        return True  # True used for readability
    return OpenMayaMPx.MPxNode.shouldSave(self, plug, result)
