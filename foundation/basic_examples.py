# Example 1

st = 'Print only the words that start with s in this sentence'

for word in st.split(): # split by word at space " "
    if word.startswith('s'):
        print(word)

# another way

for word in st.split():
    if word[0].lower() == 's':
        print(word)


# Example 2

print([x for x in range(0,11) if x%2 == 0])

# another way

for num in range (0,11,2):
    print(num)


# Example 3

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print(word + ' is even!')

# another way

for word in st.split():
    x = len(word)
    if x%2 == 0:
        print(word + ' is even!')


# Example 4

for num in range(1,101):
    if (num%3 == 0 and num%5 == 0):
        print('FizzBuzz')
    elif (num%3 == 0):
        print('Fizz')
    elif (num%5 == 0):
        print('Buzz')
    else:
        print(num)


# Example 5

[x[0] for x in st.split()]