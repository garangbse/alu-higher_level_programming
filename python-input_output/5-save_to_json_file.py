import json

#!/usr/bin/python3
"""
Module containing function to write an object to a text file using JSON
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using JSON representation
    Args:
        my_obj: The object to write to the file
        filename: The name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
