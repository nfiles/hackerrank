#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    sort = quicksort(arr)

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lower = []
    upper = []
    for i in xrange(1, len(arr)):
        value = arr[i]
        if value < pivot:
            lower.append(value)
        else:
            upper.append(value)

    sort = quicksort(lower) + [pivot] + quicksort(upper)
    print ' '.join(map(str, sort))
    return sort

if __name__ == "__main__":
    main()
