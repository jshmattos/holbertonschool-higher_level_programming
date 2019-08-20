#!/usr/bin/python3

"""
Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    _list = list_of_integers[::]
    if len(set(_list)) == 1:
        return(_list[0])
    for i, e in enumerate(list_of_integers[:-1]):
        if i == 0 and _list[i + 1] < _list[i]:
            return(_list[i])
        if i < len(_list) - 2:
            if _list[i + 1] > e and _list[i + 2] < _list[i + 1]:
                return(_list[i + 1])
        elif i == len(_list) - 1:
            if _list[i + 1] > e:
                return _list[i + 1]
    return None
