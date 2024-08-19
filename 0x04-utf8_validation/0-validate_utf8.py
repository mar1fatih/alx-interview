#!/usr/bin/python3
"""UTF8 Validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """fuction that validate a list of integers"""
    c: int = 0

    for ele in data:
        if not c:
            if ele >> 3 == 0b11110:
                c = 3
            elif ele >> 4 == 0b1110:
                c = 2
            elif ele >> 5 == 0b110:
                c = 1
            elif ele >> 6 == 0b10:
                return False
            elif ele >> 7:
                return False
        else:
            if ele >> 6 == 0b10:
                c -= 1
            else:
                return False
    return c == 0
