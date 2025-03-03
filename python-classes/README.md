# Python Classes

This repository contains Python scripts that demonstrate Object-Oriented Programming concepts.

## Files and Descriptions

- `0-square.py`: Defines an empty class Square that represents a square
- `1-square.py`: Defines a Square class with a private instance attribute for size
- `2-square.py`: Enhances the Square class with size validation
- `3-square.py`: Adds a method to calculate the area of the square
- `4-square.py`: Implements getter and setter methods for the size attribute
- `5-square.py`: Adds a method to print the square using # characters
- `6-square.py`: Extends Square with position attributes for printing with offsets

## Usage

Each script can be executed independently to demonstrate specific OOP concepts:

```python
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square = Square(3)
print("Area:", my_square.area())
```
