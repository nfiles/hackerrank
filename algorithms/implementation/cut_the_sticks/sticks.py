#! /bin/python

from sys import maxint

def main():
    N = int(raw_input())
    sticks = map(int, raw_input().strip().split())
    cut(sticks)

def cut(sticks):
    while len(sticks) > 0:
        print len(sticks)
        shortest = maxint
        for length in sticks:
            if length  < shortest:
                shortest = length

        for i in xrange(len(sticks) - 1, -1, -1):
            if sticks[i] > shortest:
                sticks[i] -= shortest
            else:
                del sticks[i]

if __name__ == "__main__":
    main()
