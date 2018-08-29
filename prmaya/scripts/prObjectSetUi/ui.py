"""

import prmaya.scripts.prObjectSetUi.utils as object_set_ui_utils
reload(object_set_ui_utils)
object_set_ui_utils.reload_all()
object_set_ui_utils.ui()


TODO:
- text scroll list selection order gets lost
"""

import os
from functools import wraps

import maya.cmds as mc
import pymel.core as pm

from . import file_utils
from . import data


DEFAULTS = {
    'config_folder': r'C:\Users\paz\Documents\git\prmaya\prmaya\scripts\prObjectSetUi',
    'select_members_in_scene': True,
}


def refresh_ui(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.load_members()
        return result
    return wrapper


class UI(pm.uitypes.Window):
    name = 'prObjectSetUi'
    version = '0.0.5'

    def __new__(cls, **options):
        if pm.window(cls.name, exists=True):
            pm.deleteUI(cls.name)
        title = '{0}_v{1}'.format(cls.name, cls.version.replace('.', ''))
        self = pm.window(cls.name, title=title, width=400, height=500, menuBar=True)
        return pm.uitypes.Window.__new__(cls, self)

    def __init__(self, **options):
        super(UI, self).__init__(**options)
        
        pm.menu(label='Options', tearOff=True, parent=self)
        pm.menuItem(label='Export members', c=pm.Callback(self.export_members))
        pm.menuItem(label='Import members', c=pm.Callback(self.import_members))
        pm.menuItem(label='---', enable=False)
        self.select_members_in_scene = pm.menuItem('Select members in scene', checkBox=DEFAULTS['select_members_in_scene'])

        with pm.verticalLayout() as main_layout:
            with pm.horizontalLayout() as content_layout:
                with pm.verticalLayout() as set_layout:
                    with pm.verticalLayout() as set_top_layout:
                        pm.button(label='load selection', c=pm.Callback(self.load_sets_from_selection))
                        pm.button(label='load all', c=pm.Callback(self.load_sets_from_scene))
                        pm.separator()
                        pm.button(label='select in scene', c=pm.Callback(self.select_sets_in_scene))
                    set_top_layout.redistribute()
                    self.sets_list = pm.textScrollList(allowMultiSelection=True, sc=pm.Callback(self.load_members))
                    # load_members
                set_layout.redistribute(0, 1)
                with pm.verticalLayout() as member_layout:
                    with pm.verticalLayout() as member_head_layout:
                        self.active_set = pm.textField(enable=False)
                        with pm.horizontalLayout() as member_selection_layout:
                            pm.button(label='+', c=pm.Callback(self.add_members_from_selection))
                            pm.button(label='-', c=pm.Callback(self.remove_members_from_selection))
                            pm.button(label='fix', c=pm.Callback(self.fix_member_order))
                        member_selection_layout.redistribute()
                        pm.separator()
                    member_head_layout.redistribute()

                    with pm.horizontalLayout() as dag_layout:
                        self.dag_member_list = pm.textScrollList(allowMultiSelection=True, sc=pm.Callback(self.dag_selection))
                        with pm.verticalLayout(w=20) as dag_button_layout:
                            pm.text('dag')
                            pm.button(label='UP', c=pm.Callback(self.move_dag_members_up))
                            pm.button(label='DN', c=pm.Callback(self.move_dag_members_down))
                            pm.button(label='-', c=pm.Callback(self.remove_active_dag_member))
                        dag_button_layout.redistribute()
                    dag_layout.redistribute(3, 1)

                    with pm.horizontalLayout() as dn_layout:
                        self.dn_member_list = pm.textScrollList(allowMultiSelection=True, sc=pm.Callback(self.dn_selection))
                        with pm.verticalLayout(w=20) as dn_button_layout:
                            pm.text('dn')
                            pm.button(label='UP', c=pm.Callback(self.move_dn_members_up))
                            pm.button(label='DN', c=pm.Callback(self.move_dn_members_down))
                            pm.button(label='-', c=pm.Callback(self.remove_active_dn_member))
                        dn_button_layout.redistribute()
                    dn_layout.redistribute(3, 1)
                member_layout.redistribute(0, 1, 1)
            content_layout.redistribute(4, 5)
        main_layout.redistribute()

        self.show()
        self.load_sets_from_selection()

    def load_members(self):
        object_set = self.sets_list.getSelectItem()
        if not object_set:
            return
        object_set = object_set[-1]
        self.active_set.setText(object_set)
        for func, text_scroll_list in [[data.get_dag_members, self.dag_member_list],
                                       [data.get_dn_members, self.dn_member_list]]:
            active_members = self.get_active_members_as_dict(text_scroll_list)
            text_scroll_list.removeAll()
            members = func(object_set)
            if not members:
                continue
            for index, item in members.items():
                text_scroll_list.append('%s: %s' % (index, item))
            self.set_active_members_from_dict(text_scroll_list, active_members)

    # ####################################
    # SET
    # ####################################

    def load_sets(self, object_sets):
        self.sets_list.removeAll()
        self.dag_member_list.removeAll()
        self.dn_member_list.removeAll()
        if not object_sets:
            return
        for set_ in object_sets:
            self.sets_list.append(set_)
        self.load_members()
        # pymel bug
        # TextScrollList.selectIndexedItems broken
        # also used by TextScrollList.selectAll()
        # self.sets_list.selectAll() # pymel command bugged
        # self.sets_list.selectIndexedItems(range(self.sets_list.getNumberOfItems()))
        for item in self.sets_list.getAllItems():
            self.sets_list.setSelectItem(item)

    @refresh_ui
    def load_sets_from_selection(self):
        set_selection = mc.ls(sl=True, type='objectSet') or []
        self.load_sets(set_selection)
        if len(set_selection) > 0:
            self.sets_list.setSelectIndexedItem(len(set_selection))

    @refresh_ui
    def load_sets_from_scene(self):
        object_sets = data.get_all_sets()
        self.load_sets(object_sets)

    def select_sets_in_scene(self):
        mc.select(self.sets_list.getSelectItem(), noExpand=True)

    def get_active_set(self):
        name = self.active_set.getText()
        if name == '':
            raise NameError('No active set')
        return name

    def export_members(self):
        selected_sets = self.sets_list.getSelectItem()
        members = []
        for object_set in selected_sets:
            members += mc.sets(object_set, q=True)

        file_path = file_utils.file_dialog_2(startingDirectory=DEFAULTS['config_folder'])
        if not file_path:
            return
        if os.path.isfile(file_path):
            old_data = file_utils.read_file(file_path)
            if isinstance(old_data, list):
                members += old_data

        members = sorted(list(set(members)))
        file_utils.write_file(file_path, members)

    @refresh_ui
    def import_members(self):
        file_path = file_utils.file_dialog_2(startingDirectory=DEFAULTS['config_folder'], fileMode=1)
        if not file_path:
            return
        new_members = file_utils.read_file(file_path)
        if not isinstance(new_members, list):
            raise ValueError('expected list, got: %s' % new_members)
        new_members = list(set(new_members))
        for member in new_members[:]:
            if not mc.objExists(member):
                new_members.remove(member)

        for object_set in self.sets_list.getSelectItem():
            for member in new_members:
                try:
                    mc.sets(member, add=object_set)
                except RuntimeError as e:
                    print(e)

    # ####################################
    # MEMBERS
    # ####################################

    def dag_selection(self):
        if pm.menuItem(self.select_members_in_scene, q=True, checkBox=True):
            mc.select(self.get_active_member_names(self.dag_member_list), noExpand=True)

    def dn_selection(self):
        if pm.menuItem(self.select_members_in_scene, q=True, checkBox=True):
            mc.select(self.get_active_member_names(self.dn_member_list), noExpand=True)

    @refresh_ui
    def add_members_from_selection(self):
        object_set = self.get_active_set()
        data.add_selected(object_set)

    @refresh_ui
    def remove_members_from_selection(self):
        data.remove_selected(self.get_active_set())

    @refresh_ui
    def fix_member_order(self):
        data.fix_input_order(self.get_active_set())

    @refresh_ui
    def remove_members(self, members):
        object_set = self.get_active_set()
        data.remove_members(object_set, members)

    @staticmethod
    def get_member_names(text_scroll_list):
        names = []
        for item in text_scroll_list.getAllItems():
            names.append(item[item.rfind(' ') + 1:])
        return names

    def get_active_member_names(self, member_text_scroll_list):
        active_indices = member_text_scroll_list.getSelectIndexedItem()
        if not active_indices:
            return []
        all_names = self.get_member_names(member_text_scroll_list)
        active_names = [all_names[index - 1] for index in active_indices]
        return active_names

    def get_active_dag_member_names(self):
        return self.get_active_member_names(self.dag_member_list)

    def get_active_dn_member_names(self):
        return self.get_active_member_names(self.dn_member_list)

    def get_active_members_as_dict(self, text_scroll_list):
        active_indices = text_scroll_list.getSelectIndexedItem()
        active_names = self.get_active_member_names(text_scroll_list)
        active_dict = {}
        for x, name in enumerate(active_names):
            active_dict[name] = active_indices[x]
        return active_dict

    def set_active_members_from_dict(self, text_scroll_list, member_dict):
        all_members = self.get_member_names(text_scroll_list)
        if not all_members:
            return
        to_activate_indices = set()
        for name, index in member_dict.items():
            select_index = index
            if name in all_members:
                select_index = all_members.index(name) + 1
            elif select_index > len(all_members):
                select_index = len(all_members)
            to_activate_indices.add(select_index)
        text_scroll_list.setSelectIndexedItem(to_activate_indices)

    def remove_active_dag_member(self):
        self.remove_members(self.get_active_dag_member_names())

    def remove_active_dn_member(self):
        self.remove_members(self.get_active_dn_member_names())

    @refresh_ui
    def move_members(self, members, attr, move_backward=False):
        object_set = self.get_active_set()
        data.move_array_attr_input(('%s.%s' % (object_set, attr)), members, move_backward)

    def move_dag_members_up(self):
        self.move_members(self.get_active_dag_member_names(), 'dagSetMembers', move_backward=True)

    def move_dag_members_down(self):
        self.move_members(self.get_active_dag_member_names(), 'dagSetMembers')

    def move_dn_members_up(self):
        self.move_members(self.get_active_dn_member_names(), 'dnSetMembers', move_backward=True)

    def move_dn_members_down(self):
        self.move_members(self.get_active_dn_member_names(), 'dnSetMembers')
