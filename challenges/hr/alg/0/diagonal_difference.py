#!/bin/python3
# 20190304

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):

    # show matrix
    print(arr)

    # diag1_sum
    diag1_sum = 0
    for i in range(n):
        diag1_sum += arr[i][i]
    print(diag1_sum)
    
    # diag2_sum
    diag2_sum = 0
    for i in range(n):
        diag2_sum += arr[i][((n-1)-i)]
    print(diag2_sum)
    
    # diff = diag1_sum - diag2_sum
    return abs(diag1_sum - diag2_sum) # key: abs of difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()