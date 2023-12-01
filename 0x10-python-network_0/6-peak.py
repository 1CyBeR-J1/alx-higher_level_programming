#!/usr/bin/python3
"""Module that contains the function"""


def find_peak(list_of_integer):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integer:
        return None

    length = len(list_of_integer)

    if length == 1 or length == 2:
        return max(ints_list)

    left, right = 0, length - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
