#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """
    determine the fewest number of
    coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    if not coins or coins is None:
        return -1

    change = 0
    sorted_coins = sorted(coins)[::-1]

    for coin in sorted_coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
