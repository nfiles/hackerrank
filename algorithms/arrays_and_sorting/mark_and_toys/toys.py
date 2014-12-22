#! /bin/python

def main():
    n, k = map(int, raw_input().strip().split())
    prices = map(int, raw_input().strip().split())
    print max_toys(prices, k)

def max_toys(prices, money):
    toys = 0
    total = 0
    for price in sorted(prices):
        if total + price > money:
            break
        total += price
        toys += 1

    return toys

if __name__ == "__main__":
    main()
