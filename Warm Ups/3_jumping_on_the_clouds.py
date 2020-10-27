#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
    counter = 0
    n = 0
    n2 = 0
    res = 0

    while counter < len(c)-2:
        n = c[counter]
        n2 = c[counter+2]

        if n == n2:
            counter += 2
        else:
            counter += 1
        res += 1
    else:
        if counter == len(c)-2:
            res +=1
    
    return res

if __name__ == '__main__':
    #c = input("What is the path?: ").split()
    c = "0 0 1 0 0 1 0".split()
    print(jumpingOnClouds(c))