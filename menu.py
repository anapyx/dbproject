#Importe das funções de cada operação do CRUD
from Locadora import *

#FUNÇÃO DE EXIBIÇÃO DO MENU
def printmenu():
    print("\nO QUE DESEJA FAZER?")
    print("1. Criar nova linha")
    print("2. Mostrar todas as linhas")
    print("3. Mostrar colunas escolhidas")
    print("4. Mostrar linhas escolhidas por condição")
    print("5. Atualizar uma linha existente")
    print("6. Deletar uma linha por condição")
    print("7. Emprestar filme")
    print("8. Sair do programa")


print("\n-------- LOCADORA ---------")

db = Locadora()

#LOOP para exibição do menu 
while True:
    printmenu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        #Criar nova linha
        nomeFilme = input("Escreva o nome do filme: ")
        anoFilme = input("Escreva o ano do filme: ")
        db.createRow(nomeFilme, anoFilme)

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


    elif escolha == '6':
        #Deletar uma linha por condição
        condicaoDel = input("Digite a condição para deletar a linha escolhida: ")
        db.deleteRow(condicaoDel)

    elif escolha == '7':
        # Efetuar um emprestimo
        print("Escolha o id do Filme que você deseja emprestar:")
        db.readAllRows()
        idFilme = input("-> ")

        db.updateRent(idFilme)

    elif escolha == '9':
        # Exibir numero de filmes cadastrados

        db.getTotalFilms()
        break

    elif escolha == '8':
        #Sair do programa
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
