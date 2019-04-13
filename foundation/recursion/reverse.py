# Python 3.7.2
# Module 98
#
# Reverse a String
# reverse a string using recursion
# Do not slice or use iteration, there must be a recursive call
#
# reverse(s)

def reverse(s):
    
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion

    return reverse(s[1:]) + s[0]


"""

Test
reverse('hello world')

"""