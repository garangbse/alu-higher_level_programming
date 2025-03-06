#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the Square

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the Square"""
        return f"[Square] {self.__size}/{self.__size}"
