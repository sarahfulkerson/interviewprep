#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps, path):
    previous = 0
    counter = 0
    res = 0

    for x in path.lower():
        previous = counter
        if x == 'u':
            counter += 1
        elif x == 'd':
            counter -= 1
        else:
            continue

        print(counter)
        if counter == 0 and previous < counter:
            res += 1
    
    return res

if __name__ == '__main__':
    steps = input("How many steps did they take?: ")
    path = input("What is the path?: ")
    print(countingValleys(steps, path))