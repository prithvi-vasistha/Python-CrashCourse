prompt = 'say something and i will repeat it\n'
prompt += 'type "quit" to exit\n'

message = ''

active = True

while active == True:
    message = input(prompt)

    if message == 'quit':
        active = False
    
    print(message)