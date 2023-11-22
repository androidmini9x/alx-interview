#!/usr/bin/python3
'''0. Change comes from within
'''


def makeChange(coins, total):
    '''Find lowest number of coins that meet a given amount'''
    if total <= 0:
        return 0

    cache = [total + 1] * (total + 1)
    cache[0] = 0
    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0:
                cache[i] = min(cache[i], 1 + cache[i-c])
    result = cache[total] if cache[total] != (total+1) else -1
    return result
