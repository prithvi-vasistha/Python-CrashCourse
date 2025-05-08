players=['alice', 'bob', 'charlie', 'delta', 'ellen']
# print() first 3 elements
print(players[0:3])

# print() the 2nd, 3rd and 4th elements
print(players[1:4])

# we can omit the first index of the slice in python to say from the beginning
print(players[:4])

# similary, we can omit the last index index of slice in python to specify that it has to slice till the end
print(players[2:])

print(players[-3:])