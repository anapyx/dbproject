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

    # Cria nova linha na tabela 'filmes'
        # Entradas: titulo, diretor, genero, ano, classificacao
        # Id gerado pelo banco e valor, vendidos pre definidos
    def createRow(self, tituloFilme, diretorFilme, generoFilme, anoFilme, classificaoFilme):
        titulo = tituloFilme
        diretor = diretorFilme
        genero = generoFilme
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

    # Deletar filme se alguma condição por coluna seja atendida
    def deleteRow(self, condicaoDel):
        comandoDeletar = f'DELETE FROM filmes WHERE {condicaoDel}'
        cursor.execute(comandoDeletar)
        conexao.commit()

    # Mostrar TODAS AS LINHAS
    def readAllRows(self):
        comandoLerLinhas = f'SELECT * from filmes'
        cursor.execute(comandoLerLinhas)
        resultado = cursor.fetchall()

        print(resultado)

    # Mostra colunas da tabela Filmes
    def readColumns(self, colunas):
        comandoLerColuna = f"SELECT {', '.join(colunas)} from filmes"
        cursor.execute(comandoLerColuna)
        resultados = cursor.fetchall()
        for resultado in resultados:
            for valor in resultado:
                print(valor, end="\t")
            print()

    # Mostra linhas da tabela Filmes por condição
    def readRow(self, condicaoLinha):
        comandoLer = f'SELECT * from filmes WHERE {condicaoLinha}'
        cursor.execute(comandoLer)
        resultado = cursor.fetchall()
        print(resultado)

    # Atualização de valores da tabela Filmes
    def updateTitle(self,id, titulo):
        comandoAtualizar = f'UPDATE filmes SET titulo = "{titulo}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateDirector(self,id, diretor):
        comandoAtualizar = f'UPDATE filmes SET diretor = "{diretor}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateGenre(self,id, genero):
        comandoAtualizar = f'UPDATE filmes SET genero = "{genero}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateYear(self,id, ano):
        comandoAtualizar = f'UPDATE filmes SET ano = "{ano}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateRating(self,id, classificacao):
        comandoAtualizar = f'UPDATE filmes SET classificacao = "{classificacao}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    # Atualizar valor de compra do Filme
    def updateValue(self,id, valor):
        comandoAtualizar = f'UPDATE filmes SET valor = "{valor}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    # Atualizar número de vendas
    def updateSold(self,id, valor):
        comandoAtualizar = f'UPDATE filmes SET vendidos = "{vendidos}" WHERE idFilmes = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

