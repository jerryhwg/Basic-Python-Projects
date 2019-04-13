#!/bin/python3
# 20190306

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1): # loop range
        print(' '*(n-i) + '#'*i) # key: n-i and i

if __name__ == '__main__':
    n = int(input())

    staircase(n)