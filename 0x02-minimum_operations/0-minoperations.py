#!/usr/bin/python3
'''
0. Minimum Operations
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed
    to result in exactly n
    '''
    if not isinstance(n, int):
        return 0
    steps = 0
    buffer = ""
    text = "H"
    while (len(text) < n):
        if (n % len(text) == 0):
            # Copy All & Paste
            buffer = text
            text += buffer
            steps += 2
        else:
            # Only Paste
            text += buffer
            steps += 1
    return steps
