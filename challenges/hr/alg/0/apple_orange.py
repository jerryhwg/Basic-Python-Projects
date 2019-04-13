## !/bin/python3
# 20190311

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    fl_apple = []
    fl_orange = []
    ct_apple = []
    ct_orange = []
    
    for i in apples:
        fl = i + a
        fl_apple.append(fl)
    print("location of apples", fl_apple)
        
    for i in oranges:
        fl = i + b
        fl_orange.append(fl)
    print("location of orange", fl_orange)
        
    for i in fl_apple:
        if i in range(s,t+1): # range end doesn't include the value of end
            ct_apple.append(i)
    print("number of my apples", len(ct_apple))    
        
    for i in fl_orange:
        if i in range(s,t+1):
            ct_orange.append(i)
    print("number of my orange", len(ct_orange))
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
    
# s: starting point of the house
# t: ending location of the house
# a: location of the Apple tree
# b: location of the Orange tree
# m: number of apples
# n: number of oranges
# apples: int array, distances at which each apple falls from the tree
# oranges: int array, distances at which each orange falls from the tree
# ex. s = 7, t = 10, a = 4, b = 12
# apple falls at [2, 3, -4] => adding apple tree location = [2+4, 3+4, -4+4]
# orange falls at [3, -2, -4] => adding orange tree location = [3+12, -2+12, 12-4]
# fruits in range(7, 10): 1 apple(7), 2 orange (10, 8), so count 1 apple, 2 orange