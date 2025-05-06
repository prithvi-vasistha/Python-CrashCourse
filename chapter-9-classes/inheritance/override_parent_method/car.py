class Car:
    """A Simple attempt at creating a digital car"""

    def __init__(self, make, model, year):
        """Initialize the values for the class"""
        self.make = make
        self.model = model
        self.year = year
        self.odo = 0

    def describe_car(self):
        """print the specifications of the car"""
        print(f"The car is a {self.make} {self.model}, it was made in {self.year}")

    def start_car(self, key):
        """Simulate a car starting"""
        if key:
            print(f'grrrrrrrrr...... {self.make} is ON')

    def readodometer(self):
        """Simulate reading the odometer of the car"""
        print(f'Your {self.make} has run for {self.odo} kilometers')

    def update_odo(self, value):
        """method to update the odometer value based on the value provided by the object"""
        if value<self.odo:
            print('incorrect value')
            exit()
        self.odo = value



class Electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 45

    def start_car(self, key):
        if key:
            print(f'Hiss, <silence> your {self.make} is ON')

    def describe_battery(self):
        print(f'The car {self.make} has a {self.battery_size}-kWh battery')
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


byd = Electric_Car('byd', 'some_bullshit_ahh_name',2025)
print()
byd.describe_car()
byd.start_car('key')
byd.readodometer()
byd.describe_battery()





