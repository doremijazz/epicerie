def is_in_stock(product, achat):
    return product.stock >= achat.stock


def buy_product(product, achat, client):
    product.buy(achat)
    client.buy(achat)


def sell_product(product, achat, client):
    if is_in_stock(product, achat):
        buy_product(product, achat, client)

def user_input():
    pass