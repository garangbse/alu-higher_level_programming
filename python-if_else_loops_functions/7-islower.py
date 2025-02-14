#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase
    Args:
        c: character to check
    Returns:
        True if c is lowercase, False otherwise
    """
    return ord('a') <= ord(c) <= ord('z')
