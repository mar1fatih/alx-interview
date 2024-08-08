#!/usr/bin/python3
"""interview preparation"""


def minOperations(n):
    """minimum operations"""
    if n <= 1 and type(n) is not int:
        return 0
    temp = n
    pr = 2
    list_sum = []
    while pr <= temp:
        if temp % pr == 0:
            temp = temp / pr
            if (isprime(pr)):
                list_sum.append(pr)
        else:
            pr += 1
    sum = 0
    for i in list_sum:
        sum += i
    return sum


def isprime(x):
    """check if it a prime"""
    j = 2
    while j < x:
        if x % j == 0:
            return False
        j += 1
    return True
