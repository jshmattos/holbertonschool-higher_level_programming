#!/usr/bin/python3

"""
This is a module for Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square."""

    def __init__(self, size):
        """Initialize Square class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of square."""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
