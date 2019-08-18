# Python 3.7.2
# module 12:56
# Given two integer arrays, find which first element is missing in the second array
# Usage: finder1(arr1,arr2)

def finder1(arr1,arr2):

    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2): # zip(arr1,arr2)
        if num1 != num2:
            return num1

    return arr1[-1]  
    # if no return num1, then run this final element in arr1 must be 
    # the one to return so use -1 index eg. 7


"""
zip: zip up matching pair of the tuples
ex. zip([1,2,3],[4,5,6])
[(1,4),(2,5),(3,6)]

"""

"""
Test:
finder1([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
5
"""