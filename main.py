from login import *
from menu_functions import *

def display_menu(is_logged_in, user_role):
    printMenu()
    if is_logged_in:
        if user_role == True:
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

is_logged_in = False
user_role = False

while True:
    inicio()
    display_menu(is_logged_in, user_role)
    choice = input("Enter your choice: ")

    if choice == "1":
        showFilms()

    elif choice == "2":
        if is_logged_in and user_role:
            # Para admin
            pass
        elif is_logged_in and not user_role:
            # Para usuário
            pass
        else:
            # Para usuário não logado
            print("~ 2. Fazer login ~")
            username = input("Insira seu nome de usuário: ")
            password = input("Insira sua senha: ")
            is_logged_in = getLogin(username, password)
            if is_logged_in == True:
                user_role = getUserRole(username)

    elif choice == "3":
        if is_logged_in and user_role == True:
            pass
        else:
            # Para usuário não logado
            print("~ 3. Registrar-se ~")
            printRegisterMenu()

    elif choice == 'sair':
        cursor.close()
        conexao.close()
        print("Saindo...")
        break        
    # ... other actions
