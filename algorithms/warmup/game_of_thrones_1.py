#! /bin/python

def main():
    string = raw_input()

    if find_palindrome(string):
        print "YES"
    else:
        print "NO"

def find_palindrome(word):
    odd = ""
    for c in word:
        if c in odd:
            odd = odd.translate(None, c)
        else:
            odd += c

    return len(odd) <= 1

if __name__ == "__main__":
    main()
