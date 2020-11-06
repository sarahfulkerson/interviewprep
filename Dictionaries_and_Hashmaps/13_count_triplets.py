#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/count-triplets-1/problem

def countTriplets(arr, r):
    from collections import Counter
    arr_dict = Counter()
    ratio_range = []
    triplets = 0

    # Build the counter
    for x in arr:
        arr_dict[x] += 1

    # Build a list for easier iteration
    for key, value in arr_dict.items():
        ratio_range.append(tuple([key,value]))
    ratio_range.sort()
    
    # TODO fix this so that it doesn't depend on a certain length of array
    for y in range(len(ratio_range)-2):
        firstvalue = ratio_range[y][1]
        secondvalue = ratio_range[y+1][1]
        thirdvalue = ratio_range[y+2][1]
        print(ratio_range, firstvalue, secondvalue,thirdvalue)

        summedvalue = (firstvalue + secondvalue + thirdvalue) - 3
        triplet_count = 2**summedvalue
        print(summedvalue, triplet_count)
        triplets += triplet_count

    return triplets, arr_dict, ratio_range

if __name__ == '__main__':
    """
    3
    1 3 9 9 27 81
    output: 6

    5
    1 5 5 25 125
    output: 4
    """    
    r = 3
    #line = "1 1 3 3 9 9 27 81"
    line = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"

    arr = list(map(int, line.rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)