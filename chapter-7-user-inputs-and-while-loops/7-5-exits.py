# flags
# active = True
# while active:
#     print('Enter your age:')
#     user_in = int(input())
#     if user_in < 3:
#         print('The price for your age is 100 rupees')
    
#     elif user_in > 70:
#         print('You are too old go home')
#         active = False

#     elif user_in < 13:
#         print('The price for your age is 300 rupees')
#     else :
#         print('The price for your age is 500 rupees')


while True:
    print('Enter your age:')
    user_in = int(input())
    if user_in < 3:
        print('The price for your age is 100 rupees')
    
    elif user_in > 80:
        print('You are too old')
        break
    
    elif user_in < 13:
        print('The price for your age is 300 rupees')
    else :
        print('The price for your age is 500 rupees')


    
