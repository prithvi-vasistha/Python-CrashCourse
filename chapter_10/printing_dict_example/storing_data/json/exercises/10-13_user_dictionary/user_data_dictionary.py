from pathlib import Path
import json

path = Path('user-dict.json')
user_dict = {}
user_list = []



def input_data():
    global user_list
    user_input = input('Enter a data to store:\n')
    user_list.append(user_input)
    return

def read_the_written_file():
    global path
    try:
        contents = path.read_text()
        json_text = json.loads(contents)
        print()
        print('file contents')
        print(json_text)
    except json.JSONDecodeError:
        return
    return

def exit_sequence():
    global user_list, path
    user_list = json.dumps(user_list)
    old_data = path.read_text()
    old_data = json.dumps(old_data)
    to_write = old_data
    to_write += user_list
    path.write_text(to_write) 
    print('Exitting the code')
    read_the_written_file() 
    return


while True:
    user_input = input('Press "q" to quit\nPress "y" to enter data\n')
    if user_input == 'q':
        exit_sequence()
        break

    elif user_input == 'y':
        input_data()

    else:
        print('Enter a valid input')

