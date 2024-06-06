#!/usr/bin/python3
""" This module contains method canUnlockAll(boxes)
that determines of a box can be opened"""


def canUnlockAll(boxes):

    """ The method to determine if all boxes
        can be opend using BFS algorithm"""

    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
