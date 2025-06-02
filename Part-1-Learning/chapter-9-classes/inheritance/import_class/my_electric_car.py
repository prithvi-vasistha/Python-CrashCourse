from car_skeleton import Electric_Car as EV, Battery as B

Tesla = EV('Tesla', 'S', 2016, 56)

print(Tesla.get_descriptive_name())

Tesla.odometer_reading = 23

Tesla.start_car('key')

Tesla.read_odometer()

Tesla.battery_size.print_battery_details('Tesla')
Tesla.battery_size.print_range()
