# Python 3.7.2
#
# Module 102
#
# Implement a Fibonnaci Sequences Dynamically (using Memoization)
#
# a function will accept a number n and return the nth number of the fibonacci sequence


# Instantiate cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n

    # Check Cache (memoization)
    if cache[n] != None:
        return cache[n]

    # Keep Setting Cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2) # same as recursion case

    return cache[n]


"""

Test
fib_rec(10)
result: 55

"""