def print_cities(dict):
    list=[]
    for key in dict:
        list.append(f'{key.title()}, {dict[key].title()}')
    list.reverse()
    return list

print("Enter the city names followed by state names")

dict = {}
active = True


while active:
    user_city= input('Enter the city name\n')
    user_state= input('Enter the state name\n')
    print('would you like to continue?\npress "y" to continue\npress anything else to quit')
    dict[user_city] = user_state
    if input() != 'y':
        break
    


a=print_cities(dict)
print(a)