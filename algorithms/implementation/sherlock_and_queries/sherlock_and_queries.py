#! /bin/python

import threading
import time
from math import pow

def main():
    N, M = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    B  = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())

    threads = []
    for i in xrange(0, M):
        thread = DividesThread(A, B[i], C[i])
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join(1)

    mod = int(pow(10, 9) + 7)
    print " ".join(map(lambda num: str(num % mod), A))

# ref: http://stackoverflow.com/a/24066054/2548291
def timed_join_all(threads, timeout):
    start = cur_time = time.time()
    while cur_time < (start + timeout):
        for thread in threads:
            if not thread.is_alive():
                thread.join()
        time.sleep(1)
        cur_time = time.time()

class DividesThread(threading.Thread):
    def __init__(self, A, b, c):
        threading.Thread.__init__(self)
        self.A = A
        self.b = b
        self.c = c

    def run(self):
        for j in xrange(0, len(self.A)):
            if divides(j+1, self.b):
                self.A[j] *= self.c

def divides(dividend, divisor):
    tmp = divides.cache
    if dividend not in tmp:
        tmp[dividend] = dict()

    tmp = tmp[dividend]
    if divisor not in tmp:
        tmp[divisor] = (dividend % divisor == 0)

    return divides.cache[dividend][divisor]
divides.cache = dict()

if __name__ == "__main__":
    main()
