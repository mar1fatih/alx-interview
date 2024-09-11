#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[list]):
    """ rotate 2D matrix """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
