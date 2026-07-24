import display
from client import Client
from product import Product
from purchase import Achat

def is_in_stock(product, achat):
    return product.stock >= achat.quantity  #ex : stock 8kg quantite demandee 2kg, 8 >= 2 True donc vente possible


def buy_product(product, achat, client):
    product.buy(achat)

    client.buy(achat, client)

    client.buy(achat, client)


def sell_product(product, achat, client):
    if is_in_stock(product, achat):
        buy_product(product, achat, client)

        print("Achat ajouté au panier.")

    else:

        print("Stock insuffisant.")


def main(products):
    clientel = []
    while True:
        client = start_input()

        if client is None:  #Il n'y a pas de nouveau client, la journée est terminée
            display.assessment(clientel)
            break

        while True:  #boucle du panier
            display.catalogue(products)
            achat = user_input(products)

            if achat is None:
                display.ticket(client)
                clientel.append(client)
                break

            sell_product(achat.product, achat, client)

            #clientel.append(client)


#pour gérer l'arrivée d'un client le programme demande nom et prenom
#La fonction représente l'interaction avec l'utilisateur

def start_input():         #creer une fonction sans parametre car elle recup les info direct avec l'input

    choix = input(
        "1 - Nouveau client\n"
        "2 - Terminer la journée\n"
        "Votre choix : "
    )

    if choix == "2":
        return None 
    
    name = input("Nom du client : ")

    surname = input("Prénom du client : ")

    client = Client(name, surname)  #On appelle le constructeur de la classe Client

    return client  #la fonction doit donner le client au programme principal sinon l objet n existe que dans la fonction


#fonction qui demande ce que le client veut acheter
#trouve le produit correspondant
#demande la quantite
#retourne un objet Achat
def user_input(products):  #on a besoin de connaitre la liste des produits disponibles

    choix = input(
        "1 - Ajouter un produit\n"
        "2 - Terminer mes achats\n"
        "Votre choix : "
    )

    if choix == "2":
        return None

    product_name = input(
        "Produit souhaité : ")  #recherche dans une liste d'objets, ex pomme on retrouve ses attributs dans product

    #Cherche dans la liste products le produit dont le nom correspond à ce que le client a écrit. Si tu le trouves, mets-le dans product. Sinon, mets None.4
    # product = Je vais stocker le résultat de ma recherche dans une variable appelée product
    product = next(
        (p for p in products if p.name.lower() == product_name.lower()),
        #On teste chaque produit en mettant toutes les lettres en petit
        None
    )
    #boucle écrite à l'envers, premier tour p = Product("Pomme") puis 2eme ("Orange), etc
    #products c est la liste du magasin
    #"Pour chaque élément de la liste products, je vais l'appeler temporairement p."
    #"Donne-moi le produit p seulement si la condition est vraie."
    #next c'est comme un break dans une boucle classique, ca donne le premier element trouvé et arrete la recherche

    if product is None:  #Si tu ne trouves rien, retourne None et ecris ce produit n existe pas
        print("Ce produit n'existe pas.")
        return None

    quantity = float(input(
        "Quantité souhaitée : "))  #float transforme le texte en nombre car dans l input 2 est une chaine de caractere pas un nombre et qu'il faut accepter les nombres avec virgule (ex : 1,7 kg)

    achat = Achat(product,
                  quantity)  #Avant un avait product et quantity separés, maintenant on fabrique : Achat(product, quantity) donc Python appelle classe Achat
    #Python cree une variable locale et quand la fonction arrive à la fin, Python va supprimer ce qu'il y avait dans cette boîte
    #donc si on ne fait rien le programme crée l'achat puis le perd c est pour ca qu'on fait un return


    return achat  #la fonction doit donner le resultat a qq un et c est logique que ca soit a Achat
    #achat = user_input(products)

    return achat   #la fonction doit donner le resultat a qq un et c est logique que ca soit a Achat
                   #achat = user_input(products)

