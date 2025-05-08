users={'ken': {'first_name': 'ken', 'last_name': 'barbie', 'age': 21}, 'ellen':{'first_name':'ellen', 'last_name': 'paige', 'age':21}}

for id, details in users.items():
    print(f'username : {id}')
    print(f"Full Name : {details['first_name']} {details['last_name']}")
    print(f"age : {details['age']}\n")

