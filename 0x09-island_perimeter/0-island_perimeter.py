#!/usr/bin/python3
"""grid island"""


def island_perimeter(grid):
    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i - 1 >= 0:
                    if grid[i - 1][j] == 0:
                        c += 1
                else:
                    c += 1
                if j + 1 < len(grid[0]):
                    if grid[i][j + 1] == 0:
                        c += 1
                else:
                    c += 1
                if j - 1 >= 0:
                    if grid[i][j - 1] == 0:
                        c += 1
                else:
                    c += 1
                if i + 1 < len(grid):
                    if grid[i + 1][j] == 0:
                        c += 1
                else:
                    c += 1
    return c
