def print_formatted(first_name, last_name):
    return(first_name.title()+' '+last_name.title())

user_f_name = input('Enter a first name\n')
user_l_name = input('Enter a last name\n')

a = print_formatted(first_name=user_f_name, last_name=user_l_name)
print(a)