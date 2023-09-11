#!/usr/bin/python3
"""A module that creates a class"""


class BaseGeometry():
    """A class with Public instance method"""

    def area(self):
        """calcuculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value inputted"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
