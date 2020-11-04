#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

def sherlockAndAnagrams(s):
    """
    Key to this one will be finding letter pairs in the string
    and then looking at all of the letters (if any) that exist 
    betwen those letter pairs.
    """
    return s

if __name__ == '__main__':
    """
    2
    ifailuhkqq
    kkkk
    """
    fptr = []
    q = 2
    l1 = ['ifailuhkqq', 'kkkk']

    for q_itr in range(q):
        s = l1[q_itr]
        result = sherlockAndAnagrams(s)
        fptr.append(result)
    for x in fptr: print(x)