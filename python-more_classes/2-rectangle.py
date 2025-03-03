#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Rectangle class with width and height attributes
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance
        
        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        
        Args:
            value (int): width value to set
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        
        Args:
            value (int): height value to set
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        
        Returns:
            int: area value (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        
        Returns:
            int: perimeter value (2 * (width + height))
            or 0 if either width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
