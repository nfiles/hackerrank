#! /bin/python

from math import pow

def main():
    N, M = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    B  = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())

    for i in xrange(0, M):
        for j in xrange(0, N):
            if divides(j+1, B[i]):
                A[j] *= C[i]

    mod = int(pow(10, 9) + 7)
    print " ".join(map(lambda num: str(num % mod), A))

def static_var(name, value):
    def decorate(func):
        setattr(func, name, value)
        return func
    return decorate

@static_var("cache", dict())
def divides(dividend, divisor):
    tmp = divides.cache
    if dividend not in tmp:
        tmp[dividend] = dict()

    tmp = tmp[dividend]
    if divisor not in tmp:
        tmp[divisor] = (dividend % divisor == 0)

    return tmp[divisor]

if __name__ == "__main__":
    main()
