#!/bin/python3
# 20190313-3

# contraints
# 2 <= n <= 100
# 1 <= k <= 100
# 1 <= ar[i] <= 100

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    
    result = 0
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i] + ar[j])%k == 0:
                result += 1
             
    return result
    
# How to improve the code from O(n^2) to O(n+2) >

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    
    print(str(result) + '\n')