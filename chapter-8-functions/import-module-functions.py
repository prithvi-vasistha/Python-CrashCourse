import helperfunction
import printdict

input_numbers=[]

print('Enter the numbers you desire the squares of:')
active = True

while active:
    print('Press q to quit')
    user_input = input()
    if user_input == 'q':
        print('Thank you for the inputs')
        break
    else:
        user_input = int(user_input)
        input_numbers.append(user_input)

res = helperfunction.print_squares(input_numbers)
printdict.print_dict(res)