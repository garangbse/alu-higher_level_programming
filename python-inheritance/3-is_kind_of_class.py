#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or if obj is an instance
    of a class that inherited from a_class, otherwise False.
    
    Args:
        obj: The object to check
        a_class: The class to match against
    
    Returns:
        bool: True if obj is instance of a_class or its subclasses, False otherwise
    """
    return isinstance(obj, a_class)
