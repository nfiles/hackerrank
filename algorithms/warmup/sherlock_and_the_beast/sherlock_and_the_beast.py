#! /bin/python

from math import pow

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        print largest_decent_number(N)

def largest_decent_number(digits):
    largest = '1' * digits
    while largest:
        decent = decent_string(largest)
        if decent:
            return decent
        
        largest = decrement_bin(largest)

    decent = decent_string('0' * digits)
    return decent if decent else -1

def decrement_bin(string):
    last = string.rfind('1')
    if last < 0: # only able to decrement positive numbers
        return None

    decremented = string[:last]
    for i,c in enumerate(string[last:], last):
        decremented += ('1' if c == '0' else '0')

    return decremented

def decent_string(string):
    # valid number of each digit
    if string.count('1') % 3 != 0 or string.count('0') % 5 != 0:
        return None

    return string.replace('0', '3').replace('1', '5')

if __name__ == "__main__":
    main()
