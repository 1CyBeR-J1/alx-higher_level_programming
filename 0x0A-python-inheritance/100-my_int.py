#!/usr/bin/python3
"""Module for MyInt that inherit from int"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, value):
        """invert of =="""
        return super().__ne__(value)

    def __ne__(self, value):
        """invert of !="""
        return super().__eq__(value)
