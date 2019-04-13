#!/bin/python3
# 20190307

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    
    total = sum(arr) # sum()
    total_list = [] # key: empty as global
    
    for i in arr:
        total_i = total - i
        total_list.append(total_i) # key: build list with append

    total_max = max(total_list) # key: max(arr)
    total_min = min(total_list) # key: min(arr)
    print(total_min, total_max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)