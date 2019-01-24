"""

import sys
sys.path.append('/home/prthlein/private/code/prmaya/test/plugins')
import test_prRemapValue
reload(test_prRemapValue)
test_prRemapValue.run()


import sys
sys.path.append('C:/Users/paz/Documents/git/prmaya/test/plugins')
import test_prRemapValue
reload(test_prRemapValue)
test_prRemapValue.SETTINGS['plugin_path'] = r'C:\Users\paz\Documents\git\prmaya\prmaya\plugins\prRemapValue.py'
test_prRemapValue.SETTINGS['file'] = r'C:\Users\paz\Documents\git\prmaya\test\plugins\test_prRemapValue_scene.ma'
test_prRemapValue.run()


import maya.cmds as mc
mc.file(new=True, force=True)
mc.file(rename='/home/prthlein/private/Documents/asdf.ma')
mc.createNode('prRemapValue')
mc.createNode('prRemapValue')
#mc.getAttr('prRemapValue1.outValue')
mc.connectAttr('prRemapValue1.outValue', 'prRemapValue2.inputValue')
mc.file(save=True, typ='mayaAscii')
mc.file(new=True, force=True)
mc.file('/home/prthlein/private/Documents/asdf.ma', open=True, force=True)



"""

import maya.cmds as mc
from prmaya.plugins import prRemapValue

reload(prRemapValue)

SETTINGS = {'plugin_name': 'prRemapValue.py',
            'plugin_path': '/home/prthlein/private/code/prmaya/prmaya/plugins/prRemapValue.py',
            'file': '/home/prthlein/private/code/prmaya/test/plugins/test_prRemapValue.ma',
            }


def run():
    mc.file(newFile=True, force=True)
    mc.unloadPlugin(SETTINGS['plugin_name'])
    mc.loadPlugin(SETTINGS['plugin_path'])
    mc.file(SETTINGS['file'], open=True, force=True)
    mc.file(rename='asdf')
    mc.file(renameToSave=True)

    mc.createNode('prRemapValue')
    mc.setAttr("prRemapValue1.value[1].value_Position", 1)
    mc.setAttr("prRemapValue1.value[1].value_FloatValue", 1)

    for x in range(5):
        mc.setAttr('prRemapValue1.inputValue[{}]'.format(x), 1.0/4 * x)
        mc.connectAttr('prRemapValue1.outValue[{}]'.format(x), 'pCube{}.ty'.format(x+2))

    print(mc.getAttr('prRemapValue1.outValue'))
    #mc.select('prRemapValue1')
