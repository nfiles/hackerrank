#! /bin/python

def main():
    N, M = (int(i) for i in raw_input().split())
    people = [raw_input() for _ in xrange(N)]

    topics, teams = maximum_team(people)

    print topics
    print teams

def maximum_team(people):
    max_topics = 0
    max_teams = 0

    for i, person1 in enumerate(people):
        for j, person2 in enumerate(people[i+1:]):
            topics = maximum_topics(person1, person2)

            if topics > max_topics:
                max_topics = topics
                max_teams = 1
            elif topics == max_topics:
                max_teams += 1
    
    return (max_topics, max_teams)

def maximum_topics(person1, person2):
    bin1 = int(person1, 2)
    bin2 = int(person2, 2)
    return bin(bin1 | bin2)[2:].count('1')

if __name__ == "__main__":
    main()
