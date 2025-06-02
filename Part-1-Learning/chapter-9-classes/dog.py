class Dog():
    """This section is basically me learning about classes, this is my first class in python"""

    def __init__(self, name, age):
        """Initialize variables and values"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog obeying command and sitting"""
        print(f'The dog {self.name} is now sitting')

    def bark(self):
        """Simulate a dog obeying command and barking"""
        print(f'The dog {self.name} is now barking')



pug = Dog('yoda', 6)
doberman = Dog('rocky', 8)



pug.bark()
doberman.bark()
pug.sit()
doberman.sit()