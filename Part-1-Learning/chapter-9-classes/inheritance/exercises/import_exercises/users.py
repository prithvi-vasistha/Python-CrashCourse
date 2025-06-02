class User:
    """A simple class containing user structure and greet and describe methods"""

    def __init__(self, first_name, last_name):
        """Initialize values"""
        self.fname = first_name
        self.lname = last_name
    
    def describe_users(self):
        """Print the full user name"""
        print(f"{self.fname}{self.lname}")

    def greet(self):
        """Greet the user"""
        print(f'Hello, {self.fname} {self.lname}')

class Admin(User):
    """Class intended to showcase various privileges of an Admin"""
    def __init__(self, first_name, last_name): 
        """This method is used to initialize the values to Admin class"""
        super().__init__(first_name, last_name)



