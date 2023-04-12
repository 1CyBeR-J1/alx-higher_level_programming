#!/usr/bin/python3
"""Module that reads a text file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints to stdout"""
    with open(filename, encoding="utf-8") as Nwfile:
        for line in Nwfile:
            print(line, end="")
