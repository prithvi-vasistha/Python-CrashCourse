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

<<<<<<< HEAD
    def petrol_car(self):
        """ a simple method that prints the selected car runs on petrol"""
        print(f'{self.make} runs on petrol')

class Battery():
    """ a simple attempt at configuring battery"""
    def __init__(self, battery_size):
        """ a simple method to initialize the values in Battery class"""
        self.battery_size = battery_size

    def describe_battery(self, make):
        """ a simple method to print the battery information of the EV"""
        print(f'the car {make} has a battery capacity of {self.battery_size}-kWh')

class Electric_Car(Car):
    """ a simple attempt of derivng an Electric vehicle based on the original class Car with additional methods"""
    def __init__(self, make, model, year):
        """ a simple method to initialize values in child class using parent classes"""
        super().__init__(make, model, year)
        self.battery_size = Battery(45)

    def start_car(self, key):
        """ a simple method that simulates the starting of a car by checking the key"""
        if key:
            print(f'Hiss, <silence> your {self.make} is ON')


    def petrol_car(self):
        """ a simple method that overrides the parent class to say that EV does not run on petrol"""
        print(f'mofo {self.make} does not run on petrol')


=======


class Electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 45

    def start_car(self, key):
        if key:
            print(f'Hiss, <silence> your {self.make} is ON')

    def describe_battery(self):
        print(f'The car {self.make} has a {self.battery_size}-kWh battery')
>>>>>>> 80751539a9bef86ad0e81dc317c7981ab6cb2a8b
mercedes = Car('mercedes', 's-class', 2012)
bmw = Car('BMW', '320d', 2009)

mercedes.describe_car()
print()
mercedes.update_odo(3000)
mercedes.readodometer()
<<<<<<< HEAD
mercedes.petrol_car()
=======
>>>>>>> 80751539a9bef86ad0e81dc317c7981ab6cb2a8b

bmw.describe_car()
print()

bmw.start_car('key')
mercedes.start_car('key')
<<<<<<< HEAD
bmw.petrol_car()
=======
>>>>>>> 80751539a9bef86ad0e81dc317c7981ab6cb2a8b

bmw.readodometer()
mercedes.readodometer()


byd = Electric_Car('byd', 'some_bullshit_ahh_name',2025)
print()
byd.describe_car()
byd.start_car('key')
byd.readodometer()
<<<<<<< HEAD
byd.battery_size.describe_battery('byd')

byd.petrol_car()
=======
byd.describe_battery()

>>>>>>> 80751539a9bef86ad0e81dc317c7981ab6cb2a8b




