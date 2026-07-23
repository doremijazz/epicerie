class Achat:        #nouveau type d'objet

    #Quand on écrira achat = Achat(pomme, 2) Python fera product = pomme et quantity = 2
    def __init__(self, product, quantity):
        self.product = product      #donc contient tout l objet product, grace a ca on peut ecrire self.produit.price par ex
        self.quantity = quantity    #parce que le produit ne connait pas la quantite achetee mais juste son stock

    def __str__(self):
        return (
            f"{self.product.name} : "
            f"{self.quantity} {self.product.unit} - "
            f"{self.total_price():.2f} €"
        )

#methode calcul achat
    def total_price(self):
        return self.product.price * self.quantity
    #cette methode ne sert pas a afficher mais a donner un resultat c est ensuite le client qui fera l affichage avec print(achat)

