from print_cubes import print_cube, print_dict

input_array = []
while True:
    print('Enter the numbers you want the squares of:\nPress "q" to quit')
    user_input = input()
    if(user_input == 'q'):
        a = print_cube(input_array)
        break
    user_input = int(user_input)
    input_array.append(user_input)

print_dict(a)