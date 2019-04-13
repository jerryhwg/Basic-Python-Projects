#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    
    sorted_arr = sorted(arr) # key: for lower key first
    seen = {}
    
    for type in sorted_arr:
        if type in seen:
            seen[type] += 1 # key: build a dict
        else:
            seen[type] = 1
            
    print(seen)
    return max(seen, key=seen.get) # key: get a key with the max value
    #v = list(seen.values())
    #k = list(seen.keys())
    #return k[v.index(max(v))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()