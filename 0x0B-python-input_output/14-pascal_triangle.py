#!/usr/bin/python3

"""
This is a module for pascal_triangle.
"""

from math import factorial as fc

def pascal_triangle(n):
    return [[int(fc(i)/(fc(e) * fc(i - e))) for e in range(i + 1)] for i in range(n)]
