#! /bin/python

import fileinput

def main():
    stdin = fileinput.input();

    # first line is number of test cases. Don't need it
    T = stdin.readline()

    for line in stdin:
        num = int(line)
        if num in fib(100):
            print "IsFibo"
        else:
            print "IsNotFibo"

# enumerable set of fibonacci numbers
def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    main()
