#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    quicksort(arr)

def quicksort(arr):
    partition(arr, 0, len(arr) - 1)

def partition(arr, lo, hi):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    if hi - lo < 1:
        return

    pivot = arr[hi]
    index = lo
    for i in xrange(lo, hi):
        if arr[i] < pivot:
            swap(arr, i, index)
            index += 1

    swap(arr, index, hi)

    print ' '.join(map(str, arr))

    partition(arr, lo, index - 1)
    partition(arr, index + 1, hi)

if __name__ == "__main__":
    main()
