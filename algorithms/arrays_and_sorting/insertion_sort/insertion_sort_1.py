#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().split()]

    unsorted = arr[-1]
    i = len(arr) - 2
    while i >= 0 and arr[i] > unsorted:
        arr[i + 1] = arr[i]
        print ' '.join(str(i) for i in arr)
        i -= 1

    arr[i + 1] = unsorted
    print ' '.join(str(i) for i in arr)

if __name__ == "__main__":
    main()
