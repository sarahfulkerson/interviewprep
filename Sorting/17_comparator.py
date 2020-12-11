#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return 'Player(%s,%s)' % (self.name, self.score)
    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score == other.score and self.name > other.name:
            return True
        else:
            return False
    def __le__(self, other):
        if self.score <= other.score:
            return True
        elif self.score == other.score and self.name >= other.name:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.score > other.score:
            return True
        elif self.score == other.score and self.name < other.name:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.score >= other.score:
            return True
        elif self.score == other.score and self.name <= other.name:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.score == other.score and self.name == other.name:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.score != other.score or self.name != other.name:
            return True
        else:
            return False
    def comparator(a, b):
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

if __name__ == '__main__':
    file = open('17_input00')
    n = int(file.readline())
    data = []
    for i in range(n):
        name, score = file.readline().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)
    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
    print(Player.comparator(data[2],data[3]), data[2], data[3])