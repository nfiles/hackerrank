#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    print ' '.join(map(str, count_sort(arr)))

def count_sort(arr):
    hi = 0
    for num in arr:
        if num > hi:
            hi = num

    counts = [0] * (hi + 1)

    for num in arr:
        counts[num] += 1

    expanded = []
    for i, v in enumerate(counts):
        if v > 0:
            expanded += [i] * v

    return expanded

if __name__ == "__main__":
    main()
