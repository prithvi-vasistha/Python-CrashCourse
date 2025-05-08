#Welcome options
welcome = {1 : 'Order Pizza',
           2 : 'Exit'
           }

build_pizza = {1: 'Choose pizza from our menu',
               2: 'Build your own pizza'
               }

# Toppings as a dictionary
toppings = {
    0: "Quit",
    1: "Mushrooms",
    2: "Onions",
    3: "Sausage",
    4: "Bacon",
    5: "Extra cheese",
    6: "Black olives",
    7: "Green peppers",
    8: "Pineapple",
    9: "Spinach",
    10: "Tomatoes",
    11: "Jalapenos",
    12: "Chicken",
    13: "Ham",
    14: "Beef",
    15: "Artichokes",
    16: "Garlic",
    17: "Basil",
    18: "Pepperoni"
}

# Pizza types as a dictionary
pizza_types = {
    0: "Margherita",
    1: "Pepperoni",
    2: "BBQ Chicken",
    3: "Hawaiian",
    4: "Veggie",
    5: "Meat Lovers",
    6: "Supreme",
    7: "Buffalo Chicken",
    8: "Four Cheese",
    9: "Pesto"
}

# Dough types as a dictionary
dough_types = {
    0: "Thin crust",
    1: "Thick crust",
    2: "Stuffed crust",
    3: "Gluten-free",
    4: "Whole wheat",
    5: "Cheese burst",
    6: "Flatbread",
    7: "Cauliflower crust"
}

# Extra cheese options as a dictionary
extra_cheese_options = {
    0: "Regular cheese",
    1: "Extra mozzarella",
    2: "Cheddar blend",
    3: "Parmesan topping",
    4: "Vegan cheese"
}


def printDict (dict):
    for key in dict:
        print(f'{key}  :  {dict[key]}')

def printList (list):
    for value in list:
        print(value)

your_pizza=[]




print('Welcome to our pizza joint, What will you be having today?')
printDict(welcome)
if int(input()) == 2:
    print('Thank you,\nPlease visit again')


else:
    print('Please select one option:')
    printDict(build_pizza)


    if int(input()) == 1:
        printDict(pizza_types)

        pizza_user = int(input())
        print(f'Your order of {pizza_types[pizza_user]} is being prepared')
        exit()
        

    else:
        print('Select the crust of your liking:')
        printDict(dough_types)

        user_dough = int(input())
        your_pizza.append(dough_types[user_dough])

        print(f'You selected {dough_types[user_dough]}')
        print(f'Your pizza configuration till now :')
        print(your_pizza)

        print('Select Cheese :')
        printDict(extra_cheese_options)

        user_cheese = int(input())
        your_pizza.append(extra_cheese_options[user_cheese])
        print(f'You selected {extra_cheese_options[user_cheese]}')
        print(f'Your pizza configuration till now:')
        print(your_pizza)

        print('Select as many toppings as needed:')
        printDict(toppings)

    while True:
        user_toppings = int(input())
        if user_toppings == 0:
            break
        else :
            print(f'You selected {toppings[user_toppings]}')
            your_pizza.append(toppings[user_toppings])
    
    print(f'Your pizza configuration:')
    print(your_pizza)
    print('Thanks for choosing us')
    exit()









