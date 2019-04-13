# Python 3.7.2
# Module 59
# Given a string of words, reverse all the *words*
# Usage: rev_word1('words')

def rev_word2(s):
    return " ".join(s.split()[::-1])

# s.split()
# ['space', 'before']

# ::-1: reverse the words order + join (put them together into a sentence)

"""
Test:
s = '   space before'
rev_word2(s)

Output:
'before space'
"""