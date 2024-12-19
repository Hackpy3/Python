# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ['apple', 'banana', 'cherry']

# A list with mixed data types
mixed_list = [1, 'hello', 3.14, True]



fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry


fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']


# Append an element to the end of the list
fruits.append('date')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Extend the list by appending elements from another list
fruits.extend(['elderberry', 'fig'])
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

# Insert an element at a specific position
fruits.insert(1, 'banana')
print(fruits)  # Output: ['apple', 'banana', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

# Remove the first occurrence of a specific element
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

# Remove an element by index and get its value
popped_element = fruits.pop(2)
print(popped_element)  # Output: cherry
print(fruits)  # Output: ['apple', 'blueberry', 'date', 'elderberry', 'fig']

# Remove an element by index using del
del fruits[0]
print(fruits)  # Output: ['blueberry', 'date', 'elderberry', 'fig']


# Syntax: list[start:end:step]
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Get elements from index 1 to 3 (3 not included)
slice1 = fruits[1:4]
print(slice1)  # Output: ['banana', 'cherry', 'date']

# Get elements from the beginning to index 2 (2 not included)
slice2 = fruits[:3]
print(slice2)  # Output: ['apple', 'banana', 'cherry']

# Get elements from index 2 to the end
slice3 = fruits[2:]
print(slice3)  # Output: ['cherry', 'date', 'elderberry', 'fig']

# Get every second element
slice4 = fruits[::2]
print(slice4)  # Output: ['apple', 'cherry', 'elderberry']

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of fruits containing the letter 'a'
fruits_with_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_a)  # Output: ['banana', 'date']





