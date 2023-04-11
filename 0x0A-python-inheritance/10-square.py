#!/usr/bin/python3
"""A module that creates a Square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle class"""


    def __init__(self, size):
        """initializing the Square"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of the Square"""
        return self__size ** 2
