#!/bin/python3
# 20190301

import os
import sys

#
# Complete the simpleArraySum function below.
# Sum of every elements in an array
#
def simpleArraySum(ar):
    sum = 0
    for num in ar:
        sum += num # key: sum += num
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
