#!/usr/bin/python3
""" This module contains an imlementation of Pascal's
triangle in python"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n given the following:
    Returns an empty list if n <= 0 and assuming
    n will be always an integer"""

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
