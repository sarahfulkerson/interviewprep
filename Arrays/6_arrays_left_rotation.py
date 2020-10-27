#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def rotLeft(a, d):
    """
    a = an array of integers
    d = an integer; the number of rotations to perform on 'a'
    """
    #TODO: FIX OOM ERRORS
    res = a
    for x in range(d):
        res = res[1:] + [res[0]]
    
    return res

if __name__ == '__main__':
    a = [10, 20, 30]
    d = 7
    print(rotLeft(a,d))