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

    for i in range(2, n + 1):
        if n % i == 0:
            clipboard = i
            operations += n // i
            break

    while i < n:
        i += clipboard
        operations += 1

    return operations
