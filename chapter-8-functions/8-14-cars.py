def car_details (model_name, manufacturer, **additional_details):
    additional_details["model_name"] = model_name
    additional_details["manufacturer"] = manufacturer
    return additional_details


car1 = car_details('800', 'Maruti_Suzuki', Color = 'white')
car2 = car_details('380', 'BMW', Price = 'Wayy to costly', color = 'pink')
car3 = car_details('R8', 'Audi')

print(car1)
print(car2)
print(car3)