#!/usr/bin/python3
"""Minimum Operations"""
import subprocess
import sys


# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Try to import the package; if it fails, install it
try:
    from sympy import factorint
except ImportError:
    install('sympy')
    from sympy import factorint

from sympy import factorint  # noqa


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates the
    fewest number of operations needed to result in exactly n H characters
    in the file."""

    if not isinstance(n, int) or n <= 0:
        return 0

    factorial = factorint(n)

    number_operations = 0

    for k, v in factorial.items():
        number_operations += k * v

    return number_operations
