import json

#!/usr/bin/python3
"""
Module that contains a function that returns JSON representation of an object
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
        my_obj: object to convert to JSON string
    Returns:
        JSON representation of object
    """
    return json.dumps(my_obj)
