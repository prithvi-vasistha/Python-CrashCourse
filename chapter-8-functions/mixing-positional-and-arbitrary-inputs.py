def make_pizza (size, *toppings):
    print(f'Making a {size} pizza with the following toppings')
    for topping in toppings:
        print(f'- {topping}')


make_pizza('small','a', 'b', 'c', 'd', 'e', 'f')