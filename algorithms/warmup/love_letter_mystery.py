#! /bin/python

import string

def main():
    T = int(raw_input())

    for _ in xrange(T):
        print make_palindrome(raw_input())

def make_palindrome(word):
    count = 0
    for i in xrange(len(word) / 2):
        a = word[i]
        b = word[-(i+1)]
        diff = ord(a) - ord(b)
        if diff < 0:
            diff = -diff
        count += diff

    return count

if __name__ == "__main__":
    main()
