#!/usr/bin/python3
"""Module that contains a script"""
import json
import sys

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-laod_from_json_file")\
            .load_from_json_file

    filename = "add_item.json"

    try:
        in_file = load_from_json_file("filename")
    except FileNotFoundError:
        in_file = []
    in_file.extend(sys.argv[1:])
    save_to_json_file(in_file, "filename")
