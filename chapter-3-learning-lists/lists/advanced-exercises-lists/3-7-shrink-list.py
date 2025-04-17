guest_list=['daniel radcliffe', 'emma watson', 'alison brie']
print('The following emails will be sent:')
print(f"Hi {guest_list[0].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[1].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[2].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")

print()
print('**************************************************')
print('We have found a bigger venue and can accomodate 3 more people\n New set of invites will be sent soon')
print('**************************************************')
print()
print()
guest_list.insert(0, 'peter')
guest_list.insert(2, 'griffin')
guest_list.append('louis')
print(f"Hi {guest_list[0].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[1].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[2].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[3].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[4].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[5].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print()
print('**************************************************')
print('The venue people cancelled. Sorry guys but the guest list is shortened to 2')
print('**************************************************')
print()
print()

popped_guy=guest_list.pop()
print(f"Sorry {popped_guy.title()} you are uninvited from the party. Please understand our situation")
popped_guy=guest_list.pop()
print(f"Sorry {popped_guy.title()} you are uninvited from the party. Please understand our situation")
popped_guy=guest_list.pop()
print(f"Sorry {popped_guy.title()} you are uninvited from the party. Please understand our situation")
popped_guy=guest_list.pop()
print(f"Sorry {popped_guy.title()} you are uninvited from the party. Please understand our situation")

print(f"{guest_list[0].title()} You are still invited to the party please do attend")
print(f"{guest_list[1].title()} You are still invited to the party please do attend")


del guest_list[1]
del guest_list[0]

print(guest_list)
