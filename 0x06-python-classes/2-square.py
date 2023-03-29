#!/usr/bin/python3
"""2-square.py - A module gthat contains a Square class"""


class Square:
    """defines a square by:

    -private instance variable size
    -instatiation with optional size
    """

    def __init__(self, size=0):
        """Initializes the instance properties"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
