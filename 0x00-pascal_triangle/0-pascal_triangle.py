#!/usr/bin/python3
""" script for interviews preparing """


def pascal_triangle(n):
    """ return list of lists of pascal_triangle """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            c = 0
            if i - 1 >= 0 and j-1 >= 0:
                try:
                    c = pascal[i-1][j-1] + pascal[i-1][j]
                except:
                    c = 1
            else:
                c = 1
            row.append(c)

        pascal.append(row)
    return pascal
