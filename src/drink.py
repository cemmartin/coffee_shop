class Drink:
    def __init__(self, input_drink_name, input_drink_price):
        self.drink_name = input_drink_name
        self.drink_price = input_drink_price
        
    def give_drink_price(self, input_drink_name):
        input_drink_price = input_drink_name[1]
        return input_drink_price
        # input: drink name, output drink price

