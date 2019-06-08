#!/usr/bin/python3

"""
This is a module for Square class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of class."""
        return Rectangle.__str__(self).replace("Rectangle", "Square")


