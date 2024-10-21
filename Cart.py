from Locadora import *
from menu_functions import *
from prettytable import PrettyTable

payment = ['pix', 'cartão', 'boleto', 'berries']

class Cart:
    def __init__(self):
        self.items = {}

    def _check_film_exists(self, title):
        resultado = db.readRowByTitle(title)
        if resultado is None:
            print(f"Filme com título {title} não existe no banco de dados.")
            return False
        return True

    def addItem(self, title):
        if self._check_film_exists(title):
            if title in self.items:
                print("Esse filme já foi adicionado ao seu carrinho.")
            else:
                price = db.readPriceByTitle(title)
                self.items[title] = {'nome': title, 'quantidade': 1, 'preco': price}  # Adicione outras informações do filme aqui
                print("Filme adicionado ao carrinho.")
                print(self.items[title])
            return True
        return False
    
    def getCart(self):
        if self.items == {}:
            print("Carrinho vazio.")
        else:
            table = PrettyTable(["Nome", "Preço", "Quantidade"])
            for title, item in self.items.items():
                table.add_row([item['nome'], item['preco'], item['quantidade'],])
            print(table)

    def removeItem(self, title):
        if title in self.items:
            del self.items[title]
            print("Item removido.")

    def get_total_price(self, user):
        total_price = 0
        for item in self.items.values():
            total_price += item['quantidade'] * item['preco']
        
        print(f"Preço total: {total_price}")
        discount = db.readUserDiscount(user)
        if discount == 1:
            discount_price = total_price*0.9
            print(f"Preço com desconto: {discount_price}")


    def get_total(self):
        total_price = 0
        for item in self.items.values():
            total_price += item['quantidade'] * item['preco']
        return total_price

    def finish_buy(self, user):
        method = input("Qual o método de pagamento? ")
        filmlist = []
        if method in payment:
            for title, item in self.items.items():
                stock = db.readStock(title)
                if stock >= item['quantidade']:
                    db.updateStock(title, stock - item['quantidade'])
                    filmlist.append(title)
                    print(f"Compra concluída para {title}")
                else:
                    print(f"Estoque insuficiente para {title}. Compra cancelada.")
                    return False  # Stop processing if there's not enough stock
            db.addCart(user, filmlist, self.get_total(), method)
            print("Compra concluída!")
            self.items = {}  # Clear the cart
            return True
        else:
            print("Método de pagamento inválido.")
            return False

