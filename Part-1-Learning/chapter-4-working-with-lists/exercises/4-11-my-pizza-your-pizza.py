pizzas=['margherita', 'corn & cheese', 'onion & capsicum']
friend_pizza=pizzas[:]
friend_pizza.append('mushroom cheese')

print('The pizzas in my list are:')
for pizza in pizzas:
    print(f"{pizza.title()} from pizzahut")

print()
print("The pizzas in my friend's favorites list are:")
for pizza in friend_pizza:
    print(f"{pizza.title()} from dominoes")
