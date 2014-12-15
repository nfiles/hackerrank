#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    insertion_sort(arr)

def insertion_sort(arr):
    for i in xrange(1, len(arr)):
        sort_iter(arr, i)
        print ' '.join(str(i) for i in arr)

def sort_iter(arr, end):
    unsorted = arr[end]
    for j in xrange(end + 1):
        if arr[j] > unsorted:
            del arr[end]
            arr.insert(j, unsorted)
            break

if __name__ == "__main__":
    main()
