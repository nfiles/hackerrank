#! /bin/python

def main():
    T = int(raw_input())

    for _ in xrange(T):
        print alt_char(raw_input())

def alt_char(string):
    count = 0
    current = None
    for c in string:
        if current != c:
            current = c
        else:
            count += 1

    return count

if __name__ == "__main__":
    main()
