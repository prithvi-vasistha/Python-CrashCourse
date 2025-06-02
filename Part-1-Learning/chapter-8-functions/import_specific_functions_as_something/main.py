from print_cubes import print as print_cube, print_dict

# Here, I have imported the function defined in print_cubes as print_cube instead of print() as print() is an in-built function and it would override it function I had defined in the print_cube.py
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