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

def printmenu():
    print("\nO QUE DESEJA FAZER?")
    print("1. Adicionar um novo filme")  # Criar nova linha
    print("2. Mostrar todos os filmes")  # Mostrar todas as linhas
    print("3. Mostrar detalhes de filmes selecionados")  #Mostrar colunas escolhidas
    print("4. Filtrar filmes por critério")  #Mostrar linhas escolhidas por condição
    print("5. Atualizar informações de um filme")  #Atualizar uma linha existente
    print("6. Deletar um filme por critério")  #Deletar uma linha por condição
    print("7. Emprestar um filme")  #Emprestar filme
    print("8. Exibir número total de filmes cadastrados")  # Exibir número de filmes
    print("9. Sair do programa")  #Sair do programa

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
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        #Criar nova linha
        nomeFilme = treatTitle(input("Escreva o nome do filme: "))
        diretorFilme = treatDirector(input("Escreva o diretor do filme: "))
        generoFilme = treatGenre(input("Escreva o genero do filme: "))
        anoFilme = treatYear(input("Escreva o ano do filme: "))
        classificacaoFilme = treatRating(input("Escreva a classificacao indicativa do filme: "))
        db.createRow(nomeFilme, diretorFilme, generoFilme, anoFilme, classificacaoFilme)

    elif escolha == '2':
        #Mostrar todas as linhas
        db.readAllRows()

    elif escolha == '3':
        #Mostrar colunas escolhidas
        colunas_escolhidas = input("Escolha as colunas para imprimir (separadas por vírgula, ex: nomeFilme, valorEmprestimo, emprestado, ano, quantidadeEmprestimo): ").split(",")
        colunas_escolhidas = [coluna.strip() for coluna in colunas_escolhidas]
        db.readColumns(colunas_escolhidas)

    elif escolha == '4':
        #Mostrar linhas escolhidas por condição
        condicaoLer = input("Digite a condição para selecionar as linhas: ")
        db.readRow(condicaoLer)

    elif escolha == '5':
        #Atualizar uma linha existente
        print("Escolha o id do Filme que você deseja atualizar:")
        db.readAllRows()
        idFilme = input("-> ")

        print("Atualizar nome? s/n")
        res = input()
        if res == "s":
            print("Digite o novo nome:")
            newname = input()
            if newname != '':
                db.updateName(idFilme,newname)
            else:
                print("Escreva um nome válido.")

        print("Atualizar ano? s/n")
        res = input()
        if res == "s":
            print("Digite o novo ano:")
            ano = input()
            if ano != '':
                db.updateYear(idFilme,ano)
            else:
                print("Escreva um ano válido.")

        print("Atualizar valor? s/n")
        res = input()
        if res == "s":
            print("Digite o novo valor de empréstimo:")
            valor = input()
            if valor != '':
                db.updateYear(idFilme,valor)
            else:
                print("Escreva um valor válido.")

        print("Atualizar valor de copias? s/n")
        res = input()
        if res == "s":
            print("Digite o novo valor de empréstimo:")
            valor = input()
            if valor != 0:
                db.updateCopies(idFilme,valor)
            else:
                print("Escreva um valor válido.")


    elif escolha == '6':
        #Deletar uma linha por condição
        condicaoDel = input("Digite a condição para deletar a linha escolhida: ")
        db.deleteRow(condicaoDel)

    elif escolha == '7':
        # Efetuar um emprestimo
        print("Escolha o nome do Filme que você deseja emprestar:")
        db.readAllRows()
        nomeFilme = input("-> ")

        db.updateRent(nomeFilme)

    elif escolha == '9':
        # Exibir numero de filmes cadastrados

        db.getTotalFilms()
        break

    elif escolha == '8':
        #Sair do programa
        cursor.close()
        conexao.close()
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
