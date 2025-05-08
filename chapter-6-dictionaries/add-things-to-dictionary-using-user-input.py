alien={'color':1,'x_pos':1,'y_pos':2}

print('enter your alien color:\n')
user_input=str(input())
alien['color']=user_input

print('enter the position of your alien\nx_pos\ny_pos')
user_input=int(input())
alien['x_pos']=user_input

user_input=int(input())
alien['y_pos']=user_input

if alien['x_pos']<5 or alien['y_pos']<5:
    print('deploying slow alien')

elif alien['x_pos']<10 or alien['y_pos']<10:
    print('deploying medium speed aliens')

else:
    print('deploying fast aliens')