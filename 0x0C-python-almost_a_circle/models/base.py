#!/usr/bin/python3
"""This module contains a Base class"""
import json
import os
import csv


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class construction initializing the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string repn of list_dict"""
        if list_dictionaries is None or "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string reprensentation to a file"""
        new_list = [objs.to_dictionary() for objs in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON str representations"""
        if json_string is None or "":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribute already set"""
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(0, 0)
        elif cls.__name__ == "Square":
            dummy_inst = cls(0)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return "[]"
        else:
            with open(filename, "r") as f:
                dicts = Base.from_json_string(f.read())
                result = [cls.create(**d) for d in dicts]
                return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            csvwriter = csv.writer(f)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'r') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
