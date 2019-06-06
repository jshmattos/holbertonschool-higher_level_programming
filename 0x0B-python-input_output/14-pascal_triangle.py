#!/usr/bin/python3

"""
This is a module for pascal_triangle.
"""


def fc(n):
    """Return factorial of n."""
    if n <= 1:
        return 1
    return n * fc(n - 1)


def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal’s
    triangle of n"""
    if n <= 0:
        return [[]]
    return [[int(fc(i) / (fc(e) * fc(i - e)))
             for e in range(i + 1)] for i in range(n)]
