import random
lives = 3
lower_limit=1
upper_limit=3
current_number=random.randint(lower_limit, upper_limit)

def out_of_lives():
    print(f'You have run out of guesses\n {current_number} was the number')

while lives >0:
    print(f'Guess the number between {lower_limit} and {upper_limit}')
    if(int(input())==current_number):
        print('You guessed it correct!!!')
        break
    else:
        lives-=1
        print('You guessed it wrong try again')
        if lives==0:
            out_of_lives()


