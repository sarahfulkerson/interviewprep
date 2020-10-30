#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/crush/problem

def arrayManipulation1(n, queries):
    """Too slow to pass big test cases"""
    arr = [0] * n

    for row in queries:
        ind1 = row[0] - 1
        ind2 = row[1]
        value = row[2]

        for pos in range(ind1, ind2):
            arr[pos] += value
        print(arr, ind1, ind2, value)
    arr.sort()
    return arr[-1]

def arrayManipulation2(n, queries):
    """
    This one was slower than the last attempt!
    """
    arr = [0] * n

    for pos in range(0, len(arr)):
        operation = 0
        for row in queries:
            value = row[2]
            if (row[0] - 1) <= pos < row[1]: operation += value
        arr[pos] = operation
        
    arr.sort()
    return arr[-1]

def arrayManipulation3(n, queries):
    """
    Faster than the last attempt, but still slower than the first attempt.
    """
    arr = []

    for pos in range(0, n):
        operation = 0
        for row in queries:
            value = row[2]
            if (row[0] - 1) <= pos < row[1]: operation += value
        arr += [operation]
        
    arr.sort()
    return arr[-1]

def arrayManipulation4(n, queries):
    """
    Good idea, doesn't work on large files! Keep getting
    'Wrong Answer' error.
    """
    arr = {}

    for row in queries:
        ind1 = row[0] - 1
        ind2 = row[1]
        value = row[2]

        for pos in range(ind1, ind2):
            if pos not in arr: 
                arr[pos] = value
            else:
                arr[pos] += value

    maxval = max(arr.values())
    return maxval

def arrayManipulation(n, queries):
    """
    Finally looked at the discussion for help. This code does what I couldn't
    quite figure out how to do on my own: only consider the pattern of the
    overlapping ranges in the queries array and somehow get the redundant addition
    removed from the code. This new code calculates the "slope" of the list 'arr'
    and gives the correct, scalable answer by: 
        1. adding 'value' to where the slope starts and subtracting 'value' from 
        where it ends
        2. then loops over 'arr' again and sums the last item in list 'res' with 
        the present value in 'arr' and adds the sum to the end of 'res'
        3. finally, sort 'res' and return the largest value
    """
    arr = [0] * n
    length = len(arr)
    res = [0]

    for row in queries:
        ind1 = row[0] - 1
        ind2 = row[1]
        value = row[2]

        arr[ind1] += value
        if ind2 < length: arr[ind2] -= value

    for item in arr:
        if item == 0: continue
        res += [res[-1] + item]
    
    res.sort()
    return res[-1]

if __name__ == '__main__':
    n = 5
    queries = [ [1, 5, 3], # 0 5 3
                [4, 8, 7], # 3 8 7
                [6, 9, 1]] # 5 9 1
    
    queries = [ [1, 2, 100], # 0 2 100
                [2, 5, 100], # 1 5 100
                [3, 4, 100]] # 2 4 100
    
    print(arrayManipulation(n, queries))
    
    """    import os

    fptr = open('output07.txt', 'w')

    file = open('C:\\Users\\sarah\\code\\interviewprep\\Arrays\\input07.txt')

    nm = file.readline().rstrip().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for x in range(m):
        queries.append(list(map(int, file.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()"""