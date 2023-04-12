#!/usr/bin/python
"""
This is 1-write_file module
It contains function write_file
"""


def write_file(filename="", text=""):
    """
    writes a string to a txt file (UTF8)
    and returns the number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
