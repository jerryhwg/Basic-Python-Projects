"""
Use four spaces per indentation level
Keep your lines to 79 characters or fewer
Use single blank lines to group parts of program visually
"""

# Variables
# Strings: surrounded by single or double quotes

print("Hello World")

msg = "Hello World"
print(msg)

# Concatenation
first_name = 'jack'
last_name = 'ryan'
full_name = first_name + ' ' + last_name
print(full_name)

# List: ordered, access using an index or through a loop
colors = ['red', 'blue', 'yellow']
first_color = colors[0]
last_color = colors[-1]

# Changing an element
colors[0] = 'white'
colors[-2] = 'black'

# Append to a list
colors = []
colors.append('green')
colors.append(color)

colors.insert(0, 'purple')

# Delete by its position
del colors[1]
# Remove by its value
colors.remove('yellow')

# pop the last item from a list
most_recent_color = colors.pop()
print(most_recent_color)

# pos the first item from a list
first_color = colors.pop(0)
print(first_color)

# Loop through a list
for color in colors:
    print(color)

squares = []
for i in range(1, 11): # 1 ~ 10
    squares.append(i**2)

# List Comprehensions
squares = [i**2 for i in range(1, 11)]

#
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())

# List comprehensions
upper_names = [name.upper() for name in names]

# Slicing a list
colors = ['red', 'blue', 'yellow', 'green', 'white', 'black']
first_two_colors = colors[:2]
middle_three_colors = colors[1:4]
last_three_colors = colors[-3:]

# Reversed order
colors[::-1]

# Copying a list
copy_of_colors = colors[:]

# List Length
num_colors = len(colors)
print("We have " + str(num_colors) + " colors.")

# Sorting a list
# Sorting a list permanently
colors.sort()
colors.sort(reverse=True)

# Sorting a list temporarily
print(sorted(colors))
print(sorted(colors, reverse=True))

# Reversing the order of a list
colors.reverse()

# Range() function
range(1001) # 0 to 1000

for number in range(1,1001):
    print(number)

# Make a list of numbers
numbers = list(range(1, 1001))

# Simple statistics
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

# Tuples: immutable
dimensions = (1920, 1080)

# Conditional tests
x == 12 # equal
x != 12 # not equal
x > 12 # greater than
x < 12 # less than
x >= 12 # greater than or equal to
x <= 12 # less than or equal to

'green' in colors
'green' not in colors

# Checking multiple conditions
age_0 >= 21 and age_1 >= 21
age_0 >= 21 or age_1 >= 21

# Assign boolean value
game_active = True
game_active = False

# if test
if age >= 18:
    print("You can vote!")

# if, elif, else
if age < 5:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 20

# While loops
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

# Pattern 1
msg = ""
while msg != 'quit':
    msg = input("What's your message? ")
    
    if msg != 'quit':
    print(msg)

# Pattern 2
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    else:
        print(message)

# Pattern 3
while True:
    message = input(prompt)

    if message == 'quit':
        break

    else:
        print(message)

# Avoiding infinite loops

# Removing all instances from a list
while 'cat' in pets:
    pets.remove('cat')
print(pets)