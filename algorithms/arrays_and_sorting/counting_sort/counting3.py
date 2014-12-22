#! /bin/python

def main():
    n = int(raw_input())
    arr = [int(raw_input().split()[0]) for _ in xrange(n)]
    counts = count_sort(arr)
    print ' '.join(map(str, counts))

def count_sort(arr):
    counts = [0] * 100
    for num in arr:
        for j in xrange(num, 100):
            counts[j] += 1

    return counts

if __name__ == "__main__":
    main()
