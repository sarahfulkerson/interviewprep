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

def countTriplets3(arr, r):
    """
    This one isn't working either. Finally looked for a hint in the
    discussions and it looks like sequentiality is important. Test case
    to try is:

    5 2
    1 2 1 2 4
    """
    from collections import Counter
    from math import factorial
    arr_dict = Counter()
    n0 = arr[0]

    # If the ratio 'r' is 1 then this is a special case of combinations
    if r == 1:
        for x in arr:
            if x == n0: arr_dict[x] += 1
        n = arr_dict[n0]
        r2 = 3
        return factorial(n)//(factorial(r2)*factorial(n-r2)), arr_dict

    # Main variables for the rest of the function
    max_arr = max(arr)
    ratio_range = [n0]
    triplets = 0

    # Build all possible values
    index = n0  
    counter = 0
    while index < max_arr:
        index *= r
        ratio_range.append(index)
        counter += 1
    if ratio_range[-1] > max_arr: ratio_range.pop(-1)
    
    # Build the counter
    for x in arr:
        if x in ratio_range: arr_dict[x] += 1

    # With the 1 special case removed, there now cannot be triplets if there are not 3 items in the dict
    if len(arr_dict) < 3: return triplets, arr_dict, ratio_range

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

    return triplets, arr_dict

def countTriplets(arr, r):
    """
    Test case to try is:

    5 2
    1 2 1 2 4
    """
    from collections import Counter
    arr_dict = {}
    n0 = arr[0]
    max_arr = max(arr)
    ratio_range = {n0: 0}
    triplets = 0

    # Build all possible values
    index = n0  
    counter = 1
    while index < max_arr:
        index *= r
        ratio_range[index] = counter
        counter += 1
    if index > max_arr: ratio_range.pop(index)

    # Remove anything that isn't a possible value and build the dictionary
    for x in range(len(arr)):
        if arr[x] not in ratio_range: 
            arr.pop(x)
            continue
        if arr[x] in arr_dict:
            arr_dict[arr[x]] += [x]
        else:
            arr_dict[arr[x]] = [x]
    if len(arr) < 3: return triplets # return 0 if there are not enough items left in arr to make a triplet

    # Iterate backwards through arr starting at index arr[-2]
    for n in range(len(arr)-2, -1, -1):
        item = arr[n]
        item_before = item // r if item // r in ratio_range else 0  # Set to 0 if the next value in the progression does not appear in the input
        item_after = item * r if item * r in ratio_range else 0     # Set to 0 if the previous value in the progression does not appear in the input
        if not item_before or not item_after: continue                  # Continue in the loop if triplets are not possible with 'item' as 'j'

        counter_after = Counter(arr[n+1:])
        counter_before = Counter(arr[:n])
        triplets += counter_before[item_before] * counter_after[item_after]

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

    input06.txt output:          2 325 652 489
    input11.txt output:      1 667 018 988 625
                  mine:        171 410 983 415
    13_input03.txt output: 166 661 666 700 000    
    """

    fptr = open('custominput1.txt')

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