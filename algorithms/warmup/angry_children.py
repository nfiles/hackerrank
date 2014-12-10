#! /bin/python

from sys import maxint

def main():
    N = input()
    K = input()
    candies = [input() for _ in xrange(0,N)]
    candies.sort()

    print min_diff(candies, K)

def min_diff(array, k):
    min_diff = maxint
    for i in xrange(0, len(array) - k):
        diff = array[i+k-1] - array[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

if __name__ == "__main__":
    main()
