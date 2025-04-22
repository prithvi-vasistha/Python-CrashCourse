import random


possible_colors=['red', 'green', 'yellow']
alien_color=random.choice(possible_colors)

if alien_color == 'red':
    print("alien is angry")

elif alien_color == 'green':
    print('alien is happy')

else:
    print('alien is neutral')