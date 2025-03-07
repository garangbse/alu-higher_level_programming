#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """confirms if the object is an inherited instance of a class.

    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
