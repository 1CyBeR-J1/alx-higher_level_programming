#!/usr/bin/python3
"""Module that contains function that creates an obj"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object
    from a “JSON file”:
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
