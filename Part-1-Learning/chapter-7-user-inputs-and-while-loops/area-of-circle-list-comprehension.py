number = int(input('Enter the number till which areas must be calculated\n'))

areas = [(radii**2)*3.14 for radii in range (number)]

for idx, value in enumerate(areas):
    print(f'Area of cicle with radius {idx} = {value}')