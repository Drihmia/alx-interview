#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.
    """

    if total <= 0:
        return 0

    if len(coins) == 0:
        return -1

    number_coins = 0
    for coin in sorted(coins, reverse=True):
        while (total > 0):
            total = total - coin
            if total < 0:
                total = total + coin
                break
            number_coins += 1

    if total != 0:
        return -1
    return number_coins
