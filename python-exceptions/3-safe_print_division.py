#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Function that divides two integers and prints the result.
    Returns the value of the division, otherwise: None
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
