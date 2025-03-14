#!/usr/bin/python3
def read_file(filename=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name/path of the file to read. Defaults to empty string.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
