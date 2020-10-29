#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/new-year-chaos/problem

"""
I had a LOT of help on this one; see minimumBribes1 and minimumBribes2 for those
that got me the rest of the way home.

I was able to pass all of the shorter test cases with my previous solution, but
I timed out on the test cases with ~100K items in the array. 
"""

def minimumBribes(q):
    counter = 0
    q = [x-1 for x in q] # make the math easier when comparing person to their position
    #tester = [0,1,2,3,4]
    # If 3 people are in front of person A (up to 1 pos in front of their org
    # position) who were originally behind person A, then the min number of
    # bribes needed to put person A in their curr position is 3.
       
    for pos, person in enumerate(q):
        if (person - pos) > 2: 
            print('Too chaotic')
            return  # 3 or more moves are illegal
        
        maxBribePos = max(person-1,0)
        tracker = maxBribePos
        #if pos in tester: print("A pos: %s person: %s maxBribePos: %s tracker: %s q[tracker]: %s, counter: %s" % (pos, person, maxBribePos, tracker, q[tracker], counter))
        while tracker < pos:
            if q[tracker] > person:
                counter += 1
            tracker += 1
            #if pos in tester: print("B pos: %s person: %s maxBribePos: %s tracker: %s q[tracker]: %s, counter: %s" % (pos, person, maxBribePos, tracker, q[tracker], counter))
    print(counter)

def minimumBribes1(q):
    t2 = time.time()
    looptimes = []

    q = [x-1 for x in q] # make the math easier when comparing person to their position
    counter = 0
    expectedFirst = 1
    expectedSecond = 2
    expectedThird = 3
    
    for pos, person in enumerate(q):
        t0 = time.time()
        if (person - pos) > 2: 
            print('Too chaotic')
            return  # 3 or more moves are illegal
        
        # Time to count how many times someone has been bribed!
        # If 3 people are in front of person A (up to 1 pos in front of their org
        # position) who were originally behind person A, then the min number of
        # bribes needed to put person A in their curr position is 3.

        if person == expectedFirst:
            expectedFirst = expectedSecond
            expectedSecond = expectedThird            
            expectedThird += 1
        elif person == expectedSecond:
            counter += 1            
            expectedSecond = expectedThird            
            expectedThird += 1
        elif person == expectedThird:
            counter += 2
            expectedThird +=1
        
        t1 = time.time()
        looptimes.append(t1-t0)
    t3 = time.time()
    avglooptime = sum(y for y in looptimes) / len(q)
    print("avg loop time (for loop): ", avglooptime)
    print("total time: ", t3-t2)
    print(counter)

def minimumBribes2(q):
    counter = 0
    index = len(q) - 1
    while index >= 0:
        person = q[index]

        if person - (index + 1) > 2:
            print("Too chaotic")
            return

        maxBribePos = max(person - 2, 0)
        while index > maxBribePos:
            if q[maxBribePos] > person: 
                counter += 1
            maxBribePos += 1

        index -= 1
    print(counter)

if __name__ == '__main__':
    """

    POS 0  1  2  3  4  5  6  7 
    TST 0  1  4  2  6  7  5  3 # TODO TEST CASE FAILING: returning 6 when the answer is 7
    DIF 0  0  2 -1  2  2 -1 -4
    
    q[max(TST-1, 0):POS]
    
    TST = 0
    POS = 0
    q[0:0]
    [0]
    0 bribes
    """
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
