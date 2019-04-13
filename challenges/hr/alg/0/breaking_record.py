#!/bin/python3
# 20190313-2

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best_time = 0
    worst_time = 0
    best_scores = scores[0]
    worst_scores = scores[0]
        
    for i in range(n):
        if scores[i] > best_scores:
            best_scores = scores[i]
            best_time += 1
            
        elif scores[i] < worst_scores:
            worst_scores = scores[i]
            worst_time += 1
        
    return (best_time, worst_time)

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))