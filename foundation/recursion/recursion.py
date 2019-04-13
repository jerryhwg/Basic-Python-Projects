# Python 3.7.2
# Recursion

def fact(n):

    # Base Case
    if n == 0:
        return 1

    else:
        return n * fact(n-1) # recursion


"""

Test
fact(5)
result: 120

"""