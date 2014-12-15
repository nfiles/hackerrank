#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    partition(arr)
    print ' '.join(map(str, arr))

def partition(arr):
    pivot = arr[0]
    pivot_pos = 0
    for i in xrange(1, len(arr)):
        value = arr[i]
        if arr[i] < pivot:
            for j in xrange(i, pivot_pos, -1):
                arr[j] = arr[j-1]
            arr[pivot_pos] = value
            pivot_pos += 1

    return arr

if __name__ == "__main__":
    main()
