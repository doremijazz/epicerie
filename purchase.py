class Achat:        #nouveau type d'objet

    #Quand on écrira achat = Achat(pomme, 2) Python fera product = pomme et quantity = 2
    def __init__(self, product, quantity):
        self.product = product      #donc contient tout l objet product, grace a ca on peut ecrire self.produit.price par ex
        self.quantity = quantity    #parce que le produit ne connait pas la quantite achetee mais juste son stock

#Chaque objet Achat sait déjà comment se présenter
    def __str__(self):      #Python affichera ce que tu retournes dans __str__ quand tu feras print(achat)
        return (
            f"{self.product.name} : "   #donne moi le nom du produit
            f"{self.quantity} {self.product.unit} - "  #quantite genre 2 et unit par ex kg
            f"{self.total_price():.2f} €"  #appelle la methode total_price et Le :.2f signifie afficher un nombre décimal avec 2 chiffres après la virgule
        )

#methode calcul achat
    def total_price(self):
        return self.product.price * self.quantity
    #cette methode ne sert pas a afficher mais a donner un resultat c est ensuite le client qui fera l affichage avec print(achat)

