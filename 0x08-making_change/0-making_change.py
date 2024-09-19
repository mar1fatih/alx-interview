#!/usr/bin/python3
"""making change"""
import sys


def Change(coins, total, cache):
    """
    determine the fewest number of
    coins needed to meet a given amount total
    """
    if total < 0:
        return -1

    if total == 0:
        return 0

    if cache[total] != 0:
        return cache[total]

    _max = sys.maxsize
    _min = _max
    for coin in coins:
        change_result = Change(coins, total - coin, cache)
        if (change_result >= 0 and change_result < _min):
            _min = 1 + change_result

    cache[total] = -1 if (_min == _max) else _min

    return cache[total]


def makeChange(coins, total):
    """
    determine the fewest number of
    coins needed to meet a given amount total
    """
    if total < 1:
        return 0

    return Change(coins, total, [0] * (total + 1))
