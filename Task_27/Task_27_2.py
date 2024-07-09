class Item:
    def __init__(self, name, price, quantity):
        self.name = name.title()
        self.price = price
        self.quantity = quantity

    def __getattr__(self, attr):
        return self.price * self.quantity

a = Item("книга", 50, 10)
print(a.name)
print(a.total)
