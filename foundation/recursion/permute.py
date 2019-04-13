# Python 3.7.2
#
# String permutation
# if a character is repeated, treat each occurrence as distinct
# Module 99
# ex. s = 'abc'
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#
# permute(s)


def permute(s):
    
    out = [] #empty list

    # Base Case
    if len(s) == 1:
        out = [s]

    else:

        # for every letter in string

        for i, let in enumerate(s): # ex. i = 1, let = b

            # For every permutation resulting from step 2 and 3

            for perm in permute(s[:i] + s[i+1:]): # ex. s[:1] = a + s[2:] = c

                print ('Current letter is: ', let)
                print('perm is', perm) # ex. a or c = eventually ac

                # Add it to the out
                out += [let + perm] # ex. bac

    return out

"""

Test
s = 'abc'
permute(s)

"""