from pathlib import Path
import json

path = Path('usernames.json')
user_input = input("Enter your name and i will remember you\n")
for i in user_input:
    if i.lower() not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ):
        print('you have entered your name in an incorrect format try again')
        print('to try again, re-run the program')
        exit()
    
user_data_json = json.dumps(user_input)
path.write_text(user_data_json)
print('Saved the file successfully')

