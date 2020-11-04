#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/two-strings/problem
# formula from this Quora question was used: https://www.quora.com/How-many-substrings-can-be-formed-from-a-character-string-of-length-n

import os

def twoStrings1(s1, s2):
    """
    did not execute within the timeframe
    """
    length, shorter_str = (len(s1), s1) if len(s1) <= len(s2) else (len(s2), s2)
    longer_str = s1 if len(s1) > len(s2) else s2
    #reps = (length * (length + 1)) / 2
    
    for x in range(length, 0, -1):
        substring_len = length-x+1
        #print('x: ', x)
        #print('str length: ', substring_len)
        for y in range(0, x, 1):
            if shorter_str[y:y+substring_len] in longer_str: return 'YES'
            #print(y, shorter_str[y:y+substring_len], shorter_str[y:y+substring_len] in longer_str)

    return 'NO'

def twoStrings2(s1, s2):
    """
    reversed the order of the loops in twoStrings1 to try to put the
    larger strings first but it still did not execute within time for
    test case 3, 4, and 5.
    """
    length, shorter_str = (len(s1), s1) if len(s1) <= len(s2) else (len(s2), s2)
    longer_str = s1 if len(s1) > len(s2) else s2
    
    for x in range(1, length+1):
        substring_len = length-x+1
        #print('x: ', x)
        #print('str length: ', substring_len)
        for y in range(x):
            if shorter_str[y:y+substring_len] in longer_str: return 'YES'
            #print(y, shorter_str[y:y+substring_len])

    return 'NO'

def twoStrings(s1, s2):
    """
    I'm an idiot; s1 and s2 are STRINGS and only need to have a single 
    character in common!! this can be done with set intersection.
    """
    return 'YES' if set(s1) & set(s2) else 'NO'

if __name__ == '__main__':
    s1 = 'hel'
    s2 = 'world'
    
    print(twoStrings(s1, s2))

    """    fptr = open(os.environ['OUTPUT_PATH'], 'w')

        q = int(input())

        for q_itr in range(q):
            s1 = input()

            s2 = input()

            result = twoStrings(s1, s2)

            fptr.write(result + '\n')

        fptr.close()"""