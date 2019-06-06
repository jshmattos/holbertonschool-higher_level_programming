#!/usr/bin/python3

"""
This is a module for append_write.
"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8) and return the
    number of characters added."""
    with open(filename, 'a') as f:
        chars = f.write(text)
    return chars
