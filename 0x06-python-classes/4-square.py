#!/usr/bin/python3

"""4-square.py - A module that contains a Square class"""


class Square:
    """defines a square by:

    - private instance variable: size
    - Instantiation with optional size
    """

    def __init__(self, size=0):
        """Initialize the instance properties"""
        self.size = size

    @property
    def size(self):
        """Retrives the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the new value for the size of the square"""
        if not ininstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size mus be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
