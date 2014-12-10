#! /bin/python

def main():
    T = int(raw_input())

    for _ in xrange(T):
        cuts = int(raw_input())
        print most_pieces_for(cuts)

def most_pieces_for(cuts):
    a = cuts / 2
    b = cuts - a
    return a * b

if __name__ == "__main__":
    main()
