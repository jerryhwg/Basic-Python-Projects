# Python 3.7.2
# Module 62
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it
# to become 'A4B4C5D2E4'
# the function is also case sensitive
# Usage: compress(s)

def compress(s):

    r = ""
    l = len(s)

    if l == 0:
        return "" # return empty (edge case)

    if l == 1:
        return s+"1"
        # s = "A" then return A1

    cnt = 1
    i = 1

    while i < l:

        if s[i] == s[i-1]: # s[1] == s[0]
            cnt +=1 # 2,3,4 ...
        else:
            r = r + s[i-1] + str(cnt) # if no more repeated char: eg. A3
            cnt = 1 # cnt reset to 1 for the next char
        
        i += 1 # loop continues

    r = r + s[i-1] + str(cnt) # final: last element from if statement (eg. E4)
    # if s[i] instead of s[i-1], string index out of range

    return r


"""
Test:
s = 'AAAABBBBCCCCCDDEEEE'
compress(s)

Output:
'A4B4C5D2E4'
"""