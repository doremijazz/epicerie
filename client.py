class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.ticket = []
        self.total_price = 0

    def __str__(self):          #Une méthode __str__ doit retourner une chaîne

        texte = f"Ticket de {self.name} {self.surname}\n"

        for achat in self.ticket:
            texte += str(achat) + "\n"

        texte += f"Total : {self.total_price():.2f} €"

        return texte

    def buy(self, achat, client):
        self.ticket.append(achat)
        self.total_price = achat.total_price(achat)

    def total_price(self):   #on est dans la classe Client donc self designe un client
        total = 0  #on va additionner plusieurs prix mais au début on n'a encore rien additionné

        for achat in self.ticket:    # regarder un par un tous les achats du client, le ticket est une liste
                                     # a chaque tour la variable achat change
            total += achat.calculate_prix()   #le total plus le nouvel achat qui utilise la methode de la classe Achat calculate_price pour avoir le prix d'un achat

        return total
        #Quand tous les achats ont été parcourus la methode repond un prix mais ne l'affiche pas, elle calcule juste et ces ailleurs qu on fera print.

    #si le client prend 2kg de pommes et 1kg d orange alors le ticket contient [Achat(Pomme,2), Achat(Orange,1)]