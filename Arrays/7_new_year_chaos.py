#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/new-year-chaos/problem

# Complete the minimumBribes function below.
def minimumBribes(q):
    counter = 0
    flag = False
    
    for ind in range(len(q)):
        item = q[ind]
        if (item - ind) > 3:
            print('Too chaotic')
            flag = True
            break
        else:
            if item - ind == 2: counter += 1
            elif item - ind == 3: counter += 2

    if flag == False: print(counter)

if __name__ == '__main__':
    """
    2
    5 1 2 3 7 8 6 4
    1 2 5 3 7 8 6 4 # TODO TEST CASE FAILING
    """
    
    t = int(input())

    for t_itr in range(t):

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)