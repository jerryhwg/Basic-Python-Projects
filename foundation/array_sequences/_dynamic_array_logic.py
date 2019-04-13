# Dynamic memory usage jump for array in python

# to use get size of function that let us know the actual size in bytes that the computer's holding in memory
import sys 

# amount of elements in the array
n = 10 

# set an empty list called data
data = []

for i in range(n): # 0-9
    
    # number of elements
    a = len(data) # 0,1,2...9 after data.append(n)
    
    # actual size in bytes
    b = sys.getsizeof(data)
    
    # Python 3 format print
    print ('Length: {0:3d}, Size in bytes: {1:4d}'.format(a, b))
    # 3d => Length:   0
    # 1d => Length: 0
    
    # increase length by one
    data.append(n)