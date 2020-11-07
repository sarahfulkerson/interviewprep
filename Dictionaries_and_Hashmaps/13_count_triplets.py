#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/count-triplets-1/problem

def countTriplets1(arr, r):
    """This only passed test cases 0, 1, and 12."""
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

def countTriplets2(arr, r):
    """
    This one did better but it failed test cases 6, 10, and 11. I am now properly
    handling special case r = 1 and when there are no possible triplets, but the
    summation part of the function is still not correct.
    """
    from collections import Counter
    from math import factorial

    # If the ratio 'r' is 1 then this is a special case of combinations
    if r == 1:
        n = len(arr)
        r = 3
        return factorial(n)//(factorial(r)*factorial(n-r))

    arr_dict = Counter()
    ratio_range = []
    index = 0
    counter = 0
    triplets = 0
    
    # Build the counter
    for x in arr:
        arr_dict[x] += 1
    max_arr_dict = max(arr_dict)

    # With the 1 special case removed, there now cannot be triplets if there are not 3 items in the dict
    if len(arr_dict) < 3: return triplets
    
    # There is now the potential for triplets so build all possible values
    while index < max_arr_dict:
        index = r**counter
        ratio_range.append(index)
        counter += 1
    if ratio_range[-1] > max_arr_dict: ratio_range.pop(-1)

    for y in range(len(ratio_range)-2):
        firstkey = ratio_range[y]
        secondkey = ratio_range[y+1]
        thirdkey = ratio_range[y+2]
        
        # If there are no triplets then the loop will exit without incrementing triplets 
        if firstkey not in arr_dict or secondkey not in arr_dict or thirdkey not in arr_dict: 
            continue
        else:
            firstvalue = arr_dict[firstkey]
            secondvalue = arr_dict[secondkey]
            thirdvalue = arr_dict[thirdkey]
            
            summedvalue = (firstvalue + secondvalue + thirdvalue) - 3
            triplet_count = 2**summedvalue
            triplets += triplet_count

    return triplets

def countTriplets(arr, r):
    from collections import Counter
    from math import factorial
    
    # If the ratio 'r' is 1 then this is a special case of combinations
    if r == 1:
        n = len(arr)
        r2 = 3
        return factorial(n)//(factorial(r2)*factorial(n-r2))

    # Main variables for the rest of the function
    arr_dict = Counter()
    max_arr = max(arr)
    ratio_range = []
    triplets = 0

    # Build all possible values
    index = 0
    counter = 0
    while index < max_arr:
        index = r**counter
        ratio_range.append(index)
        counter += 1
    if ratio_range[-1] > max_arr: ratio_range.pop(-1)
    
    # Build the counter
    for x in arr:
        if x in ratio_range: arr_dict[x] += 1

    # With the 1 special case removed, there now cannot be triplets if there are not 3 items in the dict
    if len(arr_dict) < 3: return triplets

    for y in range(len(ratio_range)-2):
        firstkey = ratio_range[y]
        secondkey = ratio_range[y+1]
        thirdkey = ratio_range[y+2]
        
        # If there are no triplets then the loop will exit without incrementing triplets 
        if firstkey not in arr_dict or secondkey not in arr_dict or thirdkey not in arr_dict: 
            continue
        else:
            firstvalue = arr_dict[firstkey]
            secondvalue = arr_dict[secondkey]
            thirdvalue = arr_dict[thirdkey]
            
            triplet_count = (firstvalue) * (secondvalue) * (thirdvalue)
            triplets += triplet_count

    return triplets

if __name__ == '__main__':
    """
    3
    1 3 9 9 27 81
    output: 6

    5
    1 5 5 25 125
    output: 4

    1
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    output: 161700

    input06.txt output: 2 325 652 489
                        3 948 101 982
    """

    fptr = open('input06.txt')

    nr = fptr.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])
    #r = 3
    #line = "1 3 9 9 27 81"
    #r = 1
    #line = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"

    arr = list(map(int, fptr.readline().rstrip().split()))
    #arr = list(map(int, line.rstrip().split()))
    
    ans = countTriplets(arr, r)

    print(ans)