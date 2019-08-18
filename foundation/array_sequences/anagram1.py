# Python 3.7.2
# given two strings, check to see if they are anagrams
# anagram: two stings can be written using the exactg same letters

def anagram1(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    return sorted(s1) == sorted(s2)


"""
Test:
s1 = 'clint eastwood'
s2 = 'old west action'
anagram1(s1,s2)

Output:
True
"""