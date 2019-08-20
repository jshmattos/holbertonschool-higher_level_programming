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
    mid = int(len(list_of_integers) / 2)
    start = 0
    end = len(list_of_integers) - 1
    while mid > start and mid < end:
        if list_of_integers[mid - 1] > list_of_integers[mid]:
            end = mid
            mid = int(mid/2)
            continue
        if list_of_integers[mid + 1] > list_of_integers[mid]:
            start = mid
            mid = int((end + mid)/2)
            continue
        else:
            break
    return list_of_integers[mid]
