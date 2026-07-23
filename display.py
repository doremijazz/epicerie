#affichage
#ne contient que des fonctions qui affichent quelque chose à l'écran

def catalogue(products):
    for product in products:
        print(product)


def ticket(client):
    print(client)
    for achat in client.ticket :
        print(achat)
    print(client.total_price)


def assessment (clientel):
    total_price = 0
    for client in clientel:
        ticket(client)
        total_price += client.total_price
    print(total_price)