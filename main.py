import display


def is_in_stock(product, achat):
    return product.stock >= achat.stock


def buy_product(product, achat, client):
    product.buy(achat)
    client.buy(achat)


def sell_product(product, achat, client):
    if is_in_stock(product, achat):
        buy_product(product, achat, client)


def main(products):
    clientel = []
    while True:
        client = strat_input()

        if client == "stop":
            display.assessment(clientel)
            break

        while True:
            display.catalogue(products)
            achat = user_input()

            if achat == "stop":
                display.ticket(client)
                break

            produit = next(
                (p for p in products if p.name == achat.name),
                None
            )

            sell_product(product, achat, client)
            clientel.append(client)


def strat_input():
    pass


def user_input():
    pass
