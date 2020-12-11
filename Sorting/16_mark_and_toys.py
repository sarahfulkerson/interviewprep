#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/mark-and-toys/problem

def maximumToys(prices, k):
    total = 0
    count = 0
    
    prices.sort()
    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break
    return count

if __name__ == '__main__':
    k = int(input())

    prices = list(map(int, input().rstrip().split()))

    print(maximumToys(prices, k))