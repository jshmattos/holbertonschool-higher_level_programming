#!/usr/bin/python3

"""
This is a module for Student class.
"""


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if attrs is not None:
            d = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    d[k] = v
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        if json["first_name"]:
            self.first_name = json["first_name"]
        if json["last_name"]:
            self.last_name = json["last_name"]
        if json["age"]:
            self.age = json["age"]
