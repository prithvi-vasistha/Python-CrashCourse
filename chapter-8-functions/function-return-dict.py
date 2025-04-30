def build_your_person(first_name, last_name, age = None):
    person= {"first": first_name, 'last' : last_name}
    if age:
        person["age"]=int(age)   
    
    return person

a = build_your_person(first_name='alice', last_name='wonderland', age = 21)
print(a)