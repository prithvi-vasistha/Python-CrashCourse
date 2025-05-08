guest_list=['daniel radcliffe', 'emma watson', 'alison brie']
print('The following emails will be sent:')
print(f"Hi {guest_list[0].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[1].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[2].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print()

guest_absent=guest_list[0]
print(f"{guest_absent.title()} so sorry you couldn't make it. Good luck with your future endeavors")

print('New set of mails will be sent with a mystery guest')
guest_list[0]='Keanu Reeves'
print()
print(f"The mystery guest has been decided as {guest_list[0]}")
print()
print('The following emails will be sent:')
print(f"Hi {guest_list[0].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[1].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")
print(f"Hi {guest_list[2].title()} you're invited!!\n 21/04/2025\t\t at Nagarabhavi.\nPlease be at the venue by 5pm")