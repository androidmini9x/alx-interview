#!/usr/bin/python3
'''0. UTF-8 Validation
'''


def validUTF8(data):
    '''
    determines if a given data set represents a valid UTF-8 encoding
    '''
    # tracking the most signicate bits
    n = 0

    for bt in data:
        if n == 0:
            mask = 128
            while (mask & bt):
                n += 1
                mask >>= 1

            if n == 1 or n > 4:
                return False

            if n == 0:
                continue
        else:
            if not (bt & 128 and not (bt & 64)):
                return False

        n -= 1

    return n == 0
