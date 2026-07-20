class Produc:
    def __init__(self, name, type, stock, price):
        self.name = name
        self.type = type
        self.stock = stock
        self.price = price
        
    def buy(self, achat):
        self.stock -= achat.stock