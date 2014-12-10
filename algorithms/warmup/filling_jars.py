#! /bin/bash

def main():
    N, M = (int(i) for i in raw_input().split())
    operations = [raw_input() for _ in xrange(M)]

    average = jar_average(N, operations)

    print average

def jar_average(jar_count, operations):
    total = 0

    for operation in operations:
        left, right, amount = (int(i) for i in operation.split())
        total += (right - left + 1) * amount

    return int(float(total) / float(jar_count))

if __name__ == "__main__":
    main()
