alien={}

features=['color', 'points', 'x_position', 'y_position']
values=['green', 5, 0, 25]

for number in range(len(features)):
    alien[features[number]]=values[number]

print(alien)
