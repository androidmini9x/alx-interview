#!/usr/bin/python3
'''0. Change comes from within
'''


def makeChange(coins, total):
    '''Find lowest number of coins that meet a given amount'''
    if total <= 0:
        return 0

    coins = sorted(coins)
    counter = 0
    idx = len(coins) - 1

    while total > 0:
        if idx == -1:
            return (-1)

        if (total - coins[idx] >= 0):
            total -= coins[idx]
            counter += 1
        else:
            idx -= 1

    return counter
