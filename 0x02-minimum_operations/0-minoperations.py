#!/usr/bin/env python3
"""
Calculate the fewest number of operations
"""


def minOperations(n):
    """ Min operations. """
    outcome = 0
    i = 2

    if isinstance(n, int) and n < 2:
        return 0

    while i <= n + 1:
        if n % i == 0:
            outcome += i
            n //= i
            i = 2
        else:
            i += 1

    return outcome
