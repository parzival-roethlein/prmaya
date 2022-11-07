import maya.cmds as mc

from collections import OrderedDict


def reload_all():
    from . import data
    from . import ui
    from . import file_utils
    for module_ in [data, file_utils, ui]:
        print('reloading: {}'.format(module_))
        reload(module_)


def ui():
    from . import ui
    ui.UI()


def reset_array_attr_input_order(array_attr):
    # TODO: refactor with get_array_attr_indexed_inputs()
    array_inputs = mc.listConnections(array_attr, source=True, destination=False, plugs=True) or []
    if not array_inputs:
        return

    # disconnect all
    counter = -1
    hits = 0
    while True:
        counter += 1
        if counter > 2000:
            raise Exception('counter > 2000')
        if hits == len(array_inputs):
            break
        array_plug = '{0}[{1}]'.format(array_attr, counter)
        input_ = mc.listConnections(array_plug, source=True, destination=False, plugs=True)
        if input_:
            hits += 1
            mc.disconnectAttr(input_[0], array_plug)

    # reconnect
    for x, input_ in enumerate(array_inputs):
        mc.connectAttr(input_, '{0}[{1}]'.format(array_attr, x), force=True)


def get_array_attr_indexed_inputs(array_attr, plugs=False):
    indexed_inputs = OrderedDict()

    inputs = mc.listConnections(array_attr, s=1, d=0, plugs=plugs) or []
    if not inputs:
        return indexed_inputs

    counter = -1
    hits = 0
    while True:
        counter += 1
        if hits == len(inputs):
            break
        if counter > 9000:
            raise NameError('counter > 9000')

        each_array_attr = '%s[%s]' % (array_attr, counter)
        each_input = mc.listConnections(each_array_attr, s=1, d=0, plugs=plugs)
        if each_input:
            if len(each_input) == 1:
                each_input = each_input[0]
            hits += 1
            indexed_inputs[counter] = each_input
    return indexed_inputs


def swap_attr_input_nodes(array_attr, node_one, node_two):
    input_nodes = get_array_attr_indexed_inputs(array_attr)
    input_plugs = get_array_attr_indexed_inputs(array_attr, plugs=True)
    indices = input_nodes.keys()
    nodes = input_nodes.values()
    plugs = input_plugs.values()
    for each_node in [node_one, node_two]:
        if each_node not in nodes:
            raise NameError('node: %s // not connected to: %s' % (each_node, array_attr))
    node_one_output = plugs[nodes.index(node_one)]
    node_one_input = '%s[%s]' % (array_attr, indices[nodes.index(node_two)])
    mc.connectAttr(node_one_output, node_one_input, force=True)
    mc.connectAttr(plugs[nodes.index(node_two)], '%s[%s]' % (array_attr, indices[nodes.index(node_one)]), force=True)
