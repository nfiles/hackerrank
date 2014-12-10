#! /bin/python

from math import sqrt
from math import ceil

def main():
    T = int(raw_input())
    for _ in xrange(T):
        A, B = [int(i) for i in raw_input().split()]
        print squares(A, B)

def squares(A, B):
    base = ceil(sqrt(A))
    total = 0
    while base * base <= B:
        total += 1
        base += 1

    return total

if __name__ == "__main__":
    main()
