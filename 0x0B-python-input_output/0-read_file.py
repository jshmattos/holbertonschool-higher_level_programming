#!/usr/bin/python3

"""
This is a module for read_file.
"""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout."""
    with open(filename, 'r') as f:
        read_data = f.read()
    print(read_data, end="")
