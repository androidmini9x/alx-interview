#!/usr/bin/python3
"""Prime game module.
"""


def isPrime(num):
    """Return True if num is prime"""
    if num <= 1:
        return False
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    maria = 0
    ben = 0
    for i in range(x):
        idx = 0
        lst = [k for k in range(1, nums[i]+1)]
        for j in lst:
            if isPrime(j):
                idx += 1
        if idx % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben == maria:
        return None
    elif ben > maria:
        return 'Ben'
    else:
        return 'Maria'
