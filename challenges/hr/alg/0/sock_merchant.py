#!/bin/python3
# 20190318-2
# discussion

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result = 0
    d = {} # using dictionary for multiple pairs is the key
    for i in range(n):
        if ar[i] in d:
            d.pop(ar[i]) # using pop to take out the checked sock pairs
            result += 1
        else:
            d[ar[i]] = 1
    return result

if __name__ == '__main__':

    n = int(input()) # number of socks eg. 9

    ar = list(map(int, input().rstrip().split())) # array for each color of scok eg. [10,20,20,10,10,30,50,10,20]

    result = sockMerchant(n, ar)

    print(result)


'''
9
10 20 20 10 10 30 50 10 20

Result:
3
'''