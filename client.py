class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.ticket = []
        
        
    def __str__(self):
        for elem in self.ticket:
            print(
                f"{elem.name} : {etem.stock} {elem.unit}, "
                f"{elem.price:.2f} €/{elem.unit}"
            )

    def buy(self, achat, client):
        self.ticket.append(achat)