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
# def find_peak(list_of_integers):
#    """Finds a peak in a list of integers"""
#    if not list_of_integers:
#        return None
#    left_only = right_only = True
#    mid = int(len(list_of_integers) / 2)
#    while mid > 0 and mid < len(list_of_integers) - 1:
#        if _list_of_integers[mid - 1] > _list_of_integers[mid] and left_only:
#            right_only = False
#            mid -= 1
#            continue
#        if _list_of_integers[mid + 1] > _list_of_integers[mid] and right_only:
#            left_only = False
#            mid += 1
#            continue
#        else:
#            break
#    return list_of_integers[mid]


# even more effecient
def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if not list_of_integers:
        return None

    def fp(arr, low, high, n):
        """Helper func"""
        mid = low + (high - low)//2
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and\
           (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]
        elif (mid > 0 and arr[mid - 1] > arr[mid]):
            return fp(arr, low, mid - 1, n)
        else:
            return fp(arr, mid + 1, high, n)
    return fp(list_of_integers, 0, len(list_of_integers) - 1,
              len(list_of_integers))
