#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    d1 = {}
    counter = 0

    for x in ar:
        if x not in d1:
            d1[x] = 1
        else:
            d1[x] += 1

    for y in d1:
        counter += d1[y] // 2
    
    return counter

if __name__ == '__main__':
    n = input("How many socks are in the pile?: ")
    ar = input("What are the colors of each sock?: ").split()
    print(sockMerchant(n, ar))