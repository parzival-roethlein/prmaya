"""
# DESCRIPTION
Temporarily set (Panel > Show > types) when dragging the move/rotate/scale tool
The purpose is to have a clear view of the geometry during animation/posing
By default will create a scriptJob that evaluates on selection changes.
Part of https://github.com/parzival-roethlein/prmaya

# INSTALLATION
Copy this file ("prManipDragPanelCtx.py") into your ".../maya/scripts" folder

# SIMPLE USAGE
import prManipDragPanelCtx
prManipDragPanelCtx.enable()
prManipDragPanelCtx.disable()

# ADVANCED USAGE: USER DEFINED PANEL SETTINGS
import prManipDragPanelCtx
prManipDragPanelCtx.enable(nurbsCurve=False, manipulators=False, controllers=False, selectionHiliteDisplay=False)
prManipDragPanelCtx.disable()

# ADVANCED USAGE: WHEN ONLY WORKING WITH ONE NODE TYPE AND NOT WANTING THE SCRIPTJOB
import prManipDragPanelCtx
prManipDragPanelCtx.createFromNodeTypeAndFlags(nodeType='transform') # enable
prManipDragPanelCtx.setCommands() # disable

# TODO
- MEvent version
- component selection support
- channelBox attribute drag support: mc.draggerContext doesn't seem to trigger from channelBox drag
- Universal Manipulator support: Doesn't seem to have a command, als tried mc.draggerContext('xformManipContext', ..)


# DEV
import maya.cmds as cmds
from prmaya.scripts import prManipDragPanelCtx
reload(prManipDragPanelCtx)
prManipDragPanelCtx.logger.setLevel(10)
prManipDragPanelCtx.enable()
print(cmds.scriptJob(listJobs=True))
prManipDragPanelCtx.disable()
prManipDragPanelCtx.enable(nurbsCurves=False)
prManipDragPanelCtx.enable(manipulators=False)
prManipDragPanelCtx.enable(withFocus=True)
prManipDragPanelCtx.enable(polygons=False)

prManipDragPanelCtx.createFromNodeTypeAndFlags(withFocus=True, nurbsCurves=False, manipulators=False)
prManipDragPanelCtx.createFromNodeTypeAndFlags(nurbsCurves=False, manipulators=False)
prManipDragPanelCtx.createFromNodeTypeAndFlags(nurbsCurves=False)
prManipDragPanelCtx.createFromNodeTypeAndFlags(manipulators=False)
prManipDragPanelCtx.setCommands()

"""

from collections import defaultdict
from functools import wraps
import logging

import maya.cmds as mc


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEFAULT_FLAGS = {'nurbsCurves': False,
                 'manipulators': False,
                 'controllers': False,
                 'locators': False,
                 'joints': False}
SCENE_PANEL_VALUES = defaultdict(dict)
NODE_TYPE = None
SCRIPT_JOB_ID = None


def enable(withFocus=False, **panelFlags):
    """
    :param withFocus: only affect panel with focus. maya command cmds.getPanel(withFocus=True)
    :param panelFlags: see maya command "modelEditor" documentation
    :return:
    """
    createScriptJob(withFocus=withFocus, **panelFlags)


def disable():
    deleteScriptJob()
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

    def prManipDragPanelCtxScriptJob():
        if isNodeTypeUpdateRequired():
            global NODE_TYPE
            createFromNodeTypeAndFlags(nodeType=NODE_TYPE, withFocus=withFocus, **panelFlags)

    global SCRIPT_JOB_ID
    SCRIPT_JOB_ID = mc.scriptJob(event=["SelectionChanged", prManipDragPanelCtxScriptJob])
    prManipDragPanelCtxScriptJob()


@log
def deleteScriptJob():
    global SCRIPT_JOB_ID
    if SCRIPT_JOB_ID is not None:
        mc.scriptJob(kill=SCRIPT_JOB_ID, force=True)
        SCRIPT_JOB_ID = None
    for scriptJob in mc.scriptJob(listJobs=True):
        if 'prManipDragPanelCtxScriptJob' in scriptJob:
            scriptJobId = int(scriptJob[:scriptJob.find(':')])
            mc.scriptJob(kill=scriptJobId, force=True)


"""
def createMEvent():
    import maya.OpenMaya as OpenMaya
    global M_EVENT_ID 
    M_EVENT_ID = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", updateCtx)

def deleteMEvent():
    global M_EVENT_ID
    OpenMaya.MMessage.removeCallback(MEVENT_ID)
"""

