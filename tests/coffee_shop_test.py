import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self): #the code inside this setUp function will run before each of our tests; sometimes also called a 'before each'
        self.americano = Drink("Americano", 2)
        self.latte = Drink("Latte", 3)
        self.mocha = Drink("Mocha", 4)
        self.flat_white = Drink("Flat White", 3)
        self.tea = Drink("Tea", 2)
        self.chai = Drink("Chai", 3)
        self.london_fog = Drink("London Fog", 4)
        self.iced_coffee = Drink("Iced Coffee", 3)
        drinks = [self.americano, self.latte, self.mocha, self.flat_white, self.tea, self.chai, self.london_fog, self.iced_coffee]

        self.coffee_shop = CoffeeShop("Starbucks", 100, drinks) #has a name and a till
        self.customer = Customer("Sam", 101)

    def test_coffee_shop_has_name(self):
        self.assertEqual("Starbucks", self.coffee_shop.name) #basically saying: is "Starbucks" == self.coffee_Shop.name ?

    def test_increase_till(self):
        self.coffee_shop.increase_till(10) #one parameter bc till is already there, we just need the cash given to us
        self.assertEqual(110, self.coffee_shop.till)

    def test_reduce_wallet(self): #should decrease the money in the customer's wallet
        self.customer.reduce_wallet(5)
        self.assertEqual(96, self.customer.wallet) 

    def test_buy_drink(self):
        self.customer.buy_drink(self.chai)
        self.assertEqual(98, self.customer.wallet)

    def test_sell_drink_to_customer(self):
        self.coffee_shop.sell_drink_to_customer(self.customer, self.latte)
        self.assertEqual(98, self.customer.wallet)
        self.assertEqual(103, self.coffee_shop.till)
        

# MVP:
# A Coffee Shop should be able to sell a drink to a customer 
# and increase it's till by the price of Drink. Hint: Use a 
# Customer method you already have.