user_number = int(input('Enter a number you want the binary equivalent of:\n'))

method1=bin(user_number)
method2 = []

while user_number > 0:
    bit = user_number % 2
    method2.append(str(bit))
    user_number = int(user_number/2)

method2.reverse()
result = ''.join(method2)


print(f'The output using built-in library:\n{method1}')
print(f'The output using my method is:\n{result}')
    