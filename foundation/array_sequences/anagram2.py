# Python 3.7.2
# given two strings, check to see if they are anagrams
# anagram: two stings can be written using the exactg same letters

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Edge Case Check
    if len(s1) != len(s2):
        return False
    
    # Main
    count = {} # initialize an empty bucket (dictionary)
    
    for letter in s1:
        if letter in count:
            count[letter] += 1 # +=
        else:
            count[letter] = 1

    print(count)
    # {'i': 3, 'l': 1, 'k': 2, 'e': 1, 'b': 1, 't': 1}
            
    for letter in s2:
        if letter in count:
            count[letter] -= 1 # -=
        else:
            count[letter] = 1
            
    print(count)

    for k in count:
        if count[k] != 0: # if any element(letter) count is not 0
            return False
        # count[k] eg. count[c]
        
    return True   


"""
Test:
s1 = 'clint eastwood'
s2 = 'old west action'
anagram2(s1,s2)

Output:
True
"""