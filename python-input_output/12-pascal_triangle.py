#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with first row

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        prev_row = triangle[i - 1]
        
        # Calculate middle elements of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    return triangle
