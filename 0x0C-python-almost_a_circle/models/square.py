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
        self.size = size

    def __str__(self):
        """Return string representation of class."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for size."""
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
        self.__size = size

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args:
            if any(type(x) != int for x in args):
                raise TypeError("args must be integers")
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
