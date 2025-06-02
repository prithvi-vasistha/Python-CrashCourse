def print_flags():
    length = len(history)
    if length in [10, 20, 30, 50, 100, 150]:
        even = 0
        for number in history[-length:]:
            if number % 2 == 0:
                even +=1
        print(f'Your statistics:\n{even} even numbers out of {length} total numbers')
    if len(history) == 200:
        print('history is full, please restart the program')
        even = 0
        for number in history[-200:]:
            if number % 2 == 0:
                even += 1
        
        print(f'Your statistics:\n{even} even numbers out of {len(history)} total numbers')


history = []



active = True

while active:
    print("Press 'quit' to exit")
    user_input = input()
    if user_input == 'quit':
        print('Exitting the program')
        break
    else:
        user_input = int(user_input)
    
    history.append(user_input)
    print_flags()


print(history)
        