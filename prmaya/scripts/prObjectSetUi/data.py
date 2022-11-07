
import maya.cmds as mc

from . import utils


def get_all_sets():
    """ return all non-default non-component object sets from the scene """
    default_sets = ['defaultLightSet',
                    'defaultObjectSet',
                    'initialParticleSE',
                    'initialShadingGroup']
    sets = [s for s in mc.ls(type='objectSet') or [] if s not in default_sets]

    for set_ in list(sets):
        for component in ['renderableOnlySet',
                          'editPointsOnlySet',
                          'facetsOnlySet',
                          'edgesOnlySet',
                          'verticesOnlySet']:
            if mc.getAttr('{0}.{1}'.format(set_, component)):
                sets.remove(set_)
                break

    return sets


def get_dag_members(object_set):
    return utils.get_array_attr_indexed_inputs('%s.dagSetMembers' % object_set)


def get_dn_members(object_set):
    return utils.get_array_attr_indexed_inputs('%s.dnSetMembers' % object_set)


def move_array_attr_input(attr, members, move_backward=False):
    """ move array attr inputs forward or backward in order """
    all_inputs = mc.listConnections(attr, s=1, d=0)
    for each_member in members:
        if each_member not in all_inputs:
            raise NameError('%s is not part of set: %s' % (each_member, members))
    if not move_backward:
        members.reverse()

    for x, each in enumerate(members):
        all_inputs = mc.listConnections(attr, s=1, d=0)
        if not move_backward:
            all_inputs.reverse()
        target_index = all_inputs.index(each) - 1
        if target_index < x or target_index == len(all_inputs):
            continue
        utils.swap_attr_input_nodes(attr, each, all_inputs[target_index])


def add_members(object_set, members):
    # reverse, to counter maya behavior to add in reverse order
    if isinstance(members, list):
        members.reverse()
    mc.sets(members, add=object_set)


def remove_members(object_set, members):
    mc.sets(members, remove=object_set)


def add_selected(object_set):
    add_members(object_set, mc.ls(sl=1))


def remove_selected(object_set):
    remove_members(object_set, mc.ls(sl=1))


def fix_input_order(object_set):
    utils.reset_array_attr_input_order('%s.dagSetMembers' % object_set)
    utils.reset_array_attr_input_order('%s.dnSetMembers' % object_set)


def swap_array_inputs_by_index(array_attr, index_a, index_b):
    # TODO:
    # should be in utils module?
    inputs = []
    for each_index in [index_a, index_b]:
        each_attr = array_attr + '[' + str(each_index) + ']'
        each_input = mc.listConnections(each_attr, s=1, d=0, p=1)
        if each_input is None:
            raise NameError('no input at given index: %s' % each_attr)
        inputs.append(each_input[0])

    inputs.reverse()
    for each_input, each_index in zip(inputs, [index_a, index_b]):
        each_attr = array_attr + '[' + str(each_index) + ']'
        mc.connectAttr(each_input, each_attr, f=1)
