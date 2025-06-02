class Restaurant():
    """This is a sample restaurant located in Europe"""
    def __init__(self, restaurant_name, cuisine):
        self.name= restaurant_name
        self.cuisine = cuisine
        self.cust=0
    def print_details(self):
        print(f"The restaurant's name is {self.name}\nThe restaurant serves {self.cuisine} dishes")

    def open(self, status):
        if status == 'y' or status == 'Y':
            print(f"The restaurant is open")
        
        else:
            print(f"The restaurant is closed")
    
    def number_of_customers_served(self):
        print(f'{self.cust} customers served so far...')

    def increment_cust(self):
        self.cust += 1
        print(f'{self.cust} customers served so far...')

class Icecream(Restaurant):
    """This is a simple ice cream stand located in the restaurant""" 
    def __init__(self, restaurant_name, cuisine):
        """ a method to initialize the values of Icecream stand by inheriting the parent"""
        super().__init__(restaurant_name, cuisine)
        self.cuisine = 'dessert'
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def print_menu(self):
        """print the flavors in the menu of our restaurant"""
        for i in self.flavors:
            print(i)
    
    

linguini = Restaurant('linguini', 'french')
linguini.cust = 100
linguini.increment_cust()
linguini.open('y')
linguini.print_details()
linguini.number_of_customers_served()
   
linguini_ice_cream = Icecream('linguini', 'dessert')
linguini_ice_cream.print_menu()

