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

    for i in range(5, x**0,5 + 1):
        if x % i == 0:
            return False

    return True


def round_winner(n):
    """
    n: an integer representing the number of integers
    Determine the winner of the round using the Sieve of Eratosthenes
    """
    if not n:
        return None

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
    if len(nums) != x:
        return None

    if not x or not nums:
        return None

    if x == 1 and nums[0] == 0:
        return None

    maria_score = 0
    ben_score = 0

    for n in nums:
        if round_winner(n) == 'Maria':
            maria_score += 1
        elif round_winner(n) == 'Ben':
            ben_score += 1

    # Decision is made
    if ben_score > maria_score:
        return 'Ben'
    elif ben_score < maria_score:
        return 'Maria'
    else:
        return None
