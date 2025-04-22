#check if it is in list
flavors=['black forest', 'red velvet', 'vanilla', 'pineapple']
if'red velvet' in flavors:
    print('The  bakery has red velvet, threfore it is automatically good')

print()
print()

#check if the flavor is not on the list
bad_flavors=['chocolate', 'banana', 'apple']
print('Enter a flavor you desire:')
your_choice=str(input())
if your_choice not in bad_flavors:
    print(f'You are making a wise choice by choosing {your_choice}')

else:
    print("you shouldn't be walking among civilized people")