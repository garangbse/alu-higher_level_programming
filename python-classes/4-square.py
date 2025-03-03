#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    A class that defines a square

    Attributes:
        __size (int): Size of the square
    """

    def __init__(self, size=0):
        """
        Initialize a new Square

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size

        Args:
            value (int): The size value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
