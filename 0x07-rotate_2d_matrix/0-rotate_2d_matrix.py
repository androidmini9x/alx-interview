#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
Rotate 2D Matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """Rotate 2d matrix 90 degree"""
    n = len(matrix)
    for r in range(n):
        for c in range(r, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for row in matrix:
        reverseRow(row)


def reverseRow(row):
    """Helper function to reverse array"""
    left = 0
    right = len(row) - 1
    while right > left:
        row[right], row[left] = row[left], row[right]
        right -= 1
        left += 1
