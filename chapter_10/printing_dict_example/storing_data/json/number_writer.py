from pathlib import Path
import json

user_inputs = []
active = True

path = Path('inputs.json')
    

while active:
    user_input = input('Enter the numbers you want to store\nPress "q" or "quit" to exit the program\n')
    if user_input in ('q', 'quit'):
        print('recieved a termination signal')
        print('saving the data in json format')
        json_format = json.dumps(user_inputs)
        path.write_text(json_format)
        print('successful')
        exit()
    else:
        try:
            user_input = int(user_input)
            user_inputs.append(user_input)
        except ValueError:
            print('incorrect data type')
