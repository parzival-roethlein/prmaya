"""
# DESCRIPTION
Temporarily sets (Panel > Show > types) while dragging the translate/rotate/scale tools or the timeline changes
The purpose is to have a clear view of the deforming geometry
Creates a scriptJob (SelectionChanged) and OpenMaya.MConditionMessage (playingBack)
Get the latest version at https://github.com/parzival-roethlein/prmaya

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

# USAGE EXAMPLE: USER DEFINED PANEL SETTINGS
import prPanelShowDragCtx
prPanelShowDragCtx.enable(manipulators=False, nurbsCurves=False, controllers=False, locators=False)

# TODO
- camera orbit mode
- UI
- MEvent version of manipScriptjob
- component selection support
- channelBox attribute drag support: mc.draggerContext doesn't seem to trigger from channelBox drag
- Universal Manipulator support: Doesn't seem to have a command, als tried mc.draggerContext('xformManipContext', ..)

# DEV
import maya.cmds as cmds
cmds.file("/home/prthlein/private/code/prmaya/test/scripts/prPanelShowDragCtx.ma", open=True, force=True)
import sys
sys.path.append('/home/prthlein/private/code/prmaya/')
from prmaya.scripts import prPanelShowDragCtx
prPanelShowDragCtx.disable()
reload(prPanelShowDragCtx)
prPanelShowDragCtx.logger.setLevel(10)

prPanelShowDragCtx.enable()
prPanelShowDragCtx.getManipCtx()
prPanelShowDragCtx.disable()

prPanelShowDragCtx.enable(nurbsCurves=False, manipulators=False)
prPanelShowDragCtx.disable()

prPanelShowDragCtx.enable(polymeshes=False)
prPanelShowDragCtx.disable()

prPanelShowDragCtx.enable(withFocus=True)
prPanelShowDragCtx.disable()

"""

from collections import defaultdict
from functools import wraps
import logging

import maya.api.OpenMaya as om
import maya.cmds as mc
import maya.mel as mm

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEFAULT_FLAGS = {'manipulators': False}

SCENE_PANEL_VALUES = defaultdict(dict)
MANIP_NODE_TYPE = None
MANIP_CTX_ID = None
PLAYBACK_CTX_ID = None


def enable(manipulatorCtx=True, playingBackCtx=True, **kwargs):
    """
    :param manipulatorCtx: enable manipulator context
    :param playingBackCtx: enable playingBack context
    :param kwargs: see def preDragCommand(..)
    :return:
    """
    if manipulatorCtx:
        createManipCtx(**kwargs)
    if playingBackCtx:
        createPlaybackCtx(**kwargs)


def disable():
    deleteManipCtx()
    deletePlaybackCtx()


def preDragCommand(withFocus=False, **flags):
    """
    :param withFocus: only affect panel with focus: cmds.getPanel(withFocus=...)
    :param flags: see cmds.modelEditor() documentation
    :return: list of affected panels
    """
    global SCENE_PANEL_VALUES
    SCENE_PANEL_VALUES.clear()

    if not flags:
        global DEFAULT_FLAGS
        flags = DEFAULT_FLAGS

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


def postDragCommand():
    for panel, flags in SCENE_PANEL_VALUES.iteritems():
        for flag, value in flags.iteritems():
            mc.modelEditor(panel, e=True, **{flag: value})


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug('{0}(args: {1}, kwargs: {2})'.format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        logger.debug('  {0} output = {1}'.format(func.__name__, result))

        return result
    return wrapper


def setManipCommands(nodeType='transform', preFunc=str, postFunc=str):
    mc.manipMoveContext('Move', e=True, preDragCommand=[preFunc, nodeType])
    mc.manipMoveContext('Move', e=True, postDragCommand=[postFunc, nodeType])
    mc.manipRotateContext('Rotate', e=True, preDragCommand=[preFunc, nodeType])
    mc.manipRotateContext('Rotate', e=True, postDragCommand=[postFunc, nodeType])
    mc.manipScaleContext('Scale', e=True, preDragCommand=[preFunc, nodeType])
    mc.manipScaleContext('Scale', e=True, postDragCommand=[postFunc, nodeType])
    # the drag commands are only active on reentering the context
    mc.setToolTo(mc.currentCtx())


@log
def manipCtxNodeTypeChange():
    global MANIP_NODE_TYPE
    selectedNodeTypes = mc.ls(sl=True, showType=True)[1::2]
    if not selectedNodeTypes or MANIP_NODE_TYPE in selectedNodeTypes:
        return False
    MANIP_NODE_TYPE = selectedNodeTypes[0]
    return True


@log
def createManipCtx(**kwargs):
    deleteManipCtx()

    def prPanelShowDragCtxManipScriptJob():
        if manipCtxNodeTypeChange():
            global MANIP_NODE_TYPE
            setManipCommands(nodeType=MANIP_NODE_TYPE, preFunc=lambda: preDragCommand(**kwargs), postFunc=postDragCommand)
    prPanelShowDragCtxManipScriptJob()

    global MANIP_CTX_ID
    MANIP_CTX_ID = mc.scriptJob(event=["SelectionChanged", prPanelShowDragCtxManipScriptJob])


def getManipCtx():
    scriptJob_ids = []
    for scriptJob in mc.scriptJob(listJobs=True):
        if 'prPanelShowDragCtxManipScriptJob' in scriptJob:
            scriptJobId = int(scriptJob[:scriptJob.find(':')])
            scriptJob_ids.append(scriptJobId)
    return scriptJob_ids


@log
def deleteManipCtx():
    global MANIP_CTX_ID
    if MANIP_CTX_ID:
        mc.scriptJob(kill=MANIP_CTX_ID, force=True)
        MANIP_CTX_ID = None
    global MANIP_NODE_TYPE
    MANIP_NODE_TYPE = None
    setManipCommands()
    invalid_ids = getManipCtx()
    if invalid_ids:
        for id_ in invalid_ids:
            mc.scriptJob(kill=id_, force=True)
        mm.eval('warning "Deleted manipCtx ids that should not have existed : {}"'.format(invalid_ids))


@log
def createPlaybackCtx(**kwargs):
    deletePlaybackCtx()

    def prPanelShowDragCtxCondition(state, **kwargs):
        if state:
            preDragCommand(**kwargs)
        else:
            postDragCommand()
    global PLAYBACK_CTX_ID
    PLAYBACK_CTX_ID = om.MConditionMessage.addConditionCallback('playingBack', lambda state, *args: prPanelShowDragCtxCondition(state, **kwargs))


@log
def deletePlaybackCtx():
    global PLAYBACK_CTX_ID
    if PLAYBACK_CTX_ID:
        om.MMessage.removeCallback(PLAYBACK_CTX_ID)
        PLAYBACK_CTX_ID = None

