# A list comprehension allows you to generate this same list in just one line of code.

# Without List Comprehension:

# squares=[]
# for number in range(1, 11):
#     squares.append(number**2)

# print(squares)

# With List Comprehension:

squares = [value**2 for value in range(1, 11)]
print(squares)