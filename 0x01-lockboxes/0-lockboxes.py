#!/usr/bin/python3
"""
Finding the number of locked boxes
"""


def canUnlockAll(boxes):
    """ n number of locked boxes."""
    n = len(boxes)
    visibleboxes = set([0])
    notvisible = set(boxes[0]).difference(set([0]))
    while len(notvisible) > 0:
        boxidentity = notvisible.pop()
        if not boxidentity or boxidentity >= n or boxidentity < 0:
            continue
        if boxidentity not in visibleboxes:
            notvisible = notvisible.union(boxes[boxidentity])
            visibleboxes.add(boxidentity)
    return n == len(visibleboxes)
