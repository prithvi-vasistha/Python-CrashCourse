inventory=[['apple', 1], ['banana', 2], ['apple', 5], ['mangoes', 4], ['apple', 6]]
dict={}

for lists in inventory:
    if dict.get(lists[0]):
        dict[lists[0]] = dict.get(lists[0]) + lists[1]

    else:
        dict[lists[0]]=lists[1]

print(dict)