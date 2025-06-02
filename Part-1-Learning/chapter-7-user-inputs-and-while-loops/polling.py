reviews = {}

poll_active = True

while poll_active:
    print('What is your name?')
    name = input()
    print('What is your review?')
    review = input()

    reviews[name] = review
    
    print('Would u take another poll?\n1. Yes\n2. No')
    if int(input()) == 2:
        print('Thank you for taking the survey')
        break


print('---- Poll Results ----')

for key in reviews:
    print(f'{key}   :   {reviews[key]}')


