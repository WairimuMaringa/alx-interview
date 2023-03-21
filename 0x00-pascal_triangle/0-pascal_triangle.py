#!/usr/bin/python3
"""
Function that returns a list of integers representing
the Pascals triangle
"""


def pascal_triangle(n):
    """ Create function that returns list. """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
