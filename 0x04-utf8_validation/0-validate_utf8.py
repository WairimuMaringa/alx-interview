#!/usr/bin/python3
"""
Method to determine if a given data set represents
a valid utf-8 encoding
"""


def validUTF8(data):
    """ validate utf8 in a dataset. """

    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7

        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

                if num_bytes == 0:
                    continue

                if num_byes == 1 or num_byes > 4:
                    return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0