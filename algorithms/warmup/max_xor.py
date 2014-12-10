#! /bin/python

import math

def main():
    L = int(raw_input())
    R = int(raw_input())

    print max_xor(L, R)

def max_xor(L, R):
    _max = 0

    for l in xrange(L, R):
        for r in xrange(l + 1, R + 1):
            xor = l ^ r
            if xor > _max:
                _max = xor

    return _max

if __name__ == "__main__":
    main()
