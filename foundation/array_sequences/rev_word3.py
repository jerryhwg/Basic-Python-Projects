# Python 3.7.2
# Module 59
# Given a string of words, reverse all the words
# Usage: rev_word2('words')

def rev_word3(s):
    words = [] # empty list
    length = len(s)
    spaces = [' '] # space

    i = 0

    while i < length:
        
        if s[i] not in spaces:
        
            word_start = i

            while i < length and s[i] not in spaces:

                i += 1 # keep increasing i until hit space

            words.append(s[word_start:i]) # words <= append from s.index(word_start) to s.the_final_index(i) until the space

        i += 1 # move to a next word

    # return words
    # ['space', 'before']

    return " ".join(reversed(words)) # reverse the order of each word and join them together with ' ' space


"""
Test:
s = '   space before'
rev_word3(s)

Output:
'before space'
"""