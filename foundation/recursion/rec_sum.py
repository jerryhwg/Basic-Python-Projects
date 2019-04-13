# Python 3.7.2
# a function which takes an integer and computes the cumulative sum of 0 to that integer
# if n = 4, 4+3+2+1+1 = 10

def rec_sum(n):

    # Base Case
    if n == 0:
        return 0

    # Recursive Case
    else:
        return n + rec_sum(n-1)