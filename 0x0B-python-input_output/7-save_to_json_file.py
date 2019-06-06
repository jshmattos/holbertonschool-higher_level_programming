#!/usr/bin/python3

"""
This is a module for save_to_json_file.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation."""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
