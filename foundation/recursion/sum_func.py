# Python 3.7.2
# a function which returns the sum of all the individual digits in that integer
# ex. if n = 4321, 4+3+2+1

def sum_func(n):

    # Base Case
    if len(str(n)) == 1:
        return n

    else:
        # strip another digit
        return n%10 + sum_func(n//10) # 1 + 2 + 3 + 4