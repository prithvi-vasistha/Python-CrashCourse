from pathlib import Path
import json

try:
    path = Path('favorite_number.json')
    contents = path.read_text()
    json_format_data = json.loads(contents)
    print(f'I know your favorite number\n it is {json_format_data} right??')

except FileNotFoundError:
    print('The file is not present in the current directory')
