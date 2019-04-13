#!/bin/python3
# 20190317

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    
    result = 0

    if m == 1:
        for i in range(n):
            if s[i] == d:
                result += 1

    else:
        if m <= n:
            for i in range(n-1):
                if sum(s[i:i+m]) == d: # key: consecutive sum, how many consecutive depends on m
                    result += 1

    return result
    

if __name__ == '__main__':

    n = int(input().strip()) # number of integers eg. 5

    s = list(map(int, input().rstrip().split())) # array of integers eg. 1 2 1 3 2

    dm = input().rstrip().split()

    d = int(dm[0]) # an integer, birth day eg. 3

    m = int(dm[1]) # an integer, birth month eg. 2

    result = birthday(s, d, m) # number of ways of 2 integers sum to 3

    print(str(result) + '\n')


'''
Test 1
5
1 2 1 3 2
3 2
Result: 2

Test 2
6
1 1 1 1 1 1
3 2
Result: 0

Test 3
1
4
4 1
Result: 1

Improved version:
return sum(1 for x in range(len(s)) if sum(s[x:x+m]) == d)
'''