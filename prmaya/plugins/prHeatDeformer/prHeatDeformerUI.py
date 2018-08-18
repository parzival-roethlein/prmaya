'''
UI to create / edit prHeatDeformer

T E S T:
# #########################
import sys
sys.path.append( r'C:\Users\pz\Documents\git\prtools\plug-ins\prHeatDeformer' )
import prHeatDeformerUI;reload( prHeatDeformerUI )
prHeatDeformerUI.UI()
# #########################
'''
import pymel.core as pm
import maya.mel as mm

class UI(pm.uitypes.Window):
    '''
    window of prSelectionUi.
    Maya-UI-Hierarchy:
    (UI:)      window > formLayout > horizontalLayout > optionMenu, tabLayout
    (Set:)     verticalLayout >
    (Element:) horizontalLayout > buttons (+,select,- OR pose)
    '''
    
    # constants
    _TITLE = 'prHeatDeformerUI_005'
    #_FORMLAYOUT_MAIN = 'prHeatForm'
    #_FORMLAYOUT_DEFORMER = 'prHeatFormDeformer'
    #_FORMLAYOUT_CONNECT = 'prHeatFormConnect'
    
    # variables
    currentDeformer = ''
    heatTextField = None
    resultTextField = None
    formResult = None
    
    def __new__(cls):
        ''' delete possible old window and create new instance '''
        if pm.window(cls._TITLE, exists=True):
            pm.deleteUI( cls._TITLE )
        self = pm.window(cls._TITLE, title=cls._TITLE)
        return pm.uitypes.Window.__new__(cls, self)
    
    def __init__(self):
        '''
        create UI elements (layouts, buttons)
        show window
        '''
        # formLayout base
        form = pm.verticalLayout()
        with form:
            formDeformer = pm.horizontalLayout()
            with formDeformer:
                pm.button( l='Create', c=pm.Callback( self.create ) )
                pm.button( l='Load', c=pm.Callback( self.load ) )
                self.heatTextField = pm.textField( en=0 )
            formDeformer.redistribute()
            formConnect = pm.horizontalLayout( )
            with formConnect:
                pm.button( l='Connect Squash', c=pm.Callback( self.connect, 'squash' ) )
                pm.button( l='Connect Stretch', c=pm.Callback( self.connect, 'stretch' ) )
                pm.button( l='Connect Base', c=pm.Callback( self.connect, 'base' ) )
            formConnect.redistribute()
            self.formResult = pm.horizontalLayout()
            self.formResult.setBackgroundColor( [0,0,0] )
            self.formResult.setEnableBackground(0)
            with self.formResult:
                self.resultTextField = pm.textField( en=0 )
            self.formResult.redistribute()
        form.redistribute()
        # show window
        self.show()
    
    def create(self):
        print 'create heatdeformer ...'
        # create deformer
        try:
            newDeformer = mm.eval( 'prHeatDeformer' )
        except:
            self.currentDeformer = ''
            self.result( -1, 'Error: Invalid selection, check scriptEditor' )
            return
        newDeformer = pm.PyNode( newDeformer )
        self.heatTextField.setText( newDeformer )
        self.currentDeformer = newDeformer
        # finish
        self.result( 1, '... heatDeformer created' )
    
    def load(self):
        print 'load heatdeformer ...'
        # get selection
        sel = pm.ls(sl=1)
        if( len(sel) == 0 ):
            self.result( 0, '... cleared' )
        elif( len(sel) != 1 or pm.nodeType(sel[0]) != 'prHeatDeformer' ):
            self.currentDeformer = ''
            self.result( -1, 'Error: Must select one prHeatDeformer node for loading!' )
        else:
            self.currentDeformer = sel[0]
            self.result( 1, '... loaded successfully' )
    
    def result(self, mode, outMessage ):
        ''' 
        update result textField and possible error 
        mode:
        -1= error
        0 = clear
        1 = success
        '''
        if( mode == 0 ):
            self.currentDeformer = ''
            self.formResult.setBackgroundColor( [0,0,0] )
            self.resultTextField.setText( '' )
        elif( mode == 1 ):
            self.formResult.setBackgroundColor( [0.2,1.0,0.2] )
            self.resultTextField.setText( outMessage )
        elif( mode == -1 ):
            self.formResult.setBackgroundColor( [1.0,0.6,0.6] )
            self.resultTextField.setText( outMessage )
        self.formResult.setEnableBackground( 0 )# to get frame effect, and setting background color always enables again
        self.heatTextField.setText( self.currentDeformer )
        print outMessage
    
    def connect(self, meshType):
        print 'connect selected transforms shapes to loaded prHeatDeformer ...'
        # check for deformer
        if( not self.currentDeformer ):
            self.result( -1, 'Error: Load or create a prHeatDeformer first!' )
            return
        # get outputGeom
        currentTransform = self.currentDeformer.outputGeometry[0].outputs()[0]
        currentShapes = pm.listRelatives( currentTransform, shapes=1, f=1, ni=1, children=1 )
        # get selection
        selectedTransform = pm.ls( sl=1 )
        # check selection
        if( len(selectedTransform) != 1 or len(selectedTransform) != len( pm.ls( sl=1, type='transform') ) ):
            self.result( -1, 'Error: Invalid selection! Select one transform' )
            return
        # get shapes
        selectedShapes = pm.listRelatives( selectedTransform[0], shapes=1, f=1, ni=1, children=1 )
        # check if selection is valid
        if( len(selectedTransform) != 1 or len(selectedTransform) != len( pm.ls( sl=1, type='transform') ) ):
            self.result( -1, 'Invalid selection! Shape count does not match with target mesh shape count' )
            return
        # connect prHeatDeformer1.perGeometry[0].origMesh;
        if( meshType == 'base' ):
            targetAttr = 'origMesh'
        elif( meshType == 'squash' ):
            targetAttr = 'squashMesh'
        elif( meshType == 'stretch' ):
            targetAttr = 'stretchMesh'
        for x, eachShape in enumerate( selectedShapes ):
            eachShape.outMesh >> self.currentDeformer.perGeometry[x].attr( targetAttr )
        # finish
        self.result( 1, 'Connected '+meshType+' successfully' )
#
