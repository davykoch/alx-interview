#!/usr/bin/python3
""" Module contains implementation of method that calculates the minimum
number of operations to achieve a given number of characters using
only “Copy All” and “Paste” operations. """


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """

    if n <= 1:
        return n

    operations = 0
    clipboard = 0
    max_factor = n

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            clipboard = max(clipboard, i)
            max_factor = n // i

    operations += max_factor

    while max_factor > 1:
        operations += max_factor
        max_factor //= clipboard

    return operations
