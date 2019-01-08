"""
# DESCRIPTION
Temporarily set (Panel > Show > types) when dragging the move/rotate/scale tool
The purpose is to have a clear view of the geometry during animation/posing
Part of prmaya: https://github.com/parzival-roethlein/prmaya

# USAGE
from prmaya.scripts import prManipDragPanelCtx
# enable (feel free to change the arguments/flags)
prManipDragPanelCtx.setCommandsFromFlags(nurbsCurves=False, manipulators=False)
# disable
prManipDragPanelCtx.setCommands()

# TODO
- channelBox attribute drag support: mc.draggerContext doesn't seem to trigger from channelBox drag
- support joint selection: how? expected nodeType=transform to include joint, but does not
- Universal Manipulator support: Doesn't seem to have a command, als tried mc.draggerContext('xformManipContext', ..)

# DEV
from prmaya.scripts import prManipDragPanelCtx
reload(prManipDragPanelCtx)
prManipDragPanelCtx.logger.setLevel(10)
prManipDragPanelCtx.setCommandsFromFlags(withFocus=True, nurbsCurves=False, manipulators=False)
prManipDragPanelCtx.setCommandsFromFlags(nurbsCurves=False, manipulators=False)
prManipDragPanelCtx.setCommandsFromFlags(nurbsCurves=False)
prManipDragPanelCtx.setCommandsFromFlags(manipulators=False)
prManipDragPanelCtx.setCommands()

"""

from collections import defaultdict
from functools import wraps
import logging

import maya.cmds as mc


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SCENE_PANEL_VALUES = defaultdict(dict)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug('{0}(args: {1}, kwargs: {2})'.format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        logger.debug('result: {0}'.format(result))
        logger.debug('SCENE_PANEL_VALUES: {0}'.format(SCENE_PANEL_VALUES))
        return result
    return wrapper


@log
def setCommands(nodeType='transform', preFunc=str, postFunc=str):
    mc.manipMoveContext('Move', e=True, preDragCommand=[preFunc, nodeType])
    mc.manipMoveContext('Move', e=True, postDragCommand=[postFunc, nodeType])
    mc.manipRotateContext('Rotate', e=True, preDragCommand=[preFunc, nodeType])
    mc.manipRotateContext('Rotate', e=True, postDragCommand=[postFunc, nodeType])
    mc.manipScaleContext('Scale', e=True, preDragCommand=[preFunc, nodeType])
    mc.manipScaleContext('Scale', e=True, postDragCommand=[postFunc, nodeType])
    # the drag commands are only active on reentering the context
    mc.setToolTo(mc.currentCtx())


@log
def preCommand(withFocus=False, **flags):
    """
    :param withFocus: only affect the panel with focus
    :param flags: for mc.modelEditor
    :return: list of affected panels
    """
    global SCENE_PANEL_VALUES
    SCENE_PANEL_VALUES.clear()

    panels = mc.getPanel(type='modelPanel')
    if withFocus:
        focusedPanel = mc.getPanel(withFocus=True)
        if focusedPanel not in panels:
            # is this even possible?
            logger.debug('focusedPanel: "{0}" not a modelPanel: [{1}]'.format(focusedPanel, panels))
            return []
        panels = [focusedPanel]
    for panel in panels:
        for flag, value in flags.iteritems():
            sceneValue = mc.modelEditor(panel, q=True, **{flag: True})
            if sceneValue != value:
                mc.modelEditor(panel, e=True, **{flag: value})
                SCENE_PANEL_VALUES[panel][flag] = sceneValue
    return panels


@log
def postCommand():
    for panel, flags in SCENE_PANEL_VALUES.iteritems():
        for flag, value in flags.iteritems():
            mc.modelEditor(panel, e=True, **{flag: value})


@log
def setCommandsFromFlags(nodeType='transform', withFocus=False, **flags):
    setCommands(nodeType=nodeType, preFunc=lambda: preCommand(withFocus=withFocus, **flags), postFunc=postCommand)

