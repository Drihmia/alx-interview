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
        # Mask to get last 8 bits to get the 8 least significant bits
        num &= 0xFF

        if remaining_bytes == 0:
            # if the 8th bit is 0, then the number is a single byte character
            if (num >> 7) == 0:
                continue

            # if the leftmost 3 bits are 110,
            # then the number is a 2 byte character
            if ((num >> 5) == 0b110):
                remaining_bytes = 1
            # if the leftmost 4 bits are 1110,
            # then the number is a 3 byte character
            elif (num >> 4) == 0b1110:
                remaining_bytes = 2
            # if the leftmost 5 bits are 11110,
            # then the number is a 4 byte character
            elif (num >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            # if the two most significant bits are not 10,
            # then the number is not a valid continuation byte
            if (num & 0b11000000) != 0b10000000:
                return False

            # decrement the number of remaining bytes if the number is a
            # valid continuation byte
            remaining_bytes -= 1

    # if the number of remaining bytes isn't 0, then the data set is incomplete
    return remaining_bytes == 0
