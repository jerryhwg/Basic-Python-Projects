"""
Pyton 3.7.2

Balanced Parentheses Check
Given a string of opening and closing parentheses, check whether it's balanced
ex.
([]) balanced
([)] not balanced

Usage: balance_check(s)

Test
balance_check('[]')
balance_check('[](){([[[]]])}')
balance_check('()(){]}')
"""

def balance_check(s):

    # Edge case check, if number of elements is odd, return False
    if len(s)%2 != 0:
        return False

    opening = set('([{')
    # {'(', '[', '{'}

    matches = set([ ('(',')'), ('[',']'), ('{','}') ])
    # {('(', ')'), ('[', ']'), ('{', '}')}

    stack = [] # list

    for paren in s:

        if paren in opening:
            stack.append(paren) # add opening to the list 'stack'
        
        else: # if paren is not in opening, that means paren is "closing"

            if len(stack) == 0: # if 0 element case, return False
                return False

            last_open = stack.pop() # the last open parenthesis

            if (last_open,paren) not in matches: # if (last_open, closing) pair is NOT in matches, return False
                return False

    return len(stack) == 0 # if append & pop occurs equally, the list 'stack' must be empty, then True