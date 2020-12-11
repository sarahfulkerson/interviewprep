#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/frequency-queries/problem

def freqQueryX(queries):
    from collections import Counter
    freq = Counter()
    count = Counter()
    arr = []

    for q in queries:
        operation = q[0]
        item = q[1]
        freqItem = freq[item]

        if operation == 1:
            count[freqItem] -= 1
            freq[item] += 1
            count[freqItem] += 1
        elif operation == 2:
            if freqItem > 0:
                count[freqItem] -= 1
                freq[item] -= 1
                count[freqItem] += 1
        else:
            if count[item] > 0:
                arr.append(1)
            else:
                arr.append(0)

    return freq, count

def freqQuery(queries):
    from collections import Counter
    res = []
    freq = Counter()

    for operation, item in queries:
        if operation == 1:
            freq[item] += 1
            continue
        elif operation == 2:
            if freq.get(item, False) != False: freq[item] -= 1
            continue
        else:
            if item in freq.values(): 
                res.append(1)
            else:
                res.append(0)

    return res, freq

if __name__ == '__main__':
    output = open('14_output00')
    outputq = []
    
    for x in output:
        temp = x.rstrip()
        outputq.extend([int(temp)])
        
    input = open('14_input00')

    q = int(input.readline())

    queries = []

    for y in range(q):
        queries.append(list(map(int, input.readline().rstrip().split())))

    res = freqQueryX(queries)

    print(res)
    #print(res == outputq)