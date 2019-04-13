# Python 3.7.2
# Given a string, determine if it is comprised of all unique characters, then True
# Usage: uni_char(s)

def uni_char2(s):

    chars = set() # init var and apply set() uniq function to it

    for letter in s:
        if letter in chars: # if a letter hits for the 2nd time, return False (because of redundant chars in s)
            return False
        else:
            chars.add(letter)
    return True # if not False, True

"""
My method

def uni_char(s):
    uni_s = set(s)
    uni_s = ''.join(list(sorted(uni_s)))
    s = ''.join(list(sorted(s)))
    return s == uni_s

"""

"""
Test:
s = 'abcdea'
uni_char2(s)

Output:
False
"""