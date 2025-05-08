def add_pizza_toppings(*toppings):
    for topping in toppings:
        print(f'- {topping}')
    


add_pizza_toppings('a', 'b', 'c')