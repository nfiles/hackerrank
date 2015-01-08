#! /bin/python

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        A = map(int, raw_input().strip().split())
        if sherlock_array(A):
            print "YES"
        else:
            print "NO"

def sherlock_array(array):
    if len(array) == 0:
        return False
    elif len(array) == 1:
        return True

    index = 0
    left, right = 0, 0
    for i in xrange(1, len(array)):
        right += array[i]

    while left < right:
        left += array[index]
        index += 1
        right -= array[index]

    return left == right

if __name__ == "__main__":
    main()
