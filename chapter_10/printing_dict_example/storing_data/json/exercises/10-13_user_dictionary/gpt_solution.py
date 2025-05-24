from pathlib import Path
import json

# File to store user details
path = Path('user_details.json')

# Store all users' details
user_detail_list = []

def upload_dict(user_dict):
    user_detail_list.append(user_dict.copy())

def exit_sequence():
    if path.exists() and path.read_text().strip():
        try:
            contents = path.read_text()
            json_content = json.loads(contents)
            print("\nPrevious data in file:")
            print(json.dumps(json_content, indent=4))
        except json.JSONDecodeError:
            print('File exists but contains invalid JSON.')
    else:
        print('File is empty or does not exist.')

    # Save new data to the file
    with path.open('w') as f:
        json.dump(user_detail_list, f, indent=4)
    print("\nNew data saved to file. Goodbye!")

def input_sequence():
    user_details_dict = {}
    user_details_dict['name'] = input('Enter your name: ')
    user_details_dict['age'] = input('Enter your age: ')
    user_details_dict['number'] = input('Enter your number: ')
    upload_dict(user_details_dict)

def add_user_details():
    while True:
        user_input = input('\nPress "y" to add a user or "q" to quit: ').strip().lower()
        if user_input == 'q':
            print('Exiting the code...')
            exit_sequence()
            break
        elif user_input == 'y':
            input_sequence()
        else:
            print('Enter a valid input ("y" or "q").')

# Run the program
add_user_details()
