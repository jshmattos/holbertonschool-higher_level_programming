#!/usr/bin/python3

"""
This is a module for pascal_triangle.
"""

from math import factorial as fc

def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    return [[int(fc(i) / (fc(e) * fc(i - e)))
             for e in range(i + 1)] for i in range(n)]
