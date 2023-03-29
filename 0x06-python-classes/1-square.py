#!/usr/bin/python3
"""A module that declares a private instance variable size"""

class Square:
    """creates a class"""
    def __init__(self, size):
        """Initializing a square
        Args:
            size (int): size of a side of the square
        """
        self.__size = size
