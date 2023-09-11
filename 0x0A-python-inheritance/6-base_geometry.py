#!/usr/bin/python3
"""A module that creates a class"""


class BaseGeometry():
    """A class with Public instance method"""

    def area(self):
        """calcuculate the area"""
        raise Exception("area() is not implemented")
