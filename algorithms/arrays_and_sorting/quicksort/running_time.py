#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    main.swaps = 0
    qswaps = quicksort(arr[:])
    iswaps = isort(arr[:])
    print iswaps - qswaps

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr):
    def partition(arr, lo, hi):
        swaps = 0
        if hi - lo < 1:
            return 0

        pivot = arr[hi]
        index = lo
        for i in xrange(lo, hi):
            if arr[i] < pivot:
                swap(arr, i, index)
                swaps += 1
                index += 1

        swap(arr, index, hi)
        swaps += 1

        swaps += partition(arr, lo, index - 1)
        swaps += partition(arr, index + 1, hi)

        return swaps

    return partition(arr, 0, len(arr) - 1)

def isort(arr):
    swaps = 0

    for i in xrange(1, len(arr)):
        unsorted = arr[i]
        for j in xrange(i - 1, -1, -1):
            if arr[j] > unsorted:
                swap(arr, j, j + 1)
                swaps += 1
            else:
                break

    return swaps

if __name__ == "__main__":
    main()
