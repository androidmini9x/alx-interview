#!/usr/bin/python3
"""
The function that returns a list of lists of integers
representing the Pascals triangle of n:
"""


def pascal_triangle(n):
    """Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """
    tri_list = []

    # empty list if n <= 0
    if n <= 0:
        return tri_list
    
    for x in range(n):
        tri_list.append([1] * (x+1))
        for y in range(1, x):
            tri_list[x][y] = tri_list[x-1][y] + tri_list[x-1][y-1]

    return tri_list
