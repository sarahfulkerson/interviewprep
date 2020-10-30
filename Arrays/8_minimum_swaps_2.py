#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""
Lesson learned on this one: while you CAN do this by scanning the rest of the list looking
for the correct item for your current position, it is more efficient to just put the item
at your current position in its correct place! In this way, you guarantee that you are not
wasting a single iteration of your inner loop.
"""
def minimumSwaps(arr):
    arr = [x-1 for x in arr]
    swaps = 0

    for pos, item in enumerate(arr):
        if pos == item: continue
        
        while pos != arr[pos]:
            item = arr[pos]
            arr[pos], arr[item] = arr[item], arr[pos]
            swaps += 1
               
    return swaps

if __name__ == '__main__':
    arr = [4,5,1,2,3]
    #      3 4 0 1 2
    print(minimumSwaps(arr))