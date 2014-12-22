#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    counts = count(arr)
    print ' '.join(map(str,counts))

def count(arr):
    hi = 0
    for num in arr:
        if num > hi:
            hi = num

    counts = [0] * (hi + 1)

    for num in arr:
        counts[num] += 1

    return counts

if __name__ == "__main__":
    main()
