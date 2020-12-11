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

def countTriplets4(arr, r):
    """
    This one fails test case 3, 6, 10, and 11.
    Wrong answer: 6
    Timeout: 3, 10, 11
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
    for x in range(len(arr)-1, -1, -1):
        if arr[x] not in ratio_range: 
            arr.pop(x)
            continue
        if arr[x] in arr_dict:
            arr_dict[arr[x]] = [x] + arr_dict[arr[x]]
        else:
            arr_dict[arr[x]] = [x]
    if len(arr) < 3: return triplets # return 0 if there are not enough items left in arr to make a triplet

    # Iterate backwards through arr starting at index arr[-2]
    for n in range(len(arr)-2, -1, -1):
        item = arr[n]
        item_before = item // r if item // r in ratio_range else 0  # Set to 0 if the next value in the progression does not appear in the input
        item_after = item * r if item * r in ratio_range else 0     # Set to 0 if the previous value in the progression does not appear in the input
        if not item_before or not item_after: continue                  # Continue in the loop if triplets are not possible with 'item' as 'j'
        
        counter_before = sum(1 for x in arr_dict[item_before] if x < n)
        counter_after = sum(1 for x in arr_dict[item_after] if x > n)
        triplets += counter_before * counter_after
    return triplets

def countTripletsX(arr,r):
    count = 0
    dictItem = {}
    dictPairs = {}

    for i in reversed(arr):
        ir = i*r
        #print('1. i: %s, ir: %s, count: %s, dictPairs: %s, dictItem: %s' % (i, ir, count, dictPairs, dictItem))
        if ir in dictPairs:
            count += dictPairs[ir]
            #print('2. i: %s, ir: %s, count: %s, dictPairs: %s, dictItem: %s' % (i, ir, count, dictPairs, dictItem))
        if ir in dictItem:
            dictPairs[i] = dictPairs.get(i, 0) + dictItem[ir]
            #print('3. i: %s, ir: %s, count: %s, dictPairs: %s, dictItem: %s' % (i, ir, count, dictPairs, dictItem))
        dictItem[i] = dictItem.get(i, 0) + 1
        #print('4. i: %s, ir: %s, count: %s, dictPairs: %s, dictItem: %s\n' % (i, ir, count, dictPairs, dictItem))

    return count

def countTriplets(arr, r):
    """
    ~~manndras answer~~
    So the algorithm is: 
    -- keep two dictionaries
        1.  A dictionary to store the number of times each single value that is repeated in the array.
        2.  A dictionary to store any pair of values that are i and (i * r) (using i as the key).
    -- Walk the array backwards
        1.  If the pair dictionary has a value for r times the one you're checking, then you add the
            number of pairs to the overall count.
        2.  Otherwise, add a new item to the pair dictionary if there's a value r times the one you're
            checking in the single value dictionary.
        3.  Otherwise, just add the value to the single value dictionary. 
    """
    from collections import Counter
    triplets = 0
    item_dict = Counter()
    pairs_dict = Counter()

    for item in reversed(arr):
        item_r = item*r
        
        if item_r in pairs_dict: triplets += pairs_dict[item_r]
        if item_r in item_dict: pairs_dict[item] += item_dict[item_r]
        item_dict[item] += 1

    return triplets

def countTripletsB(arr, r):
    """
    ~~nikhilgoyal104a1 answer~~
    """
    from collections import Counter
    triplets = 0
    leftDict = Counter()
    rightDict = Counter()

    for x in arr:
        rightDict[x] += 1
    
    for item in arr:
        rightDict[item] -= 1
        leftDict[item] += 1
        rightCt = rightDict.get(item*r, 0)
        leftCt = leftDict.get(item/r, 0)
        triplets += rightCt * leftCt

    return triplets
if __name__ == '__main__':
    """
    6 2
    3 6 3 6 12 18
    output: 3
    
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

    fptr = open('13_input11.txt')

    nr = fptr.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])
    #r = 3
    #line = "1 3 9 9 27 81"
    #r = 1
    #line = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"

    arr = list(map(int, fptr.readline().rstrip().split()))
    #arr = list(map(int, line.rstrip().split()))
    
    ans = countTripletsB(arr, r)

    print(ans)
    print(1667018988625)