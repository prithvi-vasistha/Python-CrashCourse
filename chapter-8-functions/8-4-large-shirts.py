def print_tees(size = 'large', message = 'I love Python' ):
    print(f'A T-Shirt of size {size} having a message {message} is being printed')


sizes = {'s': 'small', 'm': 'medium', 'l':'large', 'xl' :'extra large'}

for key in sizes:
    print(f'{key} : {sizes[key]}')

while True:
    user_size = input('Enter the size you want\n')
    if user_size in sizes:
        user_size = sizes[user_size]
        break
    else:
        # print('Enter a valid size')
        break
user_message = input('Enter a message you want to print\n')

if user_message == '' and user_size != '':
    print_tees(user_size)

elif user_size == '' and user_message != '':
    print_tees(user_message)

if user_message == '' and user_size == '':
    print_tees()

else:
    print_tees(user_size, user_message)

