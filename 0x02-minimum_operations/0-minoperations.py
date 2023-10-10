#!/usr/bin/python3
'''0. Minimum Operations
Calculates the fewest number of operations needed
to result in exactly n
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed
    to result in exactly n
    '''
    if n < 2:
        return 0
    steps = 0
    buffer = 0
    text = 1
    while (text < n):
        if (n % text == 0):
            # Copy All & Paste
            buffer = text
            text += buffer
            steps += 2
        else:
            # Only Paste
            text += buffer
            steps += 1
    return steps
