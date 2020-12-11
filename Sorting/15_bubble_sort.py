#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    count = 0
    for x in range(len(a)):
        for y in range(len(a)-1):
            #Swap adjacent elements if they are in decreasing order
            if a[y] > a[y + 1]:
                a[y], a[y+1] = a[y+1], a[y]
                count += 1
    print('Array is sorted in %s swaps.' % count)
    print('First Element: %s' % a[0])
    print('Last Element: %s' % a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)