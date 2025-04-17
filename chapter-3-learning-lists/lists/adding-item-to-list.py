#insert to the end of the list
#append() to the end of the list
motorcycles=['yamaha', 'suzuki', 'honda']
print('the motorcycles before appending:')
for i in motorcycles:
    print(i)

motorcycles.append('ather')
print()
print('The list of motorcycles after appending:')
for i in motorcycles:
    print(i)

#insert into specific position
#use insert(<index>, <value>) method to insert a value in specific position of a list
print()
print('usage of insert() method')
motorcycles.insert(0, 'ducati')

for i in motorcycles:
    print(i)


#Remove elements from list
#Use del <listname>[<index>] method
print()
print()
print('Usage of del statement ot remove item at a specific index')
print()
print('Before Values')
for i in motorcycles:
    print(i)
del motorcycles[0]
print('\nAfter values')
for i in motorcycles:
    print(i)

#Delete item using pop() method
print()
print('usage of pop() in python:')
print()
print('before values:')
for i in motorcycles:
    print(i)
print()
popped_value = motorcycles.pop()


print('after values:')
for i in motorcycles:
    print (i)

print(f"The popped element from the list was {popped_value}")


#pop(<index>) from a specifc index
print()
print('pop() from  aspecific index:')
print()
print('The values before:')
for i in motorcycles:
    print(i)

popped=motorcycles.pop(0)

print('The after values:')
for i in motorcycles:
    print(i)

print(f"My first bike was {popped}")


#remove an element by value
#remove(<value>)
print()
print()
print("remove by specific value")
print('before removing values:')
for i in motorcycles:
    print(i)

motorcycles.remove('suzuki')
print()
print('after removing by element:')
for i in motorcycles:
    print(i)