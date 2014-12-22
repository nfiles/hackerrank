#! /bin/python

def main():
    n = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]

    median = find_median(arr)
    print median

def find_median(arr):
    return partition(arr[:], 0, len(arr) - 1)

def partition(arr, lo, hi):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    if hi - lo < 1:
        return arr[hi]

    pivot = arr[hi]
    index = lo
    for i in xrange(lo, hi):
        if arr[i] < pivot:
            swap(arr, i, index)
            index += 1

    swap(arr, index, hi)

    mid = len(arr) / 2
    if index > mid:
        return partition(arr, lo, index - 1)
    elif index < mid:
        return partition(arr, index + 1, hi)
    else:
        return arr[index]

if __name__ == "__main__":
    main()
