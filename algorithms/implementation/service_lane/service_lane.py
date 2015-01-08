#! /bin/python

def main():
    N, T = map(int, raw_input().strip().split())
    width = map(int, raw_input().strip().split())
    lane = ServiceLane(width);
    for _ in xrange(T):
        i, j = map(int, raw_input().strip().split())
        print lane.distance(i, j)

class ServiceLane:
    def __init__(self, width):
        self.width = width

    def distance(self, entry, exit):
        widest = 3
        for i in xrange(entry, exit+1):
            cur = self.width[i]
            if cur < widest:
                widest = cur
                if widest <= 1:
                    break

        return widest

if __name__ == "__main__":
    main()
