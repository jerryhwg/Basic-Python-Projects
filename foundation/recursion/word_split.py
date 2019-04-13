"""
# Python 3.7.2
# a function called word_split() which takes in a string phrase
# and a set list_of_words
# determine if it is possible to split the string in a way
# in which words can be made from the list of words
"""

def word_split(phrase,list_of_words,output = None):

    if output is None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):

            output.append(word)

            return  word_split( phrase[len(word):],list_of_words,output)

    return output


"""

Test

word_split('themanran',['the','ran','man'])
word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
word_split('themanran',['clown','ran','man'])

"""