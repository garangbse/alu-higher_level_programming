#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns dictionary description of object for JSON serialization
    Args:
        obj: instance of a Class
    Returns:
        Dictionary representation with serializable attributes
    """
    return obj.__dict__
