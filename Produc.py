class Product:
    def __init__(self, name, type, stock, price):
        self.name = name
        self.type = type
        self.stock = stock
        self.price = price
        self.unit = unit

    def __str__(self):
        print(
            f"{self.name} : {self.stock} {self.unit}, "
            f"{self.price:.2f} €/{self.unit}"
        )
        
    def buy(self, achat):
        self.stock -= achat.stock