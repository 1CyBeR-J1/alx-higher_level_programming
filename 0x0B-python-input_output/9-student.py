#!/usr/bin/python3
"""Module that contains a class Student"""


class Student:
    """defines a Student"""
    def __init__(self, first_name, last_name, age):
        """initialization of the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict rep of a Student instance"""
        return self.__dict__
