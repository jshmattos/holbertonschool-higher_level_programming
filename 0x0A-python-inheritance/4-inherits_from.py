#!/usr/bin/python3

"""
This is a module for inherits_from.
"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class; otherwise False."""
    return isinstance(obj, a_class) and type(obj) != a_class
