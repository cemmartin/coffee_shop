from src.customer import Customer
from src.drink import Drink

class CoffeeShop:
    def __init__(self, input_name, input_till, input_list_of_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_list_of_drinks
        

    def increase_till(self, input_amount):
        self.till += input_amount #till is now equal to og value plus new value
    
    def sell_drink_to_customer(self,input_customer, input_drink):
        input_customer.buy_drink(input_drink) #how would you acces
        self.increase_till(input_drink.drink_price)
        #could you maybe do this with an if statement?
        
