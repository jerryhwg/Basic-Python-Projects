# Python 3.7.2
#
# Module 102
#
# Implement a Fibonnaci Sequences Recursively
#
# a function will accept a number n and return the nth number of the fibonacci sequence


def fib_rec(n):

    # Base Case
    if n == 0 or n == 1:
        return n

    # Recurive Case
    else:
        return fib_rec(n-1) + fib_rec(n-2) # ex. fib(10 = 55) = fib(9 = 34) + fib(8 = 21)
        # fibonnaci sequence is a great example of recursion


"""

Test
fib_rec(10)
result: 55

"""