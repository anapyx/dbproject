import mysql.connector
from index import conexaoBanco

conexao, cursor = conexaoBanco()

class Locadora:
    def __init__(self, ):
        self.totalFilms = None

    
    def createRow(filme, anoFilme):
        nome_filme = filme
        valor_emprestimo = 10
        emprestado = 0
        ano = anoFilme
        quantidade_emprestimo = 0
        comandoCriar = f'INSERT INTO vendas (nomeFilme, valorEmprestimo, emprestado, ano, quantidadeEmprestimo) VALUES ("{nome_filme}", {valor_emprestimo}, {emprestado}, {ano}, {quantidade_emprestimo})'
        cursor.execute(comandoCriar)

        conexao.commit()
        cursor.close()
        conexao.close()

    def deleteRow(condicaoDel):
        comandoDeletar = f'DELETE FROM vendas WHERE {condicaoDel}'
        cursor.execute(comandoDeletar)
        conexao.commit()

        cursor.close()
        conexao.close()


    def readAllRows():
        comandoLerLinhas = f'SELECT * from vendas'
        cursor.execute(comandoLerLinhas)
        resultado = cursor.fetchall()
        print(resultado)

        cursor.close()
        conexao.close()

    #ler colunas escolhidas
    def readColumns(colunas):
        comandoLerColuna = f"SELECT {', '.join(colunas)} from vendas"
        cursor.execute(comandoLerColuna)
        resultados = cursor.fetchall()
        for resultado in resultados:
            for valor in resultado:
                print(valor, end="\t")
            print()

        cursor.close()
        conexao.close()

    #ler linhas escolhidas por condição
    def readRow(condicaoLinha):
        comandoLer = f'SELECT * from vendas WHERE {condicaoLinha}'
        cursor.execute(comandoLer)
        resultado = cursor.fetchall()
        print(resultado)

        cursor.close()
        conexao.close()