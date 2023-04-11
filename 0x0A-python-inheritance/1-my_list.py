#!/usr/bin/python3
"""A module that has a class that inherits from another"""


class MyList(list):
    """Inherits from class list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
