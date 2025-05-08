print("enter your email id:")
email=str(input())


print(f"your username for this session will be: \n{email.removesuffix('@gmail.com')}")