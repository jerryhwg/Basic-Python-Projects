# Python 3.7.2
# module 12:54
# given an integer array, output all the unique pairs that sum up to a specific value k
# usage: pair_sum(array,k)

def pair_sum(arr,k):

    if len(arr)<2:
        return # empty

    # sets for tracking
    seen = set()
    output = set()

    for num in arr:

        target = k - num
        
        if target not in seen:
            seen.add(num) 
            # when num = 1, target 3 is not in seen(), so seen.add(1)
            # when num = 3, target 1, and 1 is seen() that is else case, so output.add(1, 3)

        else: # if target in seen:
            output.add( ((min(num,target)), max(num,target)) ) # a pair of num, target

    # return len(output)
    print(output)
    # {(1, 3), (2, 2)}
    print ('\n'.join(map(str,list(output))))
    # (1, 3)
    # (2, 2)


"""
map: allows you to map a function (e.g. square, slicer) 
to an iterable object (every item in such as a list, tuple)
ex.
numbers = (1,2,3,4)
result = map(addition,numbers)

result
{2,4,6,8}

list(map(square,my_nums))

"""

"""
Test:
pair_sum([1,3,2,2],4)

Output:
(1, 3)
(2, 2)
"""