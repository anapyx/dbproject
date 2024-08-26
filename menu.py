#Importe das funções de cada operação do CRUD
from Locadora import *
import string
import re

# Funções de exibição do menu
def inicio():
    print("  _                                   _                        ")
    print(" | |                                 | |                       ")
    print(" | |        ___     ___    __ _    __| |   ___    _ __    __ _ ")
    print(" | |       / _ \   / __|  / _` |  / _` |  / _ \  | '__|  / _` |")
    print(" | |____  | (_) | | (__  | (_| | | (_| | | (_) | | |    | (_| |")
    print(" |______|  \___/   \___|  \__,_|  \__,_|  \___/  |_|     \__,_|")
    print("")

def newline():
    print("")

def printmenu():
    print(" _ _  _  _    ")
    print("| | |(/_| ||_|")
    print("\n  ~ Escolha uma operação: ~")
    print("1. Adicionar um novo filme")  # Criar nova linha
    print("2. Atualizar informações de filme existente")
    print("3. Mostrar colunas escolhidas dos filmes")  #Mostrar colunas escolhidas
    print("4. Filtrar filmes por critério")  # Mostrar linhas escolhidas por condição
    print("5. Exibir todos os filmes cadastrados") 
    print("6. Deletar um filme por critério")  # Deletar uma linha por condição
    print("7. Comprar um filme")
    print("8. Exibir número total de filmes cadastrados")
    print("9. Exibir número total de filmes vendidos")
    print("10. Sair do programa")

# Funções de tratamento de entrada
def treatTitle(entry) -> str:
    while True:
        if len(entry) > 0:
            return string.capwords(entry)
        else:
            print("[!] Insira um título válido.")
            entry = input("Escreva o nome do filme: ")

def treatDirector(entry):
    while True:
        if len(entry) > 3:
            return string.capwords(entry)
        else:
            print("[!] Insira um(a) diretor(a) válido.")
            entry = input("Escreva o nome do diretor: ")

def treatGenre(entry):
    while True:
        entry = re.sub('[^a-z]+','', entry.lower())
        if len(entry) >= 5:
            return string.capwords(entry)
        else:
            print("[!] Insira um gênero válido.")
            entry = input("Escreva o gênero: ")

def treatYear(entry):
    while True:
        entry = re.sub('[^0-9]+','', entry.lower())
        year = int(entry)
        if len(entry) == 4 and (year >= 1888 and year <= 2024):
            return year
        else:
            print("[!] Insira um ano válido.")
            entry = input("Escreva o ano do filme: ")

def treatRating(entry):
    ratings = {"10", "12", "14", "16", "18", "livre", "l"}
    while True:
        entry = re.sub('[^a-z0-9]+','', entry.lower())
        if entry in ratings:
            return entry.capitalize()
        else:
            print("[!] Insira uma classificação válida.")
            entry = input("Escreva a classificação indicativa: ")

db = Locadora()

inicio()

#LOOP para exibição do menu 
while True:
    printmenu()
    option = input("Escolha uma opção: ")

    if option == '1':
        # Criar nova linha na tabela FILMES
        newline()
        nomeFilme = treatTitle(input("Escreva o nome do filme: "))
        diretorFilme = treatDirector(input("Escreva o diretor do filme: "))
        generoFilme = treatGenre(input("Escreva o genero do filme: "))
        anoFilme = treatYear(input("Escreva o ano do filme: "))
        classificacaoFilme = treatRating(input("Escreva a classificacao indicativa do filme: "))

        db.createRow(nomeFilme, diretorFilme, generoFilme, anoFilme, classificacaoFilme)

    elif option == '2':
        # Atualizar uma linha existente
        print("Digite o id do filme que você deseja atualizar:")
        db.readAllRows()
        idFilme = int(input("-> "))

        print("AQUIIIII")
        print(idFilme)

        newline()
        print("Atualizar título? s/n")
        res = input()
        if res == "s":
            print("Digite o novo nome:")
            newname = treatTitle(input())
            db.updateTitle(idFilme, newname)

        newline()
        print("Atualizar ano? s/n")
        res = input()
        if res == "s":
            print("Digite o novo ano:")
            ano = treatYear(input())
            db.updateYear(idFilme, ano)

        newline()
        print("Atualizar diretor? s/n")
        res = input()
        if res == "s":
            print("Digite o novo diretor:")
            director = treatDirector(input())
            db.updateDirector(idFilme, director)
    
        newline()
        print("Atualizar gênero? s/n")
        res = input()
        if res == "s":
            print("Digite o novo gênero:")
            genre = treatGenre(input())
            db.updateGenre(idFilme, genre)

        newline()
        print("Atualizar classificação? s/n")
        res = input()
        if res == "s":
            print("Digite a nova classificação:")
            rating = treatRating(input())
            db.updateRating(idFilme, rating)

        newline()
        print("Atualizar valor? s/n")
        res = input()
        if res == "s":
            print("Digite o novo valor de compra:")
            valor = float(input())
            if valor > 0 and valor < 1000:
                db.updateValue(idFilme,valor)
            else:
                print("Escreva um valor válido.")

    elif option == '3':
        # Mostrar colunas escolhidas
        newline()
        colunas_escolhidas = input("Escolha as colunas para visualizar (separadas por vírgula, ex: nomeFilme, diretor, genero, ano): ").split(",")
        colunas_escolhidas = [coluna.strip() for coluna in colunas_escolhidas]
        db.readColumns(colunas_escolhidas)

    elif option == '4':
        # Mostrar linhas escolhidas por condição
        newline()
        condicaoLer = input("Digite a condição para busca de filmes: ")
        db.readRow(condicaoLer)

    elif option == '5':
        # Mostrar todas as linhas da tabela FILMES
        newline()
        db.readAllRows()
        # [!] formatar por linhas

    elif option == '6':
        # Deletar uma linha por condição
        newline()
        condicaoDel = input("Digite a condição para deletar a linha escolhida: ")
        db.deleteRow(condicaoDel)

    elif option == '7':
        # Efetuar uma compra
        newline()
        print("Escolha o filme que deseja comprar:")
        db.readAllRows()
        nomeFilme = input("-> ")

        db.updateSold(nomeFilme, 1)

    elif option == '8':
        # Exibir numero de filmes cadastrados
        newline()
        print("Total de filmes cadastrados:")
        db.getTotalFilms()
        break

    elif option == '9':
        # Exibir total de filmes vendidos
        newline()
        #db.readColumns()

    elif option == '10':
        #Sair do programa
        cursor.close()
        conexao.close()
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
