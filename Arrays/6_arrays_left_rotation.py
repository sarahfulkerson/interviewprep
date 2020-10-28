#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def rotLeft(a, d):
    """
    a = an array of integers
    d = an integer; the number of rotations to perform on 'a'
    """
    res = a

    if len(res) // d != 0:
        res = res[d:] + res[:d]
    else:
        shift = d % len(res)
        res = res[shift:] + res[:shift]
    
    return res

if __name__ == '__main__':
    a = [10, 20, 30, 40, 50]
    d = 4
    a = [10, 20, 30]
    d = 8
    print(rotLeft(a,d))