from pathlib import Path
import json

try:
    path = Path('favorite_number.json')
    contents = path.read_text()
    try:
        json_format_data = json.loads(contents)
        print(f'I know your favorite number\n it is {json_format_data} right??')
    except json.JSONDecodeError:
        print('The file is empty')

except FileNotFoundError:
    print('The file is not present in the current directory')
    path = Path('favorite_number.json')

    user_input = input('Enter your favorite number\n')

    try:
        user_input = int(user_input)
        json_data = json.dumps(user_input)
        path.write_text(json_data)
        print('saved successfully')

    except ValueError:
        print('incorrect value type')
    

