#! /bin/python

def main():
    n = int(raw_input())
    keys = []
    values = []
    for _ in xrange(n):
        line = raw_input().split()
        keys.append(int(line[0]))
        values.append(line[1])

    print ' '.join(map(str,count_sort(keys, values)))

def count_sort(keys, values):
    hi = 0
    for num in keys:
        if num > hi:
            hi = num
    sorted_keys = [[] for _ in xrange(hi + 1)]

    for i, v in enumerate(keys):
        if i >= len(keys) / 2:
            sorted_keys[v].append(values[i])
        else:
            sorted_keys[v].append('-')

    expanded = []
    for i in sorted_keys:
        for j in i:
            expanded += [j]

    return expanded

if __name__ == "__main__":
    main()
