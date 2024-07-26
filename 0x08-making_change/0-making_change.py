#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    number_coins = 0
    for coin in sorted(coins, reverse=True):
        while (total > 0):
            total = total - coin
            if total < 0:
                total = total + coin
                break
            number_coins += 1
    return number_coins
