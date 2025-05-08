print('Enter your age:')
user_age=int(input())

if user_age<2:
    print("You're a baby")

elif user_age>=2 and user_age<4:
    print("You're a toddler")

elif user_age>=4 and user_age<13:
    print("You're a kid")

elif user_age>=13 and user_age<20:
    print("you're a teenager")

elif user_age>=20 and user_age<65:
    print("You're an adult")

else:
    print("You're an elder")