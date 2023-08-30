from src.drink import Drink

class Customer:
    def __init__(self, input_customer_name, input_wallet):
        self.customer_name = input_customer_name
        self.wallet = input_wallet

    def reduce_wallet(self, input_amount): #should reduce wallet by specified amount
        self.wallet -= input_amount

    def buy_drink(self, input_drink): #don't need to add customer bc it's already in customer
        self.reduce_wallet(input_drink.drink_price)

