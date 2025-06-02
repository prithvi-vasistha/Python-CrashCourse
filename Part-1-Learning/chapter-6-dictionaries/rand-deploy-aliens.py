import random

number_of_aliens=30
    

alien={'color':'null', 'points':0, 'position_x_y':[0,0]}
print('special event red is changed to white')

while number_of_aliens > 0:
    rand_x_range=random.randrange(1, 101)
    if rand_x_range < 26:
        alien['color'] = 'green'
        alien['points'] = 5
        alien['position_x_y'] = [rand_x_range, 10]
        number_of_aliens-=1
    
    elif rand_x_range < 75:
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['position_x_y'] = [rand_x_range, 10]
        number_of_aliens-=1
    
    else:
        alien['color'] = 'red'
        alien['points'] = 15
        alien['position_x_y'] = [rand_x_range, 10]
        number_of_aliens-=1

    for key, value in alien.items():
        if(value == 'red'):
            value = 'white'
        if(key == 'color'):
            print('\n')
        print(key, ':', value)
    




    
        

        
