#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    max_num = max(nums)
    primes = [0] * (max_num + 1)

    for i in range(2, max_num + 1):
        isPrime = True
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes[i] = 1

    for n in nums:
        primes_count = len(list(filter(lambda x: x == 1, primes[0: n + 1])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
