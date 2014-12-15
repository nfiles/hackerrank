#! /bin/python

def main():
    V = int(raw_input())
    N = int(raw_input())
    arr = [int(i) for i in raw_input().split()]
    print search(arr, V)

def search(arr, value):
    hi = len(arr)
    lo = 0
    while hi != lo:
        mid = (hi + lo) / 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            hi = mid
        elif arr[mid] < value:
            lo = mid
    
    return -1

if __name__ == "__main__":
    main()
