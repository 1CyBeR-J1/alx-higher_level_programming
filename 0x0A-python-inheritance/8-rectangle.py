#!/usr/bin/python3
"""A module that creates class to inherit another class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a Rectangle class"""
        super().integer_validator('width', width)
        super().integer_validator('height', width)
        self.__width = width
        self.__height = height
