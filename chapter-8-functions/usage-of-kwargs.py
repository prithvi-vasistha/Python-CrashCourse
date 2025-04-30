def student(name, branch, **details):
    details['Name'] = name
    details['Branch'] = branch
    return details

a=student('alex', 'cse', location = 'United Kingdom', Gender = 'Bender')
b=student('bb', 'va')

print(a)
print()
print(b)