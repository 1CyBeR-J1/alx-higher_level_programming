#!/usr/bin/python3
"""A module that create a function that adds new attr"""


def attribute_add(obj, attr, value):
    """adds a new attribute to an object if it’s possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
