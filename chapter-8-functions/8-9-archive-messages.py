def send_messages(messages):
    sent_messages = []
    while messages:
        sent_messages.append(messages.pop())
    return(sent_messages)

messages = ['Hi, Tom', 'Hello, Bob', 'Hey, Jennifer']
print(f'Messages list before : {messages}')

send_msg = send_messages(messages[:])

print()
print(f"Sent Messages : {send_msg}")
print(f'Messages List After: {messages}')