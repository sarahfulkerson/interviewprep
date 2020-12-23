#! /usr/bin/env python3
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

def activityNotifications1(expenditure, d):
    """
    This one was too slow.
    Test cases failed: 1, 2, 3, 4, 5
    """
    count = 0
    median = 0

    for x in range(d-1, len(expenditure)-1):
        substr = expenditure[x+1-d:x+1]
        spend = expenditure[x+1]
        print(substr, spend, d, expenditure[x+1-d])
        substr.sort()
        if d % 2 == 1:
            median = substr[d//2]
        else:
            median = (substr[(d//2)-1] + substr[d//2]) / 2
        if spend >= (median*2): count += 1

    return count

def activityNotifications(expenditure, d):
    """
    Only help I had here was someone telling me to use the bisect module
    to insert an item in my list without sorting.
    """
    from bisect import bisect
    count = 0
    median = 0
    substr = expenditure[:d]
    substr.sort()

    for x in range(d-1, len(expenditure)-1):
        spend = expenditure[x+1]
        if d % 2 == 1:
            median = substr[d//2]
        else:
            median = (substr[(d//2)-1] + substr[d//2]) / 2
        if spend >= (median*2): count += 1
        remove_me = bisect(substr, expenditure[x+1-d]) - 1
        substr.pop(remove_me)
        pos = bisect(substr,spend)
        substr.insert(pos,spend)

    return count

if __name__ == '__main__':
    #file = open('18_sample_input_0.txt')
    file = open('18_input01.txt') #expected output 633

    nd = file.readline().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, file.readline().rstrip().split()))

    #result = activityNotifications1(expenditure, d)
    result = activityNotifications(expenditure, d)

    print(result)