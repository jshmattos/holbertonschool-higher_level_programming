#!/usr/bin/python3

"""
This is a module for Base class.
"""

class Base:
    """A base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a base."""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
