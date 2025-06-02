#rstrip() = strip whitespaces to the right
message1='The value associated with favorite_language ❶ contains extra whitespace at the end of the string. When you ask Python for this value in a terminal session, you can see the space at the end of the value ❷.                                                               '
#lstrip() = strip whitespaces to the left
message2='                                                                      The value associated with favorite_language ❶ contains extra whitespace at the end of the string. When you ask Python for this value in a terminal session, you can see the space at the end of the value ❷.'
#strip() = strip whitespaces from both sides
message3='                                                   The value associated with favorite_language ❶ contains extra whitespace at the end of the string. When you ask Python for this value in a terminal session, you can see the space at the end of the value ❷.                                       '

print(message1.rstrip())
print()
print(message2.lstrip())
print()
print(message3.strip())