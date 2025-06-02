from car_skeleton import Car

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
