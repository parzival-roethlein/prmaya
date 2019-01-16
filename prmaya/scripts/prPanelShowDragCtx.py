"""
# DESCRIPTION
Temporarily set (Panel > Show > types) when dragging the move/rotate/scale tool
The purpose is to have a clear view of the geometry during animation/posing
By default will create a scriptJob that evaluates on selection changes.
Part of https://github.com/parzival-roethlein/prmaya

# INSTALLATION
Copy this file ("prPanelShowDragCtx.py") into your ".../maya/scripts" folder

# BASIC USAGE
import prPanelShowDragCtx
prPanelShowDragCtx.enable()
prPanelShowDragCtx.disable()

# USAGE EXAMPLE: ALWAYS AUTOMATICALLY ENABLED (put this in your userSetup.py)
import maya.cmds as cmds
import prPanelShowDragCtx
cmds.evalDeferred('prPanelShowDragCtx.enable()')

# USAGE EXAMPLE: USER DEFINED PANEL SETTINGS FOR ANIMATORS
import prPanelShowDragCtx
prPanelShowDragCtx.enable(manipulators=False, nurbsCurves=False, controllers=False, locators=False)

# TODO
- MEvent version
- component selection support
- channelBox attribute drag support: mc.draggerContext doesn't seem to trigger from channelBox drag
- Universal Manipulator support: Doesn't seem to have a command, als tried mc.draggerContext('xformManipContext', ..)

# DEV
import maya.cmds as cmds
from prmaya.scripts import prPanelShowDragCtx
reload(prPanelShowDragCtx)
prPanelShowDragCtx.logger.setLevel(10)
prPanelShowDragCtx.enable()
print(cmds.scriptJob(listJobs=True))
prPanelShowDragCtx.enable(nurbsCurves=False)
prPanelShowDragCtx.enable(manipulators=False)
prPanelShowDragCtx.enable(polymeshes=False)
prPanelShowDragCtx.enable(withFocus=True)
prPanelShowDragCtx.disable()

"""

from collections import defaultdict
from functools import wraps
import logging

import maya.cmds as mc
import maya.mel as mm

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEFAULT_FLAGS = {'manipulators': False}
SCENE_PANEL_VALUES = defaultdict(dict)
NODE_TYPE = None
SCRIPT_JOB_ID = None


def enable(withFocus=False, **panelFlags):
    """
    :param withFocus: see maya.cmds.getPanel(withFocus=...) documentation
    :param panelFlags: see maya.cmds.modelEditor() documentation
    :return:
    """
    createScriptJob(withFocus=withFocus, **panelFlags)
    createTimelineDragCtx(withFocus=withFocus, **panelFlags)


def disable():
    deleteScriptJob()
    deleteTimelineDragCtx()
    setCommands()
    global NODE_TYPE
    NODE_TYPE = None


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug('{0}(args: {1}, kwargs: {2})'.format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        if result is not None:
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
    :param withFocus: see maya.cmds.getPanel(withFocus=...) documentation
    :param flags: see maya.cmds.modelEditor() documentation
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
def createFromNodeTypeAndFlags(nodeType='transform', withFocus=False, **flags):
    if not flags:
        global DEFAULT_FLAGS
        logger.debug('using default flags')
        flags = DEFAULT_FLAGS
    setCommands(nodeType=nodeType, preFunc=lambda: preCommand(withFocus=withFocus, **flags), postFunc=postCommand)


@log
def isNodeTypeUpdateRequired():
    global NODE_TYPE
    logger.debug('OLD NODE_TYPE: {}'.format(NODE_TYPE))
    selectedNodeTypes = mc.ls(sl=True, showType=True)[1::2]
    if not selectedNodeTypes or NODE_TYPE in selectedNodeTypes:
        return False
    NODE_TYPE = selectedNodeTypes[0]
    logger.debug('NEW NODE_TYPE: {}'.format(NODE_TYPE))
    return True


@log
def createScriptJob(withFocus=False, **panelFlags):
    disable()

    def prPanelShowDragCtxScriptJob():
        if isNodeTypeUpdateRequired():
            global NODE_TYPE
            createFromNodeTypeAndFlags(nodeType=NODE_TYPE, withFocus=withFocus, **panelFlags)

    global SCRIPT_JOB_ID
    SCRIPT_JOB_ID = mc.scriptJob(event=["SelectionChanged", prPanelShowDragCtxScriptJob])
    prPanelShowDragCtxScriptJob()


@log
def deleteScriptJob():
    global SCRIPT_JOB_ID
    if SCRIPT_JOB_ID is not None:
        mc.scriptJob(kill=SCRIPT_JOB_ID, force=True)
        SCRIPT_JOB_ID = None
    for scriptJob in mc.scriptJob(listJobs=True):
        if 'prPanelShowDragCtxScriptJob' in scriptJob:
            scriptJobId = int(scriptJob[:scriptJob.find(':')])
            mc.scriptJob(kill=scriptJobId, force=True)


def createTimelineDragCtx(withFocus=False, **flags):
    if not flags:
        global DEFAULT_FLAGS
        flags = DEFAULT_FLAGS
    playbackSlider = mm.eval('$tmpVar=$gPlayBackSlider')
    mc.timeControl(playbackSlider, edit=True, pressCommand=lambda a: preCommand(withFocus=withFocus, **flags))
    mc.timeControl(playbackSlider, edit=True, releaseCommand=lambda a: postCommand())


def deleteTimelineDragCtx():
    playbackSlider = mm.eval('$tmpVar=$gPlayBackSlider')
    mc.timeControl(playbackSlider, edit=True, pressCommand=str)
    mc.timeControl(playbackSlider, edit=True, releaseCommand=str)


"""
def createMEvent():
    import maya.OpenMaya as OpenMaya
    global M_EVENT_ID 
    M_EVENT_ID = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", updateCtx)

def deleteMEvent():
    global M_EVENT_ID
    OpenMaya.MMessage.removeCallback(MEVENT_ID)
"""

