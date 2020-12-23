#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/lilys-homework/problem

def lilysHomework1(arr):
    """
    Only test case that this passed was test case 0.
    """
    arrlength = len(arr)
    swaps = 0
    print(arr)
    for x in range(arrlength):
        xitem = arr[x]
        minitem = xitem
        minitempos = x
        for y in range(x, arrlength):
            yitem = arr[y]
            if yitem < minitem: 
                minitem = yitem
                minitempos = y
        if minitempos != x:
            arr[x], arr[minitempos] = arr[minitempos], arr[x]
            print(arr)
            swaps += 1

    return swaps

def lilysHomework(arr):
    swaps = 0
    arr_dict = {}
    arr_sorted = sorted(arr)
    for x in range(len(arr)):
        arr_dict[arr[x]] = x

    return arr_dict, arr_sorted

if __name__ == '__main__':
    #file = open('19_input00') #2 5 3 1 output: 2
    file = open('19_input11.txt') #3 4 2 5 1 output: 2
    #file = open('19_input07.txt') #3 2 1 output: 0

    n = int(file.readline())

    arr = list(map(int, file.readline().rstrip().split()))

    result = lilysHomework(arr)

    print(result)