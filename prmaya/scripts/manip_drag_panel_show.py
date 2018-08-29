"""
# DESCRIPTION
- Temporarily set (Panel > Show > types) when dragging the move/rotate/scale tool
- The purpose is to have a clear view of the geometry during animation/posing

# USAGE
from prmaya.scripts import manip_drag_panel_show
# enable (feel free to change the arguments/flags)
manip_drag_panel_show.set_commands_from_flags(nurbsCurves=False, manipulators=False)
# disable
manip_drag_panel_show.set_commands()

# TODO
- channelBox attribute drag support: mc.draggerContext doesn't seem to trigger from channelBox drag
- support joint selection: how? expected node_type=transform to include joint, but does not
- Universal Manipulator support: Doesn't seem to have a command, als tried mc.draggerContext('xformManipContext', ..)

# DEV
from prmaya.scripts import manip_drag_panel_show
reload(manip_drag_panel_show)
manip_drag_panel_show.logger.setLevel(10)
manip_drag_panel_show.set_commands_from_flags(with_focus=True, nurbsCurves=False, manipulators=False)
manip_drag_panel_show.set_commands_from_flags(nurbsCurves=False, manipulators=False)
manip_drag_panel_show.set_commands_from_flags(nurbsCurves=False)
manip_drag_panel_show.set_commands_from_flags(manipulators=False)
manip_drag_panel_show.set_commands()

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
def set_commands(node_type='transform', pre_func=str, post_func=str):
    mc.manipMoveContext('Move', e=True, preDragCommand=[pre_func, node_type])
    mc.manipMoveContext('Move', e=True, postDragCommand=[post_func, node_type])
    mc.manipRotateContext('Rotate', e=True, preDragCommand=[pre_func, node_type])
    mc.manipRotateContext('Rotate', e=True, postDragCommand=[post_func, node_type])
    mc.manipScaleContext('Scale', e=True, preDragCommand=[pre_func, node_type])
    mc.manipScaleContext('Scale', e=True, postDragCommand=[post_func, node_type])
    # the drag commands are only active on reentering the context
    mc.setToolTo(mc.currentCtx())


@log
def pre_command(with_focus=False, **flags):
    """
    :param with_focus: only affect the panel with focus
    :param flags: for mc.modelEditor
    :return: list of affected panels
    """
    global SCENE_PANEL_VALUES
    SCENE_PANEL_VALUES.clear()

    panels = mc.getPanel(type='modelPanel')
    if with_focus:
        focused_panel = mc.getPanel(withFocus=True)
        if focused_panel not in panels:
            # is this even possible?
            logger.debug('focused_panel: "{0}" not a modelPanel: [{1}]'.format(focused_panel, panels))
            return []
        panels = [focused_panel]
    for panel in panels:
        for flag, value in flags.iteritems():
            scene_value = mc.modelEditor(panel, q=True, **{flag: True})
            if scene_value != value:
                mc.modelEditor(panel, e=True, **{flag: value})
                SCENE_PANEL_VALUES[panel][flag] = scene_value
    return panels


@log
def post_command():
    for panel, flags in SCENE_PANEL_VALUES.iteritems():
        for flag, value in flags.iteritems():
            mc.modelEditor(panel, e=True, **{flag: value})


@log
def set_commands_from_flags(node_type='transform', with_focus=False, **flags):
    set_commands(node_type=node_type, pre_func=lambda: pre_command(with_focus=with_focus, **flags), post_func=post_command)

