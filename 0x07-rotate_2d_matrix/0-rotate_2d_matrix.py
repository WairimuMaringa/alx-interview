#!/usr/bin/python3
"""
Rotate a 2d matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ rotate a 2d matrix. """
    row = len(matrix)
    column = row - 1

    for i in range(0, int(row / 2)):
        for j in range(i, column - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[column - j][i]
            matrix[column - j][i] = matrix[column - i][column - j]
            matrix[column - i][column - j] = matrix[j][column - i]
            matrix[j][column - i] = temp
