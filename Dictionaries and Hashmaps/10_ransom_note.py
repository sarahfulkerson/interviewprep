#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

def checkMagazine(magazine, note):
    note_dict = {}
    magazine_dict = {}

    for n in note:
        if n not in note_dict: 
            note_dict[n] = 1
        else:
            note_dict[n] += 1

    for m in magazine:
        if m not in note_dict: continue
        
        if m not in magazine_dict: 
            magazine_dict[m] = 1
        else:
            magazine_dict[m] += 1
    
    for key, value in note_dict.items():
        if key not in magazine:
            print('No')
            return
        else:
            if value <= magazine_dict.get(key):
                continue
            else:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    """
    6 5

    two times three is not four

    two times two is four
    """
    #mn = input().split()
    #m = int(mn[0])
    #n = int(mn[1])
    #magazine = input().rstrip().split()
    #note = input().rstrip().split()

    m = 6
    n = 5
    magazine = "two times three is not four".rstrip().split()
    note = "two times two is four".rstrip().split()

    checkMagazine(magazine, note)