#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class
    Args:
        obj: The object to check
        a_class: The class to check against
    Returns:
        True if obj inherits from a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
