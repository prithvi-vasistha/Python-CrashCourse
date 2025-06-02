credentials=('johndoe@gmail.com', 'john123')
def wrong_password():
    print("Incorrect password try again")

def wrong_email_id():
    print("Incorrect Email-Id try again")

print("Please enter email id:")
if str(input())==credentials[0]:
    print("Please enter your password:")
    if str(input())==credentials[1]:
        print("Your credentials are correct, Welcome back John Doe")
    
    else:
        wrong_password()

else:
    wrong_email_id()

    


# if temp[0]==credentials[0]:
#     print(f"Please enter password:\n{input(str).append(temp)}")
#     if temp[1]==credentials[1]:
#         print("login credentials are correct, Welcome back!!")


# else:
#     temp=[]
#     print("wrong credentials")