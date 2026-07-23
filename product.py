class Product:
    def __init__(self, name, type, stock, price, unit):
        self.name = name
        self.type = type
        self.stock = stock
        self.price = price
        self.unit = unit

    def __str__(self):
        return (
            f"{self.name} : {self.stock} {self.unit}, "
            f"{self.price:.2f} €/{self.unit}"
        )

        #methode diminution de stock
    def buy(self, achat):
        self.stock -= achat.quantity