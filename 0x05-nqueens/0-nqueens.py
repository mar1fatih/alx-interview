#!/usr/bin/python3
""" 0. N queens """
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    r = 0
    c = 0
    qs = []
    queens = []
    block = False

    while r < n:
        back = False
        while c < n:
            ok = True
            for queen in queens:
                column = queen[1]
                if(column == c or column + (r - queen[0]) == c or
                        column - (r - queen[0]) == c):
                    ok = False
                    break
            if not ok:
                if c == n - 1:
                    back = True
                    break
                c += 1
                continue
            queens.append([r, c])
            if r == n - 1:
                qs.append(queens[:])
                for queen in queens:
                    if queen[1] < n - 1:
                        r = queen[0]
                        c = queen[1]
                for i in range(n - r):
                    queens.pop()
                if r == n - 1 and c == n - 1:
                    queens = []
                    block = True
                r -= 1
                c += 1
            else:
                c = 0
            break
        if block:
            break
        if back:
            r -= 1
            while r >= 0:
                c = queens[r][1] + 1
                del queens[r]
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    for index, value in enumerate(qs):
        if index == len(qs) - 1:
            print(value, end='')
        else:
            print(value)
    print('')
