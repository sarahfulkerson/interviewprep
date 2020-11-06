#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

def sherlockAndAnagrams(s):
    """
    Build the Counter by finding all possible substrings, sorting the substring,
    then adding it to the Counter and incrementing the count by 1. Remove any substring
    that doesn't appear at least twice because that substring cannot therefore
    have a matching anagram. Then decrement the values of the remaining items in the
    dictionary and use them as inputs to the formula n(n+1)/2, which gives you the
    total numbers of pairs that can be made with with that number of substrings.

    Formula n(n+1)/2 was found on Quora: 
    https://www.quora.com/How-many-substrings-can-be-formed-from-a-character-string-of-length-n
    """
    from collections import Counter
    length = len(s)
    str_dict = Counter()
    total_pairs = 0

    # Build the counter
    for x in range(1, length+1):    # Gives you a range starting from 1 and ending at the length of string 's'
        substring_len = length-x+1  # The length of the substring to use in this iteration (gets smaller over time): string length - iteration + 1
        for y in range(x):      # Gives you a range for how many substrings to take of string 's' (gets larger over time)
            temp = ''.join(sorted(s[y:y+substring_len]))    # For iteration y, take a slice of string 's' starting at index 'y' up to but not including
                                                            # index 'y+substring length', cast the slice to a list and sort using sorted(), then cast back 
                                                            # to a string using join() and add the sorted string to a blank string.
            str_dict[temp] += 1 # Add the sorted substring to the Counter and increment by 1
    
    for key, value in list(str_dict.items()):   # Take a list of the dictionaries items to iterate over
        if value == 1:  # Remove anything that didn't appear more than once in the substring (no matching pair) and continue in the loop
            str_dict.pop(key)
            continue
        n = value-1     # If there is at least 2 of the substrings, decrement the count by 1 to use in the following formula
        pairs = (n*(n+1))/2 # This is the same as doing n + n-1 + n-2 + n-3 + n-4 +...+ 1 to find all the possible pairs
        total_pairs += int(pairs)   # Add the total number of pairs for this substring to the total number of pairs

    return total_pairs  # Return the total number of paired substrings for string 's'

if __name__ == '__main__':
    """
    2
    ifailuhkqq      Counter({'afi': 2, 'i': 2, 'q': 2})
    kkkk            Counter({'k': 4, 'kk': 3, 'kkk': 2})

    ouput:
    3
    10

    For the first query, we have anagram pairs [i,i], [q,q], and [ifa,fai] 
    at positions [[0],[3]], [[8],[9]], and [[0,1,2],[1,2,3]] respectively.

    For the second query:
    There are 6 anagrams of the form [k,k] at positions [[0],[1]], [[0],[2]], [[0],[3]], [[1],[2]], [[1],[3]], and [[2],[3]].
    There are 3 anagrams of the form [kk,kk] at positions [[0,1],[1,2]], [[0,1],[2,3]], and [[1,2],[2,3]].
    There is 1 anagram of the form [kkk,kkk] at position [[0,1,2],[1,2,3]].
    """
    fptr = []
    q = 2
    l1 = ['ifailuhkqq', 'kkkkk']

    for q_itr in range(q):
        s = l1[q_itr]
        result = sherlockAndAnagrams(s)
        fptr.append(result)
    for x in fptr: print(x)