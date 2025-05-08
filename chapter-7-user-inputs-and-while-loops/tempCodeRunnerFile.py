unverified_users = [f'user{user}' for user in range (1, 1001)]
verified_users = []

while reversed(unverified_users):
    current_user = unverified_users.pop()
    print(f'Verifying {current_user}')
    verified_users.append(current_user)

print('\n\n\n\nThese are the verified users\n\n\n\n')
print(verified_users)

