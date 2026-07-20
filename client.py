class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.ticket = []

    def buy(self, achat, client):
        self.ticket.append(achat)