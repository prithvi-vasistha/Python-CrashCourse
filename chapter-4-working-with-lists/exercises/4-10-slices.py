import math
animals=['lion', 'tiger', 'puma','leopard', 'jaguar']
print(f"The first 3 items in the list are:\n{animals[:3]}")

print()
n=len(animals)
animal_copy=animals[:]

while n>3:
    animal_copy.pop(0)
    n-=1
    if(n>3):
        animal_copy.pop()
        n-=1

print(f"The middle 3 elements of the list are:\n{animal_copy}")
# if(n%2!=0):
#     print(f"The middle 3 elements are:\n{animals[n-1:n+2]}")

# else:
#     print(f"The middle 3 elements are:\n{animals[n-1:n+1]}")
print()

print(f"The last 3 elements of the list are:\n{animals[-3:]}")

