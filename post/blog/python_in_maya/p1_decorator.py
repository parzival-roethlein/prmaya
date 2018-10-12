"""
Python in Maya #1: Decorators
Two examples of simple Python decorators for Maya.
There are many resources online that explain decorators,
so I don't want to add yet another one.
I just want to demonstrate their usefulness to Maya coders that are
not using them yet.

Both examples show the good practice of using the optional,
standard library, convenience function functools.wraps to not
lose/overwrite the wrapped functions func.__name__, func.__doc__, ..
doc: https://docs.python.org/2/library/functools.html#functools.wraps
"""

from functools import wraps

"""
1. Preserve Maya selection (maya.cmds)

Some Maya commands automatically modify the selection.
This is often unwanted behavior.
Sometimes there is a flag to disable that behavior.
Other times it is possible to avoid those commands.
But if neither is an option (or you don't want to worry about it)
this decorator will always disable it.
"""

import maya.cmds as mc


def preserve_selection(func):
    """prevent Maya selection changes"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        selection = mc.ls(orderedSelection=True)
        result = func(*args, **kwargs)
        mc.select(clear=True)
        for each in selection:
            if mc.objExists(each):
                mc.select(each, add=True)
        return result

    return wrapper


@preserve_selection
def create_cube():
    return mc.polyCube()


create_cube()
# cube was not selected on creation


"""
2. Run in "Settings > Working Units > Linear > centimeter" (PyMEL)

Some commands do not run properly in scene working units other 
than the default centimeter. This decorator is a simple 
workaround for that problem, by temporarily setting it to 
centimeter for the duration of the wrapped function/method.
"""

import pymel.core as pm


def working_unit_linear_cm(func):
    """temporarily set working unit to cm"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        scene_unit = pm.currentUnit(query=True, linear=True)
        if scene_unit != 'cm':
            pm.currentUnit(linear='cm')
        try:
            result = func(*args, **kwargs)
        finally:
            if scene_unit != 'cm':
                pm.currentUnit(linear=scene_unit)
        return result

    return wrapper


@working_unit_linear_cm
def snap_vertex(driven_vertex, driver_vertex):
    driven_vertex = pm.PyNode(driven_vertex)
    driver_vertex = pm.PyNode(driver_vertex)
    driven_vertex.setPosition(driver_vertex.getPosition())


snap_vertex('pCube1.vtx[2]', 'pCube1.vtx[3]')
# snapped properly with non 'cm' scene_unit
