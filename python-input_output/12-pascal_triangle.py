#!/usr/bin/python3
"""
Function to generate Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
    Returns empty list if n <= 0
    Args:
        n: number of rows to generate
    Returns:
        List of lists representing Pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
