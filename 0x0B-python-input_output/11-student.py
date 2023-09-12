#!/usr/bin/python3
"""Module contains a class that defines an object"""

class Student:

    def __init)_(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict rep of a Student instance"""
        if attrs is not None:
            check_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    check_dict[key] = getattr(self, key)
            return check_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attrs of the student class"""
        for key in json:
            self.__dict__[key] = json[key]
