ken={'first_name': 'ken', 'last_name': 'barbie', 'age': 21}
ellen={'first_name':'ellen', 'last_name': 'paige', 'age':28}
katie={'first_name':'katie', 'last_name': 'paige', 'age':21}

contacts=[ken, ellen, katie]

# print(contacts)

for contact in contacts:
    print(f"User Name : {contact['first_name']}")
    print(f"Full Name : {contact['first_name']} {contact['last_name']}")
    print(f"Age : {contact['age']}\n")