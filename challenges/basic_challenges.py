# volume of a sphere given its radius

def vol(rad):
    return (4.0/3.0)*(3.14)*(rad**3)

# check whether a number is in a given range

def range_check(num,low,high):
    return num in range(low,high)

# take a string and calculates the number of upper case letters and lower case letters

def up_low(s):
    d={"upper":0, "lower":0} # init
    for c in s:
        if c.isupper():
            d["upper"] += 1 # add count
        if c.islower():
            d["lower"] += 1
        else:
            pass

    print("Original String: ", s)
    print("No. of Upper case characters: ", d["upper"]) # count
    print("No. of Lower case characters: ", d["lower"])

"""
Test:
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

"""

# take a list and return a new list with unique elements of the first list

def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

"""
Test:
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

"""

# multiply all the numbers in a list

def multiply(nums):
    total = nums[0]
    for x in nums:
        total *= x
    return total

"""
Test:
multiply([1,2,3,-4])

"""

# palindrome check
# palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward

def palindrome(s):
    return s == s[::-1]

"""
palindrome("neveroddoreven")
"""

# pangram: check string incorporating all the alphabet letters

import string

def ispangram(str1, alphabet=string.ascii_lowercase): # string.ascii_lowercase : The lowercase letters
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

"""
Test:
ispangram("The quick brown fox jumps over the lazy dog")

string.ascii_lowercase : The lowercase letters 'abcdefghijklmnopqrstuvwxyz'
https://docs.python.org/3/library/string.html

"""