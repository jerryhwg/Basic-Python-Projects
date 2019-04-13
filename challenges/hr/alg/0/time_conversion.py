#!/bin/python3
# 20190309 *

import os
import sys


def timeConversion(s):
    time = list(s.split(':')) # split string with ':'
    
    if "PM" in s: # key: "str" in string
        if time[0] == "12": # key: arr[0]
            time[2] = time[2].replace('PM','') # key: array element replace syntax
        else:
            time[0] = int(time[0]) + 12
            time[2] = time[2].replace('PM','')
        return ':'.join(map(str,time))
    elif "AM" in s:
        if time[0] == "12":
            time[0] = "00"
            time[2] = time[2].replace('AM','')
        else:
            time[2] = time[2].replace('AM','')
        return ':'.join(map(str,time)) # key: join with ':' and map(str,time)

if __name__ == '__main__':
    
    s = input()
    result = timeConversion(s)
    print(result)