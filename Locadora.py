import mysql.connector
from index import conexaoBanco

conexao, cursor = conexaoBanco()

class Locadora:
    def __init__(self):
        self.totalFilms = None

    def getTotalFilms(self):
        temp = cursor.fetchall()
        self.totalFilms = len(temp)
        print(self.totalFilms)

    #CRIAÇÃO DE UMA LINHA(valorEmprestimo = 10, emprestado = 0
    # e quantidadeEmprestimo = 0 por default)
    def createRow(self, filme, anoFilme):
        nome_filme = filme
        valor_emprestimo = 10
        emprestado = 0
        ano = anoFilme
        quantidade_emprestimo = 0
        comandoCriar = f'INSERT INTO vendas (nomeFilme, valorEmprestimo, emprestado, ano, quantidadeEmprestimo) VALUES ("{nome_filme}", {valor_emprestimo}, {emprestado}, {ano}, {quantidade_emprestimo})'
        cursor.execute(comandoCriar)

        conexao.commit()

    def deleteRow(self, condicaoDel):
        comandoDeletar = f'DELETE FROM vendas WHERE {condicaoDel}'
        cursor.execute(comandoDeletar)
        conexao.commit()

    #SELEÇÃO DE TODAS AS LINHAS
    def readAllRows(self):
        comandoLerLinhas = f'SELECT * from vendas'
        cursor.execute(comandoLerLinhas)
        resultado = cursor.fetchall()

        print(resultado)

    #PROJEÇÃO DAS COLUNAS
    def readColumns(self, colunas):
        comandoLerColuna = f"SELECT {', '.join(colunas)} from vendas"
        cursor.execute(comandoLerColuna)
        resultados = cursor.fetchall()
        for resultado in resultados:
            for valor in resultado:
                print(valor, end="\t")
            print()

    #SELEÇÃO DE LINHAS POR CONDIÇÃO
    def readRow(self, condicaoLinha):
        comandoLer = f'SELECT * from vendas WHERE {condicaoLinha}'
        cursor.execute(comandoLer)
        resultado = cursor.fetchall()
        print(resultado)

    #ATUALIZAÇÃO DA COLUNA nomeFilme DE UMA LINHA DA TABELA
    def updateName(self,id, nome_filme):
        comandoAtualizar = f'UPDATE vendas SET nomeFilme = "{nome_filme}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    #ATUALIZAÇÃO DA COLUNA ano DE UMA LINHA DA TABELA
    def updateYear(self,id, ano_filme):
        comandoAtualizar = f'UPDATE vendas SET ano = "{ano_filme}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    #ATUALIZAÇÃO DA COLUNA valorEmprestimo DE UMA LINHA DA TABELA
    def updateValue(self,id, valor_filme):
        comandoAtualizar = f'UPDATE vendas SET valorEmprestimo = "{valor_filme}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    #ATUALIZAÇÃO DA COLUNA emprestado DE UMA LINHA DA TABELA
    def updateCopies(self,id, valor_emprestado):
        comandoAtualizar = f'UPDATE vendas SET emprestado = {valor_emprestado} WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    # FUNÇÃO EMPRESTAR FILME   
    def updateRent(self,filme):
        # ALTERAR valor para emprestado
        getEmprestadoComando = f'SELECT emprestado from vendas WHERE nomeFilme = "{filme}"'
        cursor.execute(getEmprestadoComando)
        getEmprestado = cursor.fetchone()
        valorEmprestado = getEmprestado[0]

        getValorEmprestimo = f'SELECT valorEmprestimo from vendas WHERE nomeFilme = "{filme}"'
        cursor.execute(getValorEmprestimo)
        getValorEmprestimo = cursor.fetchone()
        valorEmprestimo = getValorEmprestimo[0]

        getQuantidadeEmprestimo = f'SELECT quantidadeEmprestimo from vendas WHERE nomeFilme = "{filme}"'
        cursor.execute(getQuantidadeEmprestimo)
        getQuantEmprestimo = cursor.fetchone()
        valorQuantEmprestimo = getQuantEmprestimo[0]
        
        if(valorEmprestado <= 0):
            print("Não há mais cópias do filme escolhido no momento!")
            conexao.commit()
            return None
        else:
            emprestado = valorEmprestado - 1
            comandoAtualizar = f'UPDATE vendas SET emprestado = {emprestado}, quantidadeEmprestimo = {valorQuantEmprestimo + valorEmprestimo} WHERE nomeFilme = "{filme}"'
        
            cursor.execute(comandoAtualizar)
            conexao.commit()