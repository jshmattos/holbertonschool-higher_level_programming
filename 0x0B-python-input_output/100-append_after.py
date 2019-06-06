#!/usr/bin/python3

"""
This is a module for append_after.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line containing
    a specific string."""
    with open(filename, 'r') as f:
        data = f.readlines()

    output = ""
    for line in data:
        output += line
        if search_string in line:
            output += new_string

    with open(filename, 'w') as f:
        f.write(output)
