#!/usr/bin/python3
''' 0. Prime Game
'''


def isWinner(x, nums):
    '''Return winner'''
    if x < 1 or x != len(nums):
        return None

    player = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        idx = -1
        lst = [k for k in range(1, nums[i]+1)]
        for j in lst:
            if isPrime(j):
                idx += 1
        if idx % 2 == 1:
            player['Ben'] += 1
        else:
            player['Maria'] += 1

    if player['Ben'] == player['Maria']:
        return None
    elif player['Ben'] > player['Maria']:
        return 'Ben'
    else:
        return 'Maria'


def isPrime(num):
    '''Return True if num is prime'''
    if num <= 1:
        return False
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    return True
