# Python Input/Output

This repository contains Python scripts demonstrating file I/O operations and JSON handling.

## Function Descriptions

### 0-read_file.py
* Function: `read_file(filename="")`
* Reads a text file (UTF8) and prints its contents to stdout
* Uses `with` statement to handle file operations

### 1-write_file.py
* Function: `write_file(filename="", text="")`
* Writes a string to a text file (UTF8)
* Returns the number of characters written
* Creates file if doesn't exist, overwrites if it does

### 2-append_write.py
* Function: `append_write(filename="", text="")`
* Appends a string to the end of a text file (UTF8)
* Returns the number of characters added
* Creates file if it doesn't exist

### 3-to_json_string.py
* Function: `to_json_string(my_obj)`
* Returns JSON string representation of an object
* Uses `json.dumps()` for serialization

### 4-from_json_string.py
* Function: `from_json_string(my_str)`
* Returns Python object from JSON string representation
* Uses `json.loads()` for deserialization

### 5-save_to_json_file.py
* Function: `save_to_json_file(my_obj, filename)`
* Writes an object to a text file using JSON representation
* Combines `json.dumps()` with file writing

### 6-load_from_json_file.py
* Function: `load_from_json_file(filename)`
* Creates an object from a JSON file
* Uses `json.load()` to read directly from file

### 7-add_item.py
* Script that adds all arguments to a Python list
* Saves them to a file named `add_item.json`
* Uses functions from previous tasks

### 8-class_to_json.py
* Function: `class_to_json(obj)`
* Returns dictionary description for JSON serialization of object
* Works with simple data structures

### 9-student.py
* Class: `Student`
* Contains `to_json()` method for serialization
* Handles basic student data

### 10-student.py
* Enhanced `Student` class
* `to_json()` method with optional attributes filter
* More selective serialization

### 11-student.py
* Further enhanced `Student` class
* Adds `reload_from_json()` method
* Allows object reconstruction from JSON

### 12-pascal_triangle.py
* Function: `pascal_triangle(n)`
* Returns list of lists representing Pascal's triangle
* Handles mathematical computation
