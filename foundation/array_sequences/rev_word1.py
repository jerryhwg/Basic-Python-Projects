# Python 3.7.2
# Module 59
# Given a string of words, reverse all the *words*
# Usage: rev_word1('words')

def rev_word1(s):
    return " ".join(reversed(s.split())) # split() words per space in string

# s.split()
# ['space', 'before']
#
# reversed: reverse the words order 
# ['before', 'space']
# 
# join (put them together into a sentence)
# before space

"""
Test:
s = '   space before'
rev_word1(s)

Output:
'before space'
"""