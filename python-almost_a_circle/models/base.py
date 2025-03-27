#!/usr/bin/python3
"""Base module for the project"""


class Base:
    """Base class of all other classes in the project.
    
    Attributes:
        __nb_objects (int): Private class attribute for counting objects
        id (int): Public instance attribute for object identification
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize a new Base instance.
        
        Args:
            id (int, optional): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
