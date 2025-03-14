import json

#!/usr/bin/python3
"""Module that contains a function to convert JSON string to Python object"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: JSON string to convert

    Returns:
        Python object represented by the JSON string
    """
    return json.loads(my_str)
