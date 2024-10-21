from Locadora import *
from menu_functions import *

class Cart:
    def __init__(self):
        self.items = {}
        print('Carrinho vazio')

    def add_item(self, product):
        filmes = input("Digite os títulos dos filmes que deseja adicionar ao carrinho, separados por vírgulas: ").split(",")
        filmes = [treatTitle(filme.strip()) for filme in filmes]

        for filme in filmes:
            resultado = db.readRowByTitle(filme):
            if resultado is None:
                newline()
                print(f"Filme com nome {filme} não existe no banco de dados.")



    def remove_item(self, code):
        if code in self.items:
            del self.items[code]

    def get_total_price(self):
        return sum(item['total_price'] for item in self.items.values())

    def finish_buy(self):
        # Implement your logic for finishing the purchase here
        # For example, you could create an order in the database
        print("Purchase completed!")
        self.items = {}  # Clear the cart

# Example usage
cart = Cart()

product1 = {'code': 1, 'name': 'Product 1', 'price': 10.0}
product2 = {'code': 2, 'name': 'Product 2', 'price': 20.0}

cart.add_item(product1)
cart.add_item(product2)
cart.add_item(product1)  # Add another instance of product 1

print("Total price:", cart.get_total_price())

cart.finish_buy()