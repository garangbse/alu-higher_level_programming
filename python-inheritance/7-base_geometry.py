#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A base class for geometry"""

    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value
        Args:
            name: string
            value: value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
