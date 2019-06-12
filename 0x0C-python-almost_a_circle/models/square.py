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
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of Square."""
        d = {}
        for k, v in vars(self).items():
            if k.startswith("_"):
                if not k.endswith("width") and not k.endswith("height"):
                    idx = k.index("__")
                    d[k[idx + 2:]] = v
            else:
                d[k] = v
        return d
