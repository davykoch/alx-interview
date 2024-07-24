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

    # Initialize a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
