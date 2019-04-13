# Python 3.7.2
# Level 1
# Given a sentence, return a sentence with the words reversed

def master_yoda(words):
    wordlist = words.split()
    reverse_wordlist = wordlist[::-1]
    return ' '.join(reverse_wordlist) # ' '.join(list)

if __name__ == "__main__":
    print(master_yoda('Hello World'))


# key: [::-1]
# key: ' '.join(reverse_wordlist)

"""
Hello World => World Hello
"""