pizza={'onion & capsicum' : ['thin', 'no'], 'margherita': ['cheesy', 'yes']}

print('pizza configurations available:')

for key, value in pizza.items():
    print(key)
    print(f"Crust : {value[0]}\nCheese : {value[1]}")
    print()