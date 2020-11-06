#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
    rep = n // len(s)
    remain = n % len(s)
    a_in_str = 0
    a_in_remainder = 0
    res = 0
    
    for x in s:
        if x == 'a': a_in_str += 1

    res = rep * a_in_str

    for y in s[:remain]:
        if y == 'a': a_in_remainder += 1
    
    res += a_in_remainder
    
    return res

if __name__ == '__main__':
    s = 'aba'
    n = 10
    print(repeatedString(s, n))