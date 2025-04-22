users=['ariel', 'bob', 'charlie', 'admin', 'delta', 'ellen']
# users=[]
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user.title()} would you like to see the updates from the time of last login?')
        
        else:
            print(f'Hello {user.title()}, Have a good day!!')

else:
    print('There are no users registered to the platform')