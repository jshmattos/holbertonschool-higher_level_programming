#!/usr/bin/python3

"""
This is a module for add_attribute.
"""


def add_attribute(obj, key, value):
    """Add a new attribute to an object if it’s possible."""
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, key):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
