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




ppv = User('prithvi', 'vasistha')
ppv.describe_users()
ppv.greet()