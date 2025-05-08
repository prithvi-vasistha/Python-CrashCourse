prompt = 'say something and i will repeat it\n'
prompt += 'type "quit" to exit\n'

message = ''

while message != 'quit':
    message = input(prompt)

    if message == 'quit':
        print('using break now')
        break

    print(message)


print('successfully terminated')