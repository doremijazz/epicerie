class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.ticket = []
        self.total_price = 0
        
        
    def __str__(self):
        return (f'{self.name} - {self.surname}')

    def buy(self, achat, client):
        self.ticket.append(achat)
        self.total_price = achat.total_price(achat)