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
    i = 2

    while i <= n:
        while n % i == 0:
            clipboard = i
            n //= i
            operations += 1

        i += 1

    operations += n

    return operations
