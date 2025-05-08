from car_skeleton import *
print('this method imports all methods from a module')

my_car =  Car('maruti suzuki', 'swift', 2021)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 23

my_car.read_odometer()






Tesla =  Electric_Car('Tesla', 'S', 2016, 56)

print(Tesla.get_descriptive_name())

Tesla.odometer_reading = 23

Tesla.start_car('key')

Tesla.read_odometer()

Tesla.battery_size.print_battery_details('Tesla')
Tesla.battery_size.print_range()
