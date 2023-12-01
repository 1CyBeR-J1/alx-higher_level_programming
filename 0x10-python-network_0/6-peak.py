#!/usr/bin/python3
"""Module that contains the function"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    mid = size // 2

    if length == 0:
        return None

    while True:
        length = length // 2
        if (mid < length - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if length // 2 == 0:
                length = 2
            mid = mid + length // 2
        elif length > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if length // 2 == 0:
                length = 2
            mid = mid - length // 2
        else:
            return list_of_intergers[mid]
