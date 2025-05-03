def print(num_list):
    num = {}
    for number in num_list:
       num[number] = number ** 3
    
    return num

def print_dict (num):
    for number in num:
        print(f'{number} : {num[number]}') 

