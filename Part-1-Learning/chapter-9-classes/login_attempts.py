class User_Login():
    """A simple class aimed to store the amount of times a user has tried logging in"""
    def __init__(self, user_name):
        self.user = user_name
        self.login_attempts = 0

    def login(self):
        self.login_attempts += 1
        print(f'a login attempted by user {self.user} and the value of login attempts increased by 1')

    def reset(self):
        print('A reset call has been made\nresetting the values')
        self.login_attempts = 0

    def print_login_attempts(self):
        print(f'Number of login attempts --------> {self.login_attempts}')
        print()


ppv = User_Login('ppv')
ppv.login()
ppv.print_login_attempts()
ppv.login()
ppv.print_login_attempts()
ppv.login()
ppv.print_login_attempts()
ppv.login()
ppv.print_login_attempts()
ppv.login()
ppv.print_login_attempts()
ppv.login()
ppv.print_login_attempts()
ppv.reset()
ppv.print_login_attempts()

