class Car:
    """A Simple attempt at creating a digital car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odo = 0

    def describe_car(self):
        print(f"The car is a {self.make} {self.model}, it was made in {self.year}")

    def start_car(self, key):
        if key:
            print(f'grrrrrrrrr...... {self.make} is ON')

    def readodometer(self):
        print(f'Your {self.make} has run for {self.odo} kilometers')

    def update_odo(self, value):
        if value<self.odo:
            print('incorrect value')
            exit()
        self.odo = value

mercedes = Car('mercedes', 's-class', 2012)
bmw = Car('BMW', '320d', 2009)

mercedes.describe_car()
print()
mercedes.update_odo(3000)
mercedes.readodometer()

bmw.describe_car()
print()

bmw.start_car('key')
mercedes.start_car('key')

bmw.readodometer()
mercedes.readodometer()
