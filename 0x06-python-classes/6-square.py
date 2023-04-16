#!/usr/bin/python3
"""Module that icludes the class Square"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the instance attribute"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a new value for the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if isinstance(value, tuple) or len(value) == 2 or \
                isinstance(value[0], int) or \
                isinstance(value[1], int) or value[0] > 0 \
                or value[1] > 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
