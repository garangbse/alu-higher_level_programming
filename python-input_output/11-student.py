#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of Student.

        Args:
            attrs: List of strings of attributes to retrieve

        Returns:
            Dictionary representation of requested attributes
        """
        if attrs is None:
            return self.__dict__
        
        return {attr: getattr(self, attr) 
                for attr in attrs 
                if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json: Dictionary of attributes to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
