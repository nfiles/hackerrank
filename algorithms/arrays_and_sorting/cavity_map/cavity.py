#! /bin/python

def main():
    n = int(raw_input())
    depths = [raw_input() for _ in xrange(n)]
    print '\n'.join(mark_cavities(depths))

def mark_cavities(depths):
    marks = [depths[0]]

    for i in xrange(1, len(depths) - 1):
        row = depths[i][0]

        for j in xrange(1, len(depths) - 1):
            depth = int(depths[i][j])
            if int(depths[i + 1][j]) < depth and \
               int(depths[i - 1][j]) < depth and \
               int(depths[i][j + 1]) < depth and \
               int(depths[i][j - 1]) < depth:
                row += 'X'
            else:
                row += str(depth)

        row += depths[i][-1]
        marks.append(row)

    if len(depths) > 1:
        marks.append(depths[-1])

    return marks

if __name__ == "__main__":
    main()
