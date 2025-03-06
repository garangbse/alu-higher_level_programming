#!/usr/bin/python3
"""Module containing MyList class"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
