#!/usr/bin/python3
class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student
        If attrs is a list of strings, only include those attributes
        Otherwise, return all attributes
        """
        if attrs is None:
            return self.__dict__
        
        new_dict = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict
