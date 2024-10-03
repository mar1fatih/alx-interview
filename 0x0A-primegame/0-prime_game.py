#!/usr/bin/python3
"""Prime Number"""

def isWinner(x, nums):
    """counting who won the most rounds"""
    ben = 0
    maria = 0
    prime_nums = []
    
    p = 2

    for num in nums:
        stats = [True for i in range(num + 1)]
        while (p * p <= num):
            if stats[p] == True:
                for i in range(p * p, num + 1, p):
                    stats[i] = False
            p += 1
    
        for j in range(2, num + 1):
            if stats[j]:
                prime_nums.append(j)
        if len(prime_nums) % 2 != 0 and len(prime_nums) != 1:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return 'Maria'
    else:
        return 'Ben'
