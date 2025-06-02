from restaurant import *

linguini = Restaurant('linguini', 'french')
linguini.print_details()
linguini.open('y')
linguini.number_of_customers_served()
linguini.set_number_cust_served(100) 
linguini.number_of_customers_served()
linguini.increment_cust()
linguini.number_of_customers_served()

