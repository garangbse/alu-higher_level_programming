#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list
    Args:
        my_list: list of integers (default empty list)
    Returns:
        Sum of all unique integers in the list
    """
    return sum(set(my_list))
