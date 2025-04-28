prompt = 'say something and i will repeat it\n'
prompt += 'type "quit" to exit\n'

message = ''

# while True:
#     message = input(prompt)

#     if message == 'quit':
#         break

#     print(message)

# print('Session Terminated')

while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)

print('session terminated')