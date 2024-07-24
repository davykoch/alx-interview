#!/usr/bin/python3
"""Module for makeChange function."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount.

    Returns:
        int: Fewest number of coins needed to meet total.
             Returns 0 if total is 0 or less.
             Returns -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
