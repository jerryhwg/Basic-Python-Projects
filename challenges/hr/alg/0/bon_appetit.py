#!/bin/python3
# 20190318-1
# direct

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    anna = int((sum(bill) - bill[k])/2) # anna's charged
    brian = int(sum(bill)/2) # brian's charged
    
    if anna == b: # if anna's charged == anna's contribution to the bill
        print("Bon Appetit")
    else: # if anna's overcharged, refund (brian-anna) to anna
        print(brian-anna)
        

if __name__ == '__main__':
    nk = input().rstrip().split() # eg. 4 1

    n = int(nk[0]) # number of dish items eg. 4

    k = int(nk[1]) # the item Anna doesn't eat eg. 1 = 2nd item

    bill = list(map(int, input().rstrip().split())) # all items price eg. [3, 10, 2, 9]

    b = int(input().strip()) # the amount that Anna contributed to the bill eg. 7

    bonAppetit(bill, k, b)


'''
Test 1
4 1
3 10 2 9
12
Output: 5

Test 2
4 1
3 10 2 9
7
Output: Bon Appetit
'''