#!/usr/bin/python3
"""Prime Game"""


def is_prime(x):
    """
    x: an integer
    Determine if x is a prime number
    """
    if x <= 1:
        return False
    if x <= 3:
        return True

    if x % 2 == 0 or x % 3 == 0:
        return False

    for i in range(5, int(x**0.5) + 1, 6):
        if x % i == 0:
            return False

    return True


def round_winner(n):
    """
    n: an integer representing the number of integers
    Determine the winner of the round using the Sieve of Eratosthenes
    """
    if not n or not isinstance(n, int) or n < 1:
        return None

    if n == 1:
        return 'Ben'

    ints = list(range(2, n + 1))

    for i in range(n - 1):
        if ints[i] != 0 and is_prime(ints[i]):
            for j in range(i + ints[i], n - 1, ints[i]):
                ints[j] = 0
        else:
            ints[i] = 0

    # Remove duplicates 0s
    l = set(ints)

    # Remove 0
    l.discard(0)
    num_prime_numbers = len(l)

    # Since Maria starts first,
    # if the number of prime numbers is odd, Maria wins
    if num_prime_numbers % 2 == 1:
        return 'Maria'
    else:
        return 'Ben'


def isWinner(x, nums):
    """
    x: an integer representing the number of rounds
    nums: an array of n integers
    """
    if not nums or x > len(nums) or x < 1:
        return None

    maria_score = 0
    ben_score = 0

    for n in range(x):
        winner = round_winner(nums[n])
        if winner == 'Maria':
            maria_score += 1
        elif winner == 'Ben':
            ben_score += 1

    # Decision is made
    if ben_score > maria_score:
        return 'Ben'
    elif ben_score < maria_score:
        return 'Maria'
    else:
        return None
