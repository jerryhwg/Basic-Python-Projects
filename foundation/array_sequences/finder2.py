# Python 3.7.2
# module 12:56
# Given two integer arrays, find which element is missing in the second array
# Usage: finder2(arr1,arr2)
# > CHECK <

import collections

def finder2(arr1,arr2):

    # using default dict to avoid key errors
    d = collections.defaultdict(int)

    # add a count for every instance in array 2 and create a list of d[num]
    for num in arr2:
        d[num]+=1
    # return d => {3: 1, 7: 1, 2: 1, 1: 1, 4: 1, 6: 1}

    # check if num not in dictionary
    for num in arr1:
        if d[num]==0:
            return num # when d[num] hit 0, show the num as it is a missing element in arr2
        # otherwise, iterate to subtract a count from d[num]
        else:
            d[num]-=1    


"""
defaultdict: from collections module
a dictionary in python where if the key isn't already in the dictionary
it will automatically add it for you instead of a missing key error

"""

"""
Test:
finder1([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
5
"""