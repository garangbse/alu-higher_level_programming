#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix
    Args:
        matrix: 2D list of integers
    Returns:
        New matrix with all values squared
    """
    if not matrix:
        return []
    return [[x ** 2 for x in row] for row in matrix]
