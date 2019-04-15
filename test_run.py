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

