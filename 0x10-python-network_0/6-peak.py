#!/usr/bin/python3

"""
Write a function that finds a peak in a list of unsorted integers.
"""

# naive
# def find_peak(list_of_integers):
#    """Finds a peak in a list of integers"""
#    _list = list_of_integers[::]
#    if len(set(_list)) == 1:
#        return(_list[0])
#    for i, e in enumerate(list_of_integers[:-1]):
#        if i == 0 and _list[i + 1] < _list[i]:
#            return(_list[i])
#        if i < len(_list) - 2:
#            if _list[i + 1] > e and _list[i + 2] < _list[i + 1]:
#                return(_list[i + 1])
#        elif i == len(_list) - 2:
#            if _list[i + 1] > e:
#                return _list[i + 1]
#    return None


# efficient
def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if not list_of_integers:
        return None
    left_only = right_only = True
    mid = int(len(list_of_integers) / 2)
    while mid > 0 and mid < len(list_of_integers) - 1:
        if list_of_integers[mid - 1] > list_of_integers[mid] and left_only:
            right_only = False
            mid -= 1
            continue
        if list_of_integers[mid + 1] > list_of_integers[mid] and right_only:
            left_only = False
            mid += 1
            continue
        else:
            break
    return list_of_integers[mid]
