cars=['audi', 'subaru', 'maruti', 'bmw']
target='bmw'
for idx, car in enumerate(cars):
    if car==target:
        print(f'found my {target.upper()} at index {idx}')
    else:
        print(f'Found some other pesant car {car} at {idx}')