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

