import json

#!/usr/bin/python3
"""Module for loading JSON file to object"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    Args:
        filename: name of the JSON file
    Returns:
        The Python object created from JSON file
    """
    with open(filename, 'r') as file:
        return json.load(file)
