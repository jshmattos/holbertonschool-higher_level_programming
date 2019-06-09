#!/usr/bin/python3

"""
This is a module for Base class.
"""


import json

class Base:
    """A base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def reset_nb_objects():
        """Reset nb_objects."""
        Base.__nb_objects = 0

    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(x) != dict for x in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        res = {}
        for d in list_dictionaries:
            for k, v in d.items():
                res[k] = v
        return json.dumps([res])

