from contextlib import contextmanager

import maya.cmds as mc

import pymel.core as pm


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


@contextmanager
def unlocked_node(node):
    node = pm.PyNode(node)
    is_locked = node.isLocked()
    if is_locked:
        node.setLocked(False)
    yield node
    if is_locked and node.exists():
        node.setLocked(True)


@contextmanager
def unlocked_attribute(attribute):
    attribute = pm.PyNode(attribute)
    with unlocked_node(attribute.node()):
        is_locked = attribute.isLocked()
        if is_locked:
            attribute.setLocked(False)
        yield attribute
        if is_locked and attribute.exists():
            attribute.setLocked(True)


@contextmanager
def attribute_value(attribute, value):
    attribute = pm.PyNode(attribute)
    start_value = attribute.get()
    if start_value == value:
        yield attribute
        return
    with unlocked_attribute(attribute) as attr:
        if start_value != value:
            attr.set(value)
        yield attr
        if start_value != value:
            attr.set(start_value)

