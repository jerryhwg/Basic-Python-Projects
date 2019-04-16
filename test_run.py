print("Hello World!")
msg = "Hello World!"
print(msg)

first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)

bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0]
last_bike = bikes[-1]
for bike in bikes:
    print(bike)

bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('gitant')

squares = []
for x in range(1,11):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(1,11)]

finishers = ['sam', 'bob', 'ada', 'bea']
frist_two = finishers[:2]
copy_of_bikes = bikes[:]

dimensions = (1920,1080)

x == 42
x != 42
x > 42
x >= 42
x < 42
x <= 42

'trek' in bikes
'surly' not in bikes

game_active = True
can_edit = False

if age >= 18:
    print("You can vote!")

if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15

alien = {'color': 'green', 'points': 5}
print("The alien's color is " + alien['color'])
alien['x_position'] = 0

fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

fav_numbers = {'eric': 17, 'ever': 4}
for name in fav_numbers.key():
    print(name + ' loves a number')

fav_numbers = {'eric': 17, 'ever': 4}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')

name = input("What's your name?")
print("Hello" + name + "!")

age = input("How old are you?")
age = int(age)

pi = input("What's the value of pi?")
pi = float(pi)

current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

msg = ''
while msg != 'quit':
    msg = input("What's your message?")
    print(msg)

def greet_user():
    """Display a simple greeting"""
    print("Hello!")
greet_user()

def greet_user(username):
    print("Hello" + username + "!")
greet_user('jesse')

def make_pizza(topping='bacon'):
    print("Have a " + topping + " pizza!")
make_pizza()
make_pizza('pepperoni')

def add_numbers(x, y):
    return x + y
sum = add_number(3, 5)
print(num)

class Dog():

    def __init__(self,name):
        self.name = name
    def sit(self):
        print(self.name + " is sittting.")

my_dog = Dog('Peso')

print(my_dog.name + " is a great dog!")
my_dog.sit()

class SARDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    def search(self):
        print(self.name + " is searching.")

my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()

filename = 'siddhartha.txt'
with open(filename) as file_object:
    lines = file_object.readline()

for line in lines:
    print(line)

filename = 'journal.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming")

filename = 'journal.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games")

prompt = "How many tickets do you need?"
num_tickets = input(prompt)

try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing.")

user = ['val', 'bob', 'mia', 'ron', 'ned']
first_user = users[0]
second_user = users[1]
newest_user = users[-1]

users[0] = 'valerie'
users[-2] = 'ronald'

users.append('amy')

user = []
users.append('val')
users.append('bob')
users.append('mia')

users.insert(0, 'joe')
users.insert(3, 'bea')

del users[-1]
users.remove('mia')

most_recent_user = users.pop()
print(most_recent_user)

first_user = users.pop(0)
print(first_user)

num_users = len(users)
print("We have " + str(num_users) + " users")

users.sort()
users.sort(reverse=True)

print(sorted(users))
print(sorted(users, reverse=True))
users.reverse()

for user in users:
    print(user)

for user in users:
    print("Welcome, " + user + "!")
print("Welcome, we're glad to see you all!")

for number in range(1001):
    print(number)

for number in range(1, 1001):
    print(number)

numbers = list(range(1, 1001))

ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]
middle_three = finishers[1:4]
last_three = finishers[-3:]

finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]

squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)

squares = [x**2 for x in range(1, 11)]

names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())

upper_name = [name.upper() for name in names]

dimensions = (800, 600)
for dimension in dimensions:
    print(dimension)

dimensions = (800, 600)
print(dimensions)
dimensions = (1200, 900)

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)
print(alien_color)
print(alien_points)

alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)

del alien_0['points']
print(alien_0)

fav_languages = {'jen':'python', 'sarah':'c', 'edward':'ruby', 'phil':'python'}
for name, language in fav_language.items():
    print(name + ": " + language)

for name in fav_languages.keys():
    print(name)

for languages in fav_languages.values():
    print(language)

for name in sorted(fav_languages.keys()):
    print(name + ": " + languages)

num_responses = len(fav_languages)

users = []

new_user = {'last':'fermi', 'first':'enrico', 'username': 'efermi'}
users.append(new_user)

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")


users = [
    {
        'last': 'fermi',
        'first': 'enrico',
        'username': 'efermi',
    },
    {
        'last': 'curie',
        'first': 'marie',
        'username': 'mcurie',
    }
]

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")


fav_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- ": lang)


users = {
    'aeistein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    }
    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}

for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


fav_languages = OrderedDict()
fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']

for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("- " + lang)

aliens = []
for alien_num in range(1000000):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    aliens.append(new_alien)

num_aliens = len(aliens)
print("Number of aliens created:")
print(num_aliens)

car = 'Audi'
car.lower() == 'audi'
True

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
False

age_1 = 23
age_0 >= 21 and age_1 >= 21
True

game_active = True
can_edit = False

age = 19

if age >= 18:
    print("You are old enough to vote!")

age = 17
if age >= 18:
    print("You're old enough to vote!")
else:
    print("You can't vote yet.")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your cost is $" + str(price) + ".")

players = ['al', 'bea', 'cyn', 'dale']
'al'in players
True

banned_users = ['ann', 'chad', 'dee']
user = 'erin'
if user not in banned_users:
    print("You can play!")


players = []
if players:
    for player in players:
        print("Player: " + player.title())
else:
    print("We have no players yet!")


name = input("What's your name? ")
print("Hello, " + name + ".")

age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("\nYou can vote!")
else:
    print("\nYou can't vote yet.")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

message = ""
while message != "quit":
    message = input(prmot)

    if message != quit:
        print(message)

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I've been to " + city + "!")

banned_users = ['eve', 'fred', 'gary', 'helen']
prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done."

players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned!")
        continue
    else:
        players.append(player)

print("\nYour team:")
for player in players:
    print(player)

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat'in pets:
    pets.remove('cat')
print(pets)

def greet_user():
    print("Hello!")
greet_user()

def greet_user(username):
    print("Hello, " + username + "!")

greet_user('jesse')
greet_user('diana')
greet_user('brandon')

def describe_pet(animal, name):
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

def describe_pet(animal, name):
    print("\nI have a " + animal + ".")
    print("Its name is " + name + "."\)
describe_pet(animal='hamster', name='harry')
describe_pet(name='willie', animal='dog')

def describe_pet(name, animal='dog'):
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")

describe_pet('harry', 'hamster')
describe_pet('willie')

def describe_pet(animal, name=None):
    print("\n I have a " + animal + ".")
        if name:
            print("Its name is " + name + ".")
describe_pet('hamster', 'harry')
desdribe_pet('snake')

def get_full_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

musician = get_full_name('jimi', 'hendrix')
print(musician)

def build_person(first, last):
    person = {'first': first, 'last': last}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


def print_models(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print("Printing " + current_model)
        printed.append(current_model)

unprinted = ['phone case', 'pendant', 'ring']
printed = []
print_models(unprinted, printed)

print("\nUnprinted: ", unprinted)
print("Printed: ", printed)


def print_models(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print("Printing " + current_model)
        printed.append(current_model)

original = ['phone case', 'pendant', 'ring']
printed = []

print_models(original[:], printed)
print("\nOriginal: ", original)
print("Printed: ", printed)


def make_pizza(size, *toppings):
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers', 'onions', 'extra cheese')


def build_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}

    for key, value in user_info.items():
        profile[key] = value
    
    return profile

user_0 = build_profile('albert', 'einstein', location='princenton')
user_1 = build_profile('marie', 'curie', location='paris', field='chemistry')

print(user_0)
print(user_1)