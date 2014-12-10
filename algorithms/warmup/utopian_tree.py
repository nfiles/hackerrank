#! /bin/python

import fileinput

def main():
    stdin = fileinput.input()
    T = int(stdin.readline())

    for line in stdin:
        print utopian_tree(int(line))

def utopian_tree(n):
    # find the height of the tree after n cycles
    height = 1

    for cycle in xrange(n):
        if (cycle - 1) % 2 == 0:
            height += 1
        else:
            height *= 2

    return height

if __name__ == "__main__":
    main()
