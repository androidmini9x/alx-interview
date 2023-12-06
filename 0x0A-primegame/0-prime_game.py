#!/usr/bin/python3
"""
This module contains the function `isWinner`
which determines the winner of the game.
"""


def is_prime(num):
    """
    Checks if a number is prime.
    Returns True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner of the game based on
    the number of rounds and the values of `nums`.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the
        values of `n` for each round.

    Returns:
        str or None: The name of the player with the
        most wins (either "Maria" or "Ben"),
        or None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        primes = []
        for j in range(2, nums[i] + 1):
            if is_prime(j):
                primes.append(j)

        m_turn = len(primes) % 2 == 0
        b_turn = not m_turn

        while primes:
            if m_turn:
                primes.pop()
            else:
                primes.pop(0)
            m_turn = not m_turn
            b_turn = not b_turn

        if m_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
