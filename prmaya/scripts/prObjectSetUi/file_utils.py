import json

import maya.cmds as mc


OPTIONS = {
    'file_type_filter': '*.json'
}


def write_file(file_path, export_data):
    """ write given data in given file_path"""
    print('writing file: %s' % file_path)
    with open(file_path, 'w') as outfile:
        json.dump(export_data, outfile, sort_keys=True, indent=2)


def read_file(file_path):
    print('reading file: %s' % file_path)
    f = open(file_path)
    return json.load(f)


def file_dialog_2(*args, **kwargs):
    """
    mc.fileDialog2 wrapper
    """
    kwargs.setdefault('fileFilter', OPTIONS['file_type_filter'])
    kwargs.setdefault('dialogStyle', 1)
    file_path = mc.fileDialog2(*args, **kwargs)
    print('got dialog file path: %s' % file_path)
    if file_path:
        return file_path[0]
    return None
