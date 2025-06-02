from pathlib import Path
import json

try:
    path = Path('usernames.json')
    contents = path.read_text()
    json_data = json.loads(contents)
    print(f'Hello {json_data}')

except FileNotFoundError:
    print('The file you are trying to read is not present in the current directory')
