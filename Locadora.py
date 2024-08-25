import random
from index import conexaoBanco

conexao, cursor = conexaoBanco()

class Locadora:
    def __init__(self):
        self.totalFilms = None

    def getTotalFilms(self):
        temp = cursor.fetchall()
        self.totalFilms = len(temp)
        print(self.totalFilms)

    #CRIAÇÃO DE UMA LINHA na tabela 'filmes'(id, titulo, diretor, genero, ano, classificacao,
    # valor, vendidos)
    def createRow(self, tituloFilme, diretorFilme, geneneroFilme, anoFilme, classificaoFilme):
        titulo = tituloFilme
        diretor = diretorFilme
        genero = geneneroFilme
        ano = anoFilme
        classificao = classificaoFilme
        listaValores = [19.90, 24.90, 29.90, 34.90, 39.90]
        if ano >= 2023:
            valor = 44.90
        else:
            valor = random.choice(listaValores)
        vendidos = 0

        comandoCriar = f'INSERT INTO filmes (titulo, diretor, genero, ano, classificao, valor, vendidos) VALUES ("{titulo}", "{diretor}", "{genero}", {ano}, "{classificao}", {valor}, {vendidos})'
        cursor.execute(comandoCriar)

        conexao.commit()

    def deleteRow(self, condicaoDel):
        comandoDeletar = f'DELETE FROM filmes WHERE {condicaoDel}'
        cursor.execute(comandoDeletar)
        conexao.commit()

    #SELEÇÃO DE TODAS AS LINHAS
    def readAllRows(self):
        comandoLerLinhas = f'SELECT * from filmes'
        cursor.execute(comandoLerLinhas)
        resultado = cursor.fetchall()

        print(resultado)

    #PROJEÇÃO DAS COLUNAS
    def readColumns(self, colunas):
        comandoLerColuna = f"SELECT {', '.join(colunas)} from filmes"
        cursor.execute(comandoLerColuna)
        resultados = cursor.fetchall()
        for resultado in resultados:
            for valor in resultado:
                print(valor, end="\t")
            print()

    #SELEÇÃO DE LINHAS POR CONDIÇÃO
    def readRow(self, condicaoLinha):
        comandoLer = f'SELECT * from filmes WHERE {condicaoLinha}'
        cursor.execute(comandoLer)
        resultado = cursor.fetchall()
        print(resultado)

    #ATUALIZAÇÃO DA COLUNA nomeFilme DE UMA LINHA DA TABELA

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def updateTitulo(self,id, titulo):
        comandoAtualizar = f'UPDATE filmes SET titulo = "{titulo}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    #ATUALIZAÇÃO DA COLUNA ano DE UMA LINHA DA TABELA
    def updateYear(self,id, ano):
        comandoAtualizar = f'UPDATE filmes SET ano = "{ano}" WHERE idFilmes = {id}'
        
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