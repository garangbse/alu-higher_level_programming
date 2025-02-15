#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Create new tuples with at least 2 elements, padding with 0 if necessary
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)    
    # Return a new tuple with the sum of first two elements
    return (a[0] + b[0], a[1] + b[1])
