class Restaurant():
    """This is a sample restaurant located in Europe"""
    def __init__(self, restaurant_name, cuisine):
        self.name= restaurant_name
        self.cuisine = cuisine

    def print_details(self):
        print(f"The restaurant's name is {self.name}\nThe restaurant serves {self.cuisine} dishes")

    def open(self, status):
        if status == 'y' or status == 'Y':
            print(f"The restaurant {self.name} is open")
        
        else:
            print(f"The restaurant {self.name} is closed")  

linguini = Restaurant('linguini', 'french')

linguini.open('y')
linguini.print_details()


kamat = Restaurant('kamat', 'indian')
mcd = Restaurant('McDonalds', 'American')


kamat.open('n')
kamat.print_details()

mcd.open('y')
mcd.print_details()
