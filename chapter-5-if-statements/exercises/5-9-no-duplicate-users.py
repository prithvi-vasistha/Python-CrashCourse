current_users=['Ariel', 'BOB', 'charlie', 'dElta']
#convert user names into a standard form before storing
uniform_current_users=[]
for user in current_users:
    uniform_current_users.append(user.lower())
    


new_users=['brian','ArieL' ,'Clair','ELIJAH']

for user in new_users:
    if user.lower() in uniform_current_users:
        print(f"\nThe username {user} is already in use\nPick a new username\n")
        continue
    
    else:
        print(f"Adding the username {user} to our database")
        current_users.append(user)

print(f"\nUpdated list of users:\n{current_users}")