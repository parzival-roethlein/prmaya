"""
# SOURCE
https://github.com/parzival-roethlein/prmaya

# DESCRIPTION
Temporarily sets (Panel > Show > types) while:
 - dragging the translate/rotate/scale tools
 - timeline dragging
 - timeline playback
The purpose is to have a clear view of the deforming geometry
Technical: Creates a scriptJob (SelectionChanged) and OpenMaya.MConditionMessage (playingBack)

# INSTALLATION
Copy this file ("prPanelCtx.py") into your ".../maya/scripts" folder.

# USAGE (It's recommended to run it in your userSetup file, so you don't have to think about it and treat it like a Maya setting)
import prPanelCtx
# AND EITHER
prPanelCtx.enable(manipulators=False) # prPanelCtx.disable()
# OR
prPanelCtx.toggle(manipulators=False)

# USAGE EXAMPLE: ANIMATION
import prPanelCtx
prPanelCtx.enable(manipulators=False, nurbsCurves=False, locators=False, controllers=False)

# USAGE EXAMPLE: RIGGING
import prPanelCtx
prPanelCtx.enable(manipCtxKwargs={'manipulators': False}, playbackCtxKwargs={'nurbsCurves': False, 'locators': False, 'controllers': False})


# TODO
- UI
- shadingCtx (xray joints, default material, ...)
- LightingCtx
- switch scriptJob creation to onFileOpen and delete onFileClose? so playbackId does not get lost / multiple playback scriptjobs created
- (could not find a event for this) timeline context to start on mousedown, not only after time changes

# TODO (maybe)
- compare and maybe switch to MEvent version of manipScriptjob
- camera orbit ctx (orbitCtx, draggerContext, panZoomCtx)
- manipCtx component selection support
- channelBox attribute drag support: mc.draggerContext doesn't seem to trigger from channelBox drag
- Universal Manipulator support: Doesn't seem to have a command, als tried mc.draggerContext('xformManipContext', ..)

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

SCENE_PANEL_VALUES = defaultdict(dict)
MANIP_NODE_TYPE = None
MANIP_CTX_ID = None
PLAYBACK_CTX_ID = None

TOGGLE_STATUS = False


def enable(manipCtxKwargs=None, playbackCtxKwargs=None, **allCtxKwargs):
    """
    :param manipCtxKwargs: settings for only the manipulators (translate, rotate, scale tools)
    :param playbackCtxKwargs: settings for only the timeline interaction (drag, playback)
    :param allCtxKwargs: settings for both: manipulators / timeline interaction
    :return: 
    """
    global TOGGLE_STATUS
    TOGGLE_STATUS = True
    manipCtxKwargs = dict(allCtxKwargs.items() + (manipCtxKwargs or {}).items())
    playbackCtxKwargs = dict(allCtxKwargs.items() + (playbackCtxKwargs or {}).items())
    createManipCtx(**manipCtxKwargs)
    createPlaybackCtx(**playbackCtxKwargs)


def disable():
    global TOGGLE_STATUS
    TOGGLE_STATUS = False
    deleteManipCtx()
    deletePlaybackCtx()


def toggle(displayInfo=True, **enableKwargs):
    """
    :param displayInfo: display toggle status
    :param enableKwargs: see def enable(..)
    :return:
    """
    global TOGGLE_STATUS
    if not TOGGLE_STATUS:
        enable(**enableKwargs)
        if displayInfo:
            om.MGlobal.displayInfo('ENABLED prPanelCtx')
    else:
        disable()
        if displayInfo:
            om.MGlobal.displayInfo('DISABLED prPanelCtx')


def preCommand(withFocus=False, **flags):
    """
    :param withFocus: only affect panel with focus: cmds.getPanel(withFocus=...)
    :param flags: see cmds.modelEditor() documentation
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


def postCommand():
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
    currentCtx = mc.currentCtx()
    if currentCtx in ['moveSuperContext', 'RotateSuperContext', 'scaleSuperContext']:
        # only set context if needed
        mc.setToolTo(currentCtx)


def manipCtxNodeTypeChange():
    global MANIP_NODE_TYPE
    selectedNodeTypes = mc.ls(sl=True, showType=True, type='transform')[1::2]
    if not selectedNodeTypes or MANIP_NODE_TYPE in selectedNodeTypes:
        return False
    MANIP_NODE_TYPE = selectedNodeTypes[0]
    return True


@log
def createManipCtx(**preCommandKwargs):
    def createManipCtxDeferred():
        deleteManipCtx()

        def prPanelCtxManipScriptJob():
            if manipCtxNodeTypeChange():
                global MANIP_NODE_TYPE
                setManipCommands(nodeType=MANIP_NODE_TYPE, preFunc=lambda: preCommand(**preCommandKwargs), postFunc=postCommand)
        prPanelCtxManipScriptJob()

        global MANIP_CTX_ID
        MANIP_CTX_ID = mc.scriptJob(event=["SelectionChanged", prPanelCtxManipScriptJob])
    # evalDeferred to be able to run in Maya userSetup file
    mc.evalDeferred(createManipCtxDeferred)


@log
def getManipCtx():
    scriptJob_ids = []
    for scriptJob in mc.scriptJob(listJobs=True) or []:
        if 'prPanelCtxManipScriptJob' in scriptJob:
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
def createPlaybackCtx(**preCommandKwargs):
    def createPlaybackCtxDeferred():
        deletePlaybackCtx()

        def prPanelCtxCondition(state, **preCommandKwargs):
            if state:
                preCommand(**preCommandKwargs)
            else:
                postCommand()
        global PLAYBACK_CTX_ID
        PLAYBACK_CTX_ID = om.MConditionMessage.addConditionCallback('playingBack', lambda state, *args: prPanelCtxCondition(state, **preCommandKwargs))
    # evalDeferred to be able to run in Maya userSetup file
    mc.evalDeferred(createPlaybackCtxDeferred)


@log
def deletePlaybackCtx():
    global PLAYBACK_CTX_ID
    if PLAYBACK_CTX_ID:
        om.MMessage.removeCallback(PLAYBACK_CTX_ID)
        PLAYBACK_CTX_ID = None

