#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list if they are integers.
    
    Args:
        my_list: The list to print elements from
        x: The number of elements to access
        
    Returns:
        The real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integer elements
            continue
        except IndexError:
            # If x is greater than the list length, let the exception propagate
            raise
    print()
    return count
