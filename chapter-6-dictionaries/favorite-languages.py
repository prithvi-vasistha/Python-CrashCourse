fav_lang={'alex':'rust', 'andy': 'react', 'sarah':'c'}

for keys, values in fav_lang.items():
    print(f'{keys} loves {values}')


print()

#using sets to remove duplicates
#first let us add a duplicate
fav_lang['roy']='c'

for values in fav_lang.values():
    print(f'{values}')


# eliminate duplicates using set()
print()

for value in set(fav_lang.values()):
    print(f'{value}')