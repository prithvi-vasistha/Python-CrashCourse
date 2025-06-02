from pathlib import Path
import json

def greet_user(username):
    print(f"Hello {username} welcome back")

def greet_user_first_time(username):
    print(f"Hello {username} welcome")

def get_new_username():
    user_data_json = json.dumps(user_input)
    path.write_text(user_data_json)
    print('Saved the file successfully')
    greet_user_first_time(user_input)

path = Path('usernames.json')
try:
    content = path.read_text()
    text = json.loads(content)

except FileNotFoundError:
    print("file is not present in the current directory... creating a new file")


user_input = input("Enter your name and i will remember you\n")
for i in user_input:
    if i.lower() not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ):
        print('you have entered your name in an incorrect format try again')
        print('to try again, re-run the program')
        exit()
#try:
    #if user_input in text:
        #print("we found your name in our database are you an old user?\n please confirm your username")
        #print(f"is {user_input} the correct username?")
        #user_decision = input("press 'y' to affirm and 'n' to cancel\n")
        #if user_decision == 'y':
            #greet_user(user_input)
        #elif user_decision == 'n':
            #print("please re-run the code and retry with a different username")
        #else:
            #print("invalid input")

if user_input in text:
    print("we found your name in our database are you an old user?\n please confirm your username")
    print(f"is {user_input} the correct username?")
    user_decision = input("press 'y' to affirm and 'n' to cancel\n")
    if user_decision == 'y':
        greet_user(user_input)
    elif user_decision == 'n':
        print("please re-run the code and retry with a different username")
    else:
        print("invalid input")
else:
    get_new_username()
#except:
    #get_new_username()
    

