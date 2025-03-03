### 0-safe_print_list.py
- **Function**: `safe_print_list(my_list=[], x=0)`
- **Description**: Prints `x` elements of a list safely.
- **Returns**: The real number of elements printed.
- **Notes**: Uses try/except to handle errors when accessing list elements.

### 1-safe_print_integer.py
- **Function**: `safe_print_integer(value)`
- **Description**: Prints an integer with the `"{:d}".format()` format.
- **Returns**: `True` if `value` is an integer and was printed correctly, otherwise `False`.
- **Notes**: Uses try/except to catch TypeError and ValueError.

### 2-safe_print_list_integers.py
- **Function**: `safe_print_list_integers(my_list=[], x=0)`
- **Description**: Prints the first `x` integers from a list.
- **Returns**: The number of integers printed.
- **Notes**: Skips non-integer values and handles index errors.

### 3-safe_print_division.py
- **Function**: `safe_print_division(a, b)`
- **Description**: Divides two integers and prints the result.
- **Returns**: The division result or `None` if division by zero.
- **Notes**: Uses try/except/finally to handle errors and ensure printing.

### 4-list_division.py
- **Function**: `list_division(my_list_1, my_list_2, list_length)`
- **Description**: Divides element by element between two lists.
- **Returns**: A new list with all divisions.
- **Notes**: Handles various exceptions: division by zero, wrong type, and out of range.

### 5-raise_exception.py
- **Function**: `raise_exception()`
- **Description**: Raises a type exception.
- **Notes**: Demonstrates how to explicitly raise an exception.

### 6-raise_exception_msg.py
- **Function**: `raise_exception_msg(message="")`
- **Description**: Raises a name exception with a custom message.
- **Notes**: Shows how to raise an exception with a specific error message.
