#! /bin/python

def main():
    T = int(raw_input())
    for _ in xrange(T):
        n, a, b = [int(raw_input()) for _ in range(3)]
        print find_final_values(n, a, b)

def find_final_values(n, a, b):
    _a = min(a, b)
    _b = max(a, b)

    value = _a * (n - 1)
    
    if _a == _b:
        return value
    else:
        values = ""
        for i in xrange(n):
            values += str(value) + " "
            value = value - _a + _b

        return values[:-1]

if __name__ == "__main__":
    main()
