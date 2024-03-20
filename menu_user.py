#Importe das funções de cada operação do CRUD
from index import conexaoBanco
from createOperations import createRow
from readOperations import readAllRows, readColumns, readRow
from updateOperations import updateRow
from deleteOperations import deleteRow

conexao, cursor = conexaoBanco()

#FUNÇÃO DE EXIBIÇÃO DO MENU
def menu():
    print("\nO QUE DESEJA FAZER?")
    print("1. Criar nova linha")
    print("2. Mostrar todas as linhas")
    print("3. Mostrar colunas escolhidas")
    print("4. Mostrar linhas escolhidas por condição")
    print("5. Atualizar uma linha existente")
    print("6. Deletar uma linha por condição")
    print("7. Sair do programa")

#LOOP para exibição do menu 
while True:
    menu()  #Exibe o menu
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        #Criar nova linha
        nomeFilme = input("Escreva o nome do filme: ")
        anoFilme = input("Escreva o ano do filme: ")
        createRow(nomeFilme, anoFilme)

    elif escolha == '2':
        #Mostrar todas as linhas
        readAllRows()

    elif escolha == '3':
        #Mostrar colunas escolhidas
        colunas_escolhidas = input("Escolha as colunas para imprimir (separadas por vírgula, ex: nomeFilme, valorEmprestimo, emprestado, ano, quantidadeEmprestimo): ").split(",")
        colunas_escolhidas = [coluna.strip() for coluna in colunas_escolhidas]
        readColumns(colunas_escolhidas)

    elif escolha == '4':
        #Mostrar linhas escolhidas por condição
        condicaoLer = input("Digite a condição para selecionar as linhas: ")
        readRow(condicaoLer)

    elif escolha == '5':
        #Atualizar uma linha existente
        print("Escolha o id do Filme que você deseja atualizar:")
        readAllRows()
        idFilme = input("-> ")
        updateRow(idFilme)

    elif escolha == '6':
        #Deletar uma linha por condição
        condicaoDel = input("Digite a condição para deletar a linha escolhida: ")
        deleteRow(condicaoDel)

    elif escolha == '7':
        #Sair do programa
        cursor.close()
        conexao.close()
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")