# Python 3.7.2
#
# Module 102
#
# Implement a Fibonnaci Sequences Iteratively
#
# a function will accept a number n and return the nth number of the fibonacci sequence


def fib_iter(n):
    
    a = 0
    b = 1

    for i in range(n):

        a,b = b,a+b # iterate, python way
        print('a',a)
        print('b',b)

    return a


"""

Test
fib_iter(10)
result: 55

"""