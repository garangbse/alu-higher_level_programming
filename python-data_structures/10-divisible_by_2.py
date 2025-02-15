#!/usr/bin/env python3
def divisible_by_2(my_list=[]):
    # Create a new list of same length as original
    result = []    
    # Check each number in the list
    for num in my_list:
        # Append True if number is divisible by 2, False otherwise
        result.append(num % 2 == 0)        
    return result
