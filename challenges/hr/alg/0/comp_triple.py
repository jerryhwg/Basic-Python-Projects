#!/bin/python3
# 20190302

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a = (a[0],a[1],a[2])
    b = (b[0],b[1],b[2])

    x = 0 # key: 0 init counter
    y = 0

    for i in range(3): # key: range(n) = 0 ~ n-1
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            y += 1
    return x, y


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
