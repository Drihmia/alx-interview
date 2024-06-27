#!/usr/bin/python3
"""
This module contains a function that validates that a UTF-8 encoding is
correct.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    for num in data:
        remaining_nebes = 0
        if not remaining_nebes:
            if (num >> 5 == 0b110):
                remaining_nebes = 1
            elif (num >> 4 == 0b1110):
                remaining_nebes = 2
            elif (num >> 3 == 0b11110):
                remaining_nebes = 3
            elif num >> 7:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            remaining_nebes -= 1
    return True
