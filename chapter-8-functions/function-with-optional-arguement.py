def print_name_formatted(first_name, last_name, middle_name=''):
    if middle_name != '':
        name = first_name.title()+' '+ middle_name.title()+' '+last_name.title()
        return name
    else:
        name = first_name.title()+' '+last_name.title()
        return name


user_f_name = input('Enter a first name\n')
user_m_name = input('Enter a middle name\n')
user_l_name = input('Enter a last name\n')

a = print_name_formatted(first_name=user_f_name, middle_name=user_m_name, last_name=user_l_name)
print(a)