class Restaurant():
    """This is a sample restaurant located in Europe"""
    def __init__(self, restaurant_name, cuisine):
        self.name = restaurant_name
        self.cuisine = cuisine
        self.cust = 0
    def print_details(self):
        """This method prints the details about the restaurant"""
        print(f"The restaurant's name is {self.name}\nThe restaurant serves {self.cuisine} dishes")

    def open(self, status):
        """A simple menthod used to print if the restaurant is open or not"""
        if status == 'y' or status == 'Y':
            print(f"The restaurant is open")
        
        else:
            print(f"The restaurant is closed")
    
    def number_of_customers_served(self):
        """A simple method which prints the number of customers served so far"""
        print(f'{self.cust} customers served so far...')

    def increment_cust(self):
        """A simple method used to increment the number of customers served by 1"""
        self.cust += 1
        print(f'Number of customers served has been successfully incremented by 1')

    def set_number_cust_served(self, value):
        """ A simple method used to set the number of customers served by the restaurant"""
        self.cust = value
        print(f'The number of customers served by the restaurant has been successfully set to {value}')

    

