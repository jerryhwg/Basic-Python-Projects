#!/bin/python3
# 20190305

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    
    # calc the fractions of the elements positive
    
    pos_num = 0
    neg_num = 0
    zero_num = 0
    
    for num in arr:
        if num > 0:
            pos_num += 1 # += 1
        #frag_pos = pos_num/n
         
        elif num < 0:
            neg_num += 1
        #frag_neg = neg_num/n
       
        elif num == 0:
            zero_num += 1
        #frag_zero = zero_num/n
        
    
    print(format(pos_num/n, '.4f')) # key: 4f
    print(format(neg_num/n, '.4f'))
    print(format(zero_num/n, '.4f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
