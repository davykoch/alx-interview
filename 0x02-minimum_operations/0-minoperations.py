#!/usr/bin/python3
""" Module contains implementation of method that calculates the minimum
number of operations to achieve a given number of characters using
only “Copy All” and “Paste” operations. """


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed to achieve
    n 'H' characters or 0 if n is impossible.
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
