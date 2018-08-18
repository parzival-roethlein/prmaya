""""

import prmaya.scripts.prObjectSetUi.utils as object_set_utils
reload(object_set_utils)
object_set_utils.reload_all()

import sys
sys.path.append(r'C:\Users\paz\Documents\git\prmaya\test\scripts')

import test_prObjectSetUi
reload(test_prObjectSetUi)
test_prObjectSetUi.run()

"""

import unittest

try:
    import maya.cmds as mc
    from prmaya.scripts.prObjectSetUi import data
except Exception as e:
    print('import error: %s' % e)

OPTIONS = {
    'scene': r'C:\Users\paz\Documents\git\prmaya\test\scripts\test_prObjectSetUi_scene.ma',
}

OBJECTS = {
    'all_set': 'all_set',
    'empty_set': 'empty_set',

    'gap_set': 'gap_set',
    'gap_set_child_1': 'gap_set_child_1',
    'gap_set_child_2': 'gap_set_child_2',
    'wrongOrder_set': 'wrongOrder_set',

    'pCube1': 'pCube1',
    'pCube2': 'pCube2',
    'pCube3': 'pCube3',
}


class MayaSetUpTearDown(unittest.TestCase):
    def setUp(self):
        mc.file(OPTIONS['scene'], open=True, force=True)
        mc.file(rename=OPTIONS['scene'].replace('.ma', '_TMP.ma'))
        mc.file(renameToSave=True)

    def tearDown(self):
        # mc.file(new=1, force=True)
        pass


def get_members(set_):
    return (mc.listConnections('{}.dagSetMembers'.format(set_)) or []) + \
           (mc.listConnections('{}.dnSetMembers'.format(set_)) or [])


class TestAddRemove(MayaSetUpTearDown):
    def test_addOneObject(self):
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(members, [])
        data.add_members(OBJECTS['empty_set'], OBJECTS['pCube1'])
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(len(members), 1)
        self.assertEqual(members, [OBJECTS['pCube1']])

    def test_addMultipleObjects(self):
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(members, [])
        data.add_members(OBJECTS['empty_set'], [OBJECTS['pCube1'],
                                                OBJECTS['pCube2'],
                                                OBJECTS['pCube3'], ])
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(len(members), 3)
        self.assertEqual(members, [OBJECTS['pCube1'],
                                   OBJECTS['pCube2'],
                                   OBJECTS['pCube3'], ])

    def test_removeOneObject(self):
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 3)
        data.remove_members(OBJECTS['all_set'], OBJECTS['pCube1'])
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 2)
        self.assertEqual(members, [OBJECTS['pCube2'],
                                   OBJECTS['pCube3'], ])

    def test_removeMultipleObject(self):
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 3)
        data.remove_members(OBJECTS['all_set'], [OBJECTS['pCube1'],
                                                 OBJECTS['pCube2'], ])
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 1)
        self.assertEqual(members, [OBJECTS['pCube3']])

    def test_addOneSelected(self):
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(members, [])
        mc.select(OBJECTS['pCube1'])
        data.add_selected(OBJECTS['empty_set'])
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(len(members), 1)
        self.assertEqual(members, [OBJECTS['pCube1']])

    def test_addMultipleSelected(self):
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(members, [])
        mc.select([OBJECTS['pCube1'], OBJECTS['pCube2']])
        data.add_selected(OBJECTS['empty_set'])
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(len(members), 2)
        self.assertEqual(members, [OBJECTS['pCube1'],
                                   OBJECTS['pCube2'], ])

    def test_removeOneSelected(self):
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 3)
        mc.select(OBJECTS['pCube1'])
        data.remove_selected(OBJECTS['all_set'])
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 2)
        self.assertEqual(members, [OBJECTS['pCube2'],
                                   OBJECTS['pCube3'], ])

    def test_removeMultipleSelected(self):
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 3)
        mc.select([OBJECTS['pCube1'], OBJECTS['pCube2']])
        data.remove_selected(OBJECTS['all_set'])
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 1)
        self.assertEqual(members, [OBJECTS['pCube3']])

    def test_addExisting(self):
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 3)
        data.add_members(OBJECTS['all_set'], OBJECTS['pCube1'])
        members = get_members(OBJECTS['all_set'])
        self.assertEqual(len(members), 3)

    def test_removeMissing(self):
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(members, [])
        data.remove_members(OBJECTS['empty_set'], OBJECTS['pCube1'])
        members = get_members(OBJECTS['empty_set'])
        self.assertEqual(members, [])


class TestReorder(MayaSetUpTearDown):
    def test_resetInputOrder_dag(self):
        # create gap
        mc.disconnectAttr(OBJECTS['pCube3'] + '.instObjGroups[0]', OBJECTS['gap_set'] + '.dagSetMembers[1]')
        mc.connectAttr(OBJECTS['pCube3'] + '.instObjGroups[0]', OBJECTS['gap_set'] + '.dagSetMembers[3]')
        for each_index, each_input in ((0, [OBJECTS['pCube1'] + '.instObjGroups']),
                                       (1, None),
                                       (2, None),
                                       (3, [OBJECTS['pCube3'] + '.instObjGroups']),
                                       ):
            input_attr = OBJECTS['gap_set'] + '.dagSetMembers[' + str(each_index) + ']'
            each_result = mc.listConnections(input_attr, s=1, d=0, p=1)
            self.assertEqual(each_result, each_input)
        # close gap
        data.fix_input_order(OBJECTS['gap_set'])
        for each_index, each_input in ((0, [OBJECTS['pCube1'] + '.instObjGroups']),
                                       (1, [OBJECTS['pCube3'] + '.instObjGroups']),
                                       (2, None),
                                       (3, None),
                                       ):
            input_attr = OBJECTS['gap_set'] + '.dagSetMembers[' + str(each_index) + ']'
            each_result = mc.listConnections(input_attr, s=1, d=0, p=1)
            self.assertEqual(each_result, each_input)

    def test_resetInputOrder_dn(self):
        # create gap
        mc.disconnectAttr(OBJECTS['gap_set_child_2'] + '.message', OBJECTS['gap_set'] + '.dnSetMembers[1]')
        mc.connectAttr(OBJECTS['gap_set_child_2'] + '.message', OBJECTS['gap_set'] + '.dnSetMembers[3]')
        for each_index, each_input in ((0, [OBJECTS['gap_set_child_1'] + '.message']),
                                       (1, None),
                                       (2, None),
                                       (3, [OBJECTS['gap_set_child_2'] + '.message']),
                                       ):
            input_attr = OBJECTS['gap_set'] + '.dnSetMembers[' + str(each_index) + ']'
            each_result = mc.listConnections(input_attr, s=1, d=0, p=1)
            self.assertEqual(each_result, each_input)
        # close gap
        data.fix_input_order(OBJECTS['gap_set'])
        for each_index, each_input in ((0, [OBJECTS['gap_set_child_1'] + '.message']),
                                       (1, [OBJECTS['gap_set_child_2'] + '.message']),
                                       (2, None),
                                       (3, None),
                                       ):
            input_attr = OBJECTS['gap_set'] + '.dnSetMembers[' + str(each_index) + ']'
            each_result = mc.listConnections(input_attr, s=1, d=0, p=1)
            self.assertEqual(each_result, each_input)

    def test_swapObjectsByIndex(self):
        for each_index, each_input in ((0, [OBJECTS['pCube1'] + '.instObjGroups']),
                                       (1, [OBJECTS['pCube3'] + '.instObjGroups']),
                                       (2, [OBJECTS['pCube2'] + '.instObjGroups']),
                                       ):
            input_attr = OBJECTS['wrongOrder_set'] + '.dagSetMembers[' + str(each_index) + ']'
            each_result = mc.listConnections(input_attr, s=1, d=0, p=1)
            self.assertEqual(each_result, each_input)
        data.swap_array_inputs_by_index(OBJECTS['wrongOrder_set'] + '.dagSetMembers', 1, 2)

        for each_index, each_input in ((0, [OBJECTS['pCube1'] + '.instObjGroups']),
                                       (1, [OBJECTS['pCube2'] + '.instObjGroups']),
                                       (2, [OBJECTS['pCube3'] + '.instObjGroups']),
                                       ):
            input_attr = OBJECTS['wrongOrder_set'] + '.dagSetMembers[' + str(each_index) + ']'
            each_result = mc.listConnections(input_attr, s=1, d=0, p=1)
            self.assertEqual(each_result, each_input)


def run():
    all_tests = unittest.TestSuite()
    for test in [TestAddRemove, TestReorder]:
        all_tests.addTest(unittest.makeSuite(test))
    result = unittest.TextTestRunner(verbosity=2).run(all_tests)
    print('===\ntest result:\n%s\n===\n' % result)
