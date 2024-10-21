from login import *
from menu_functions import *

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
        showFilms()

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
                admin = getUserRole(username)
                logged_user = username

    elif choice == "3":
        if is_logged_in:
            newline()
            print("~3. Filtrar filmes~")
            # Faixa de preço, genero, Mari
        else:
            # Para usuário não logado
            print("~ 3. Registrar-se ~")
            printRegisterMenu()

    elif choice == "4":
        if is_logged_in and admin:
            newline()
            print("~4. Listar Colunas Específicas~")
            # listar filmes por colunas
        elif is_logged_in and not admin:
            print("~4. Adicionar Filme ao Carrinho~")
            # função carrinho
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

        elif is_logged_in and not admin:
            print("~6. Remover item do carrinho~")
            # remover
            pass
        else:
            # Para usuário não logado
            print("Operação inválida.")

    elif choice == "7":
        if is_logged_in and admin:
            newline()
            print("~7. Deletar Filme~")

        elif is_logged_in and not admin:
            print("~7. Efetuar compra~")
            pass
        else:
            # Para usuário não logado
            print("Operação inválida.")

    elif choice == 'sair':
        cursor.close()
        conexao.close()
        print("Saindo...")
        break        
    # ... other actions
