#! /bin/python

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N, C, M = [int(x) for x in raw_input().split()]
        print chocolates(N, C, M)

def chocolates(money, cost, bonus):
    total = (money / cost)
    wrappers = total

    while wrappers >= bonus:
        exchanged = wrappers / bonus
        wrappers = (wrappers % bonus) + exchanged
        total += exchanged

    return total

if __name__ == "__main__":
    main()
