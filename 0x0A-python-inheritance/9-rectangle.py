#!/usr/bin/python3

"""
This is a module for Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class."""

    def __init__(self, width, height):
        """Initalize Rectangle class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of class."""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
