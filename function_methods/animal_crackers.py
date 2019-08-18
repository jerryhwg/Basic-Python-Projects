# Python 3.7.2
# Level 0
# A two-word string
# Returns True if both words begin with the same letter

def animal_crackers(words):
    wordlist = words.lower().split() # split() words per space in string
    #print(wordlist)
    # ['crazy', 'cat']
    return wordlist[0][0] == wordlist[1][0] # result: True

if __name__ == "__main__":
    animal_crackers('Crazy cat')

# key: words.lower().split()