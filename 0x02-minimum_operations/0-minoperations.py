#!/usr/bin/python3
"""Minimum Operations"""
from sympy import factorint


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates the
    fewest number of operations needed to result in exactly n H characters
    in the file."""
    factorial = factorint(n)
    number_operations = 0
    for k, v in factorial.items():
        number_operations += k * v
    return number_operations
