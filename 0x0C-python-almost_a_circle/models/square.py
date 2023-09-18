#!/usr/bin/python3
"""Module that contains a class square that inherits a base class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the attribute size"""
        self.width = value
        self.height = value

    def __str__(self):
        """the string method that returns a string"""
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width)

    def update(self, *args, **kwargs):
        """Update method that assigns attributes"""
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        i = 0
        for arg in args:
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]
            i += 1

    def to_dictionary(self):
        """returns the dict representation of Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
