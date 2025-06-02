class Car:
    """A Simple attempt at creating a digital car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odo = 0

    def describe_car(self):
        print(f"the car is a {self.make} {self.model}, it was made in {self.year}")

    def start_car(self, key):
        if key:
            print(f'grrrrrrrrr...... {self.make} is ON')

    def readodometer(self):
        print(f'Your {self.make} has run for {self.odo} kilometers')

    def update_odo(self, value):
        if value < self.odo:
            print('incorrect value')
            exit()
        self.odo = value

    def petrol_car(self):
        print('This car runs on petrol')

class Electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 45

    def start_car(self, key):
        if key:
            print(f'Hiss, <silence> your {self.make} is ON')


    def describe_car(self):
        print(f"the electric car is a {self.make} {self.model}, it was made in {self.year}")
        print(f'it has a battery size of {self.battery_size}')

    def print_battery(self):
        print(f'The current battery size is {self.battery_size}')

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print('The battery has been updated successfully to 65W')
            self.print_battery()

        else:
            print('The battery is already upgraded')
            self.print_battery()

mercedes = Car('mercedes', 's-class', 2012)
bmw = Car('BMW', '320d', 2009)

mercedes.describe_car()
print()
mercedes.update_odo(3000)
mercedes.readodometer()
mercedes.petrol_car()

bmw.describe_car()
bmw.petrol_car()
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
byd.petrol_car()
byd.print_battery()
byd.upgrade_battery()
byd.upgrade_battery()


