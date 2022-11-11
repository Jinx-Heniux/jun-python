class Good():

    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        return self.original_price * self.discount

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

obj = Good()
print(f"the new price is: {obj.price}")
obj.price = 200
print(f"the new price is: {obj.price}")
del obj.price
