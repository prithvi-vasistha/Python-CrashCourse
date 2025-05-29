from name_function import *

fname = None
lname = None

def user_name():
    user_choice = input("do you have both first name and a last name??\n press 'y' for yes \n press 'n' for no\n")
    if user_choice == 'y':
        user_name = input("Enter a first name:\n") 
        if user_name.isalpha:
            fname = user_name
        else:
            print("Invalid first name")
            exit()

        user_name = input("Enter a last name:\n") 
        if user_name.isalpha:
            lname = user_name
        else:
            print("Invalid last name")
            exit()

        formatted = get_formatted_name(fname, lname)
        print (formatted)

    elif user_choice == 'n':
        user_name = input("Enter a first name:\n") 
        if user_name.isalpha:
            fname = user_name
        else:
            print("Invalid first name")
            exit()
        formatted = format_first_name(fname)
        print (formatted)

    else:
        print("invalid input exitting the program")
        exit()

def enter_user_name_loop():
    user_name()
    while(True):
        user_choice = input("Do you want to enter another name?\n press 'y' for 'yes'\n press 'n' for 'no'\n")
        if user_choice == 'y':
            user_name()
        elif user_choice == 'n':
            print("Exitting the program")
            break;
        else:
            print("invalid input, exitting the code abruptly")
            exit()



user_choice = input("Do you wish to insert names in a loop? \n if yes, press 'y' \n else press 'n'\n")
if user_choice == 'y':
    enter_user_name_loop()
elif user_choice == 'n':
    user_name()
else:
    print("invalid user input")
    exit()


