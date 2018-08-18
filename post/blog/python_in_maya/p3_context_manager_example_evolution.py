"""
abstraction evolution for general purpose maya command context:

with maya_cmds_flag(maya.cmds.currentUnit, linear='cm'):
    pass

"""

from contextlib import contextmanager
from functools import wraps

import maya.cmds as mc


# original decorator
def working_unit_linear_cm(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        scene_unit = mc.currentUnit(query=True, linear=True)
        if scene_unit != 'cm':
            mc.currentUnit(linear='cm')
        try:
            result = func(*args, **kwargs)
        finally:
            if scene_unit != 'cm':
                mc.currentUnit(linear=scene_unit)
        return result

    return wrapper


# context manager version
@contextmanager
def working_unit_linear_cm():
    scene_value = mc.currentUnit(query=True, linear=True)
    if scene_value != 'cm':
        mc.currentUnit(linear='cm')
    yield
    if scene_value != 'cm':
        mc.currentUnit(linear=scene_value)


# generalize to different values
@contextmanager
def working_unit_linear(value='cm'):
    scene_value = mc.currentUnit(query=True, linear=True)
    if scene_value != value:
        mc.currentUnit(linear=value)
    yield
    if scene_value != value:
        mc.currentUnit(linear=scene_value)


# generalize to currentUnit command
@contextmanager
def current_unit(**flags):
    different_scene_values = {}
    for k, value in flags.iteritems():
        scene_value = mc.currentUnit(query=True, **{k: True})
        if scene_value != value:
            mc.currentUnit(**{k: value})
            different_scene_values[k] = scene_value
    yield
    for k, value in different_scene_values.iteritems():
        mc.currentUnit(**{k: value})


# generalize to any command
@contextmanager
def maya_cmds_flag(func, **flags):
    different_scene_values = {}
    for k, value in flags.iteritems():
        scene_value = func(query=True, **{k: True})
        if scene_value != value:
            # TODO: find proper way to detect edit flag
            try:
                func(edit=True, **{k: value})
            except:
                func(**{k: value})
            different_scene_values[k] = scene_value
    yield
    for k, value in different_scene_values.iteritems():
        mc.currentUnit(**{k: value})


# updated decorator
def working_unit_linear_cm(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with maya_cmds_flag(func=mc.currentUnit, linear='cm'):
            result = func(*args, **kwargs)
        return result

