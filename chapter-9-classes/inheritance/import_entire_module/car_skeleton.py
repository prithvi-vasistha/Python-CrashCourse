"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Electric_Car(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = Battery(battery_size)

    def start_car(self, key):
        if key == 'key':
            print(f'Hiss, <silence> your {self.make} is ON')


class Battery():
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def print_battery_details(self, car):
        print(f"The car {car} has a battery size of {self.battery_size}kWh")

    def print_range(self):
        if self.battery_size < 45:
            print('Your car has a range of 100 kilometers')

        elif self.battery_size < 65:
            print('Your car has a range of 200 kilometers')

        else:
            print("unknown battery size, hence predicting the range is near impossible")
