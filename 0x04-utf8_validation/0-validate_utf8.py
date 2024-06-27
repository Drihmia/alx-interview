#!/usr/bin/python3
"""
This module contains a function that validates that a UTF-8 encoding is
correct.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """

    try:
        byte_data = bytes(data)
        byte_data.decode('utf-8')

        return True
    except (UnicodeDecodeError, ValueError):
        return False
