#! /bin/python

def main():
    N = int(raw_input())
    arr = [int(i) for i in raw_input().strip().split()]
    shifts = insertion_sort(arr)
    print shifts

def insertion_sort(l):
    shifts = 0
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
           shifts += 1
           
        l[j+1] = key

    return shifts

if __name__ == "__main__":
    main()
