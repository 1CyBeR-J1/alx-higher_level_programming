#!/usr/bin/python3
"""A module that creates class to inherit another class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a Rectangle class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calucalates the area of Rectangle"""
        return self.__width * self__height

    def __str__(self):
        """Return the Rectangle description"""
        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                self.__width, self__height)
