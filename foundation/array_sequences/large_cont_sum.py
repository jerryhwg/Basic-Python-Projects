# Python 3.7.2
# module 57
# given an array of integers, find the *largest continuous sum*
# usage: large_cont_sum(arr)
# > CHECK <

def large_cont_sum(arr):

    # Edge case check
    if len(arr)==0:
        return 0

    # first element
    max_sum = current_sum = arr[0]

    for num in arr[1:]: # not include the first element

        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum,max_sum) # keep going until -10
        #print(num)
        #print(current_sum)
        #print(max_sum)
        #print(' ')

    return max_sum # return the final max_sum


"""
Test:
large_cont_sum([1,2,-1,3,4,10,10,-10,-1])

Output: 
29
"""