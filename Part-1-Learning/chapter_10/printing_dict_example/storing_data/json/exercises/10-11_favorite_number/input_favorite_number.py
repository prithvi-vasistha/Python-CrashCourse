from pathlib import Path
import json

path = Path('favorite_number.json')

user_input = input('Enter your favorite number\n')

#for i in user_input:
    #if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ):
        #print('incorrect value type, please re-run the code and enter proper data type')
        #exit()
try:
    user_input = int(user_input)
    json_data = json.dumps(user_input)
    path.write_text(json_data)
    print('saved successfully')

except ValueError:
    print('incorrect value type')
    

