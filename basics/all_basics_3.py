# Functions: blocks of code, designed to do one specific job
# information passed to a function is 'argument'
# information received by a function is 'parameter'

# Passing an argument
def greet_user(name):
    print("Hello, " + name + "!")

greet_user('Jesse')

# Default values for parameters
def make_pizza(topping='bacon'):
    print("Have a " + topping + " pizza!")

make_pizza()
make_pizza('pepperoni')

# Returning a value
def add_numbers(n1, n2):
    return n1 + n2

sum = add_numbers(2, 3) # return -> sum
print(sum)

# Class: blueprint of an object, behavior and informatioin, attributes and methods(functions belongs to a class)
# Child class inherits the attributes and methods from its parent class

# Parent Class
class Dog():

    def __init__(self,name):
        # Initialize dog object
        self.name = name

    def sit(self):
        print(self.name + " is sitting.")

my_dog = Dog('Benji')

print(my_dog.name + " is a great dog!")
my_dog.sit()

# Child Class
class POLDog(Dog):
    def __init__(self,name):
        super().__init__(name)
    def search(self):
        print(self.name + " is searching. ")

my_dog = POLDog('Lassie')
print(my_dog.name + " is a search dog. ")
my_dog.sit()
my_dog.search()

# Working with Files
# Reading a file and storing its lines
filename = 'test.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

# Writing to a file
filename = 'test.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love biking.")

# Appending to a file
filename = 'test.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love cooking.")