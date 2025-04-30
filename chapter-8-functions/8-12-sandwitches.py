def build_sandwitch(bread, cheese, *toppings):
    your_sandwitch = []
    your_sandwitch.append(bread)
    your_sandwitch.append(cheese)
    for topping in toppings:
        your_sandwitch.append(topping)
    
    return your_sandwitch

sandwitch1 = build_sandwitch('Sourdough', 'Cheddar','Lettuce', 'Tomato', 'Onion', 'Pickles', 'Avocado')
sandwitch2 = build_sandwitch('Whole Wheat Bread', 'Swiss', 'Spinach', 'Bell Pepper', 'Cucumber', 'Jalapeños')
sandwitch3 = build_sandwitch('Ciabatta', 'Mozzarella')

print(sandwitch1)
print(sandwitch2)
print(sandwitch3)