# Python 3.7.2
# Given a string, determine if it is comprised of all unique characters, then True
# Usage: uni_char(s)

def uni_char1(s):
    return len(set(s)) == len(s)


"""
Test:
s = 'abcdea'
uni_char1(s)

Output:
False
"""