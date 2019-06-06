#!/usr/bin/python3

"""
This is a module for write_file.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of
    characters written."""
    with open(filename, 'w') as f:
        chars = f.write(text)
    return chars
