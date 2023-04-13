#!/usr/bin/python3
"""Module that contains a function that appends a str"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text
    file (UTF8) and returns the number of characters
    added
    """
    with open(filename, "a", enoding="utf-8") as f:
    return f.write(text)
