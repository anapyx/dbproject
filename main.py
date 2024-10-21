from login import *
from menu_functions import *
from Locadora import *

def display_menu(is_logged_in, admin):
    printMenu()
    if is_logged_in:
        if admin == True:
            print("Olá, Admin!")
            printAdminMenu()
        else:
            print("Olá, usuário!")
            printUserMenu()
    else:
        print("Não logado")
        print("1. Mostrar Catálogo")
        print("2. Fazer login")
        print("3. Registrar-se")
        print("4. Fechar programa")

is_logged_in = False
admin = False

while True:
    inicio()
    newline()
    display_menu(is_logged_in, admin)
    choice = input("Entre com sua escolha: ")

    if choice == "1":
        if admin:
            db.readAllRows()
        else:
            db.readAllRowsUser()

    elif choice == "2":
        if is_logged_in:
            newline()
            print("~2. Buscar filme por nome~")
            showFilmbyName()
        else:
            # Para usuário não logado
            print("~ 2. Fazer login ~")
            username = input("Insira seu nome de usuário: ")
            password = input("Insira sua senha: ")
            is_logged_in = getLogin(username, password)
            if is_logged_in == True:
                print("Logando...")
                admin = getUserRole(username)
                logged_user = username
                newline()

    elif choice == "3":
        if is_logged_in:
            newline()
            print("~3. Filtrar filmes~")
            # Faixa de preço, genero, Mari
        else:
            print("~ 3. Registrar-se ~")
            printRegisterMenu()

    elif choice == "4":
        if is_logged_in and admin:
            newline()
            print("~4. Listar Colunas Específicas~")
            showFilmColumns()
        elif is_logged_in and not admin:
            print("~4. Adicionar Filme ao Carrinho~")
            addtoCart()
            pass
        else:
            cursor.close()
            conexao.close()
            print("Saindo...")
            break      

    elif choice == "5":
        if is_logged_in and admin:
            newline()
            print("~5. Cadastrar Filme~")
            showAddFilm()

        elif is_logged_in and not admin:
            print("~5. Ver carrinho~")
            # ver carrinho
            pass
        else:
            print("Operação inválida.")

    elif choice == "6":
        if is_logged_in and admin:
            newline()
            print("~6. Atualizar Filme~")
            showUpdateFilmRow()

        elif is_logged_in and not admin:
            print("~6. Remover item do carrinho~")
            # remover
            pass
        else:
            print("Operação inválida.")

    elif choice == "7":
        if is_logged_in and admin:
            newline()
            print("~7. Deletar Filme~")
            showDeleteFilmRow()

        elif is_logged_in and not admin:
            print("~7. Efetuar compra~")
            # comprar atualizar tabela pedidos
            pass
        else:
            print("Operação inválida.")

    elif choice == "8":
        if is_logged_in and admin:
            newline()
            print("~8. Gerar Relatório~")
            # implementar relatório

        elif is_logged_in and not admin:
            print("~8. Meu perfil~")
            getUserInfo()
            pass
        else:
            print("Operação inválida.")

    elif choice == "9":
        if is_logged_in and admin:
            newline()
            print("~9. Minhas vendas~")
            # implementar relatório desse vendedor

        elif is_logged_in and not admin:
            print("~9. Meus pedidos~")
            # histórico de pedido desse usuário
            pass
        else:
            print("Operação inválida.")

    elif choice == 'sair':
        cursor.close()
        conexao.close()
        print("Saindo...")
        break        
    # ... other actions
