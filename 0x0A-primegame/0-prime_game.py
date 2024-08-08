#!/usr/bin/python3
"""Prime Game"""
from math import sqrt


def is_prime(x):
    if not x or x == 1:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def round_winner(n):
    """
    n: an integer representing the number of integers
    Determine the winner of the round using the Sieve of Eratosthenes
    """
    ints = list(range(2, n + 1))
    if not ints:
        return 'Ben'

    for i in range(n - 1):
        if not ints[i]:
            continue

        if not is_prime(ints[i]):
            ints[i] = 0
        else:
            for j in range(i, n - 1, ints[i]):
                if i == j:
                    continue
                ints[j] = 0

    # Remove duplicates 0s
    l = set(ints)

    # Remove 0
    l.discard(0)
    num_prime_numbers = len(l)

    # Since Maria starts first,
    # if the number of prime numbers is odd, Maria wins
    if num_prime_numbers % 2:
        return 'Maria'
    else:
        return 'Ben'


def isWinner(x, nums):
    """
    x: an integer representing the number of rounds
    nums: an array of n integers
    """
    maria_score = 0
    ben_score = 0
    for n in nums:
        if round_winner(n) == 'Maria':
            maria_score += 1
        else:
            ben_score += 1

    # Decision is made
    if ben_score > maria_score:
        return 'Ben'
    elif ben_score < maria_score:
        return 'Maria'
    else:
        return None
