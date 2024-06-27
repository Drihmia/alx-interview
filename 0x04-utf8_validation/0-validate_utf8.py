#!/usr/bin/python3
"""
This module contains a function that validates that a UTF-8 encoding is
correct.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The data set to be checked.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    remaining_bytes = 0

    for num in data:
        if remaining_bytes == 0:
            if (num >> 7) == 0:
                continue

            if (num >> 5) == 0b110:
                remaining_bytes = 1
            elif (num >> 4) == 0b1110:
                remaining_bytes = 2
            elif (num >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
