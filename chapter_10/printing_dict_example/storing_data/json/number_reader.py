from pathlib import Path
import json

try:
    path = Path('inputs.json')
    contents = path.read_text()
    json_format_data = json.loads(contents)
    print(json_format_data)

except FileNotFoundError:
    print('The file is not present at the given directory')
