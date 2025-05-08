# using a for loop isn't advisible

# fruits = ['apple', 'orange', 'apple', 'apple']

# for fruit in fruits:
#     if fruit == 'apple':
#         fruits.remove(fruit)

# print(fruits)


# use while loop instead
fruits = ['apple', 'apple', 'banana', 'apple']

while 'apple' in fruits:
    fruits.remove('apple')

print(fruits)
