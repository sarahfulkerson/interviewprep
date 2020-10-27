#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    res = []

    for x in range(len(arr)-2):
        row_n = arr[x]
        row_n1 = arr[x+1]
        row_n2 = arr[x+2]
        for y in range(len(row_n)-2):
            temp = row_n[y] + row_n[y+1] + row_n[y+2] + row_n1[y+1] + row_n2[y] + row_n2[y+1] + row_n2[y+2]
            res.append(temp)
    
    res.sort(reverse=True)

    return res[0]

if __name__ == '__main__':
    arr = [ [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]
    print(hourglassSum(arr))