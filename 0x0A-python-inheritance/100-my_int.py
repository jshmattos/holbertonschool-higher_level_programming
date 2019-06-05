#!/usr/bin/python3

"""
This is a module for MyInt.
"""


class MyInt(int):
    """A MyInt class."""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
