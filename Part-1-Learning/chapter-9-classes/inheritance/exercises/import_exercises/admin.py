from users import *
class Admin(User):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.privileges = Privilege(fname, lname)


class Privilege():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.privileges = ['can add user', 'can remove user', 'can ban user']

    def print_privileges(self):
        """method used to print the privileges of an admin"""
        print(f'The user {self.fname} {self.lname} can do the following')  
        for privilege in self.privileges:
            print(privilege)
