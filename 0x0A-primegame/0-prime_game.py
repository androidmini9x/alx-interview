#!/usr/bin/python3
"""Prime game
"""


def isWinner(x, nums):
    """Return the winner
    """
    if x < 1 or not nums:
        return None
    maria = 0
    ben = 0
    primes = []

    max_num = max(nums)
    for i in range(2, max_num + 1):
        isPrime = True
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    for i in range(x):
        idx = 0
        lst = [k for k in range(1, nums[i]+1)]
        for j in lst:
            if j in primes:
                idx += 1

        ben += idx % 2 == 0
        maria += idx % 2 == 1

    if ben == maria:
        return None
    elif ben > maria:
        return 'Ben'
    else:
        return 'Maria'
