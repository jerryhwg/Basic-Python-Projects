#!/bin/python3
# 20190308

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count = 0 # empty as global
    tallest = max(ar) # key: max(ar)
    for i in ar:
        if i == tallest # key: match i with tallest and O(n)
            count += 1 # count
    return count

if __name__ == '__main__':

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)