# Dictionaries: key-value pair, unordered
fruits = {'apple':5, 'banana':3, 'orange':2}
print("Number of apple is", fruits['apple'])
fruits['kiwi'] = 7
del fruits['kiwi']
len(fruits)

# Looping through all key-value pairs
for name, number in fruits.items():
    print(name + ' number: ' + str(number))

# Looping through all keys
for name in fruits.keys():
    print(name)

# Looping through all the values
for number in fruits.values():
    print(number)

# User Input
name = input("What is your name? ")
print("Hello, " + name + "!")

age = input("How old are you? ")
age = int(age)

# Nesting
# A list of dictionaries: store a set of dictionaries in a list

# Method 1
users = []
new_user = {
    'last': 'ryan',
    'first': 'jack',
    'username': 'jryan',
}
users.append(new_user)

# Method 2
users = [
    {
        'last': 'ryan',
        'first': 'jack',
        'username': 'jryan',
    },
    {
        'last': 'bond',
        'first': 'james',
        'username': 'jbond',
    },
]

# Lists in a dictionary: store a list inside a dictionary; associate more than one value with each key

fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

# A dictionary of dictionaries: store a dictionary inside another dictionary

users = {
    'jackryan': {
        'last': 'ryan',
        'first': 'jack',
        'username': 'jryan',
    },
    'jamesbond': {
        'last': 'bond',
        'first': 'james',
        'username': 'jbond',
    }
}

# OrderedDict: keep track of the order in which keys and values are added

from collections import OrderedDict

fav_languages = OrderedDict()

fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']

for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("- " + lang)