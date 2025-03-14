#!/usr/bin/python3
def read_file(filename=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name/path of the file to read. Defaults to empty string.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
        def __doc__():
            """
            This module contains functions for file handling operations.
            The read_file function reads and prints the contents of a text file.
            """
            return "File handling module"
        