#!/usr/bin/python3

"""
This is a module for BaseGeometry.
"""


class BaseGeometry():
    """A BaseGeometry class."""

    def area(self):
        """Raise an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
