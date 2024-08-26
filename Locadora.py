import random
from index import conexaoBanco

conexao, cursor = conexaoBanco()

long_width = 60
medium_width = 45
small_width = 20
numbers_width = 6

class Locadora:
    def __init__(self):
        self.totalFilms = None

    def getTotalFilms(self):
        temp = cursor.fetchall()
        self.totalFilms = len(temp)
        print(self.totalFilms)

    #CRIAÇÃO DE UMA LINHA na tabela 'filmes'(id, titulo, diretor, genero, ano, classificacao,
    # valor, vendidos)
    def createRow(self, tituloFilme, diretorFilme, generoFilme, anoFilme, classificaoFilme):
        # Verifica se o filme já existe na tabela 'filmes'
        comandoVerificar = f'SELECT COUNT(*) FROM filmes WHERE titulo = "{tituloFilme}" AND diretor = "{diretorFilme}" AND ano = {anoFilme}'
        cursor.execute(comandoVerificar)
        resultado = cursor.fetchone()

        # Se o resultado for maior que 0, o filme já existe
        if resultado[0] > 0:
            print(f'O filme "{tituloFilme}" já existe no banco de dados.')
            return  # Saia da função sem inserir o filme

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

        comandoCriar = f'INSERT INTO filmes (titulo, diretor, genero, ano, classificacao, valor, vendidos) VALUES ("{titulo}", "{diretor}", "{genero}", {ano}, "{classificao}", {valor}, {vendidos})'
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
        result = cursor.fetchall()
        print(f"{' Id':<{numbers_width}}{' Titulo':<{long_width}} {' Diretor':<{medium_width}} {' Genero':<{small_width}} {' Year':<{numbers_width}}{' Classificacao':<{small_width}} {' Valor':>{numbers_width}} {' Vendidos':>{numbers_width}}")
        print("-" * 190)  # Separator line
        for row in result:
            id, titulo, diretor, genero, ano, classificacao, valor, vendidos = row 
            print(f"{id:<{numbers_width}} {titulo:<{long_width}} {diretor:<{medium_width}} {genero:<{small_width}} {ano:<{numbers_width}}{classificacao:<{small_width}} {valor:>{numbers_width}.2f} {vendidos:>{numbers_width}}") 

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
        comandoAtualizar = f'UPDATE filmes SET titulo = "{titulo}" WHERE id = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateDirector(self,id, diretor):
        comandoAtualizar = f'UPDATE filmes SET diretor = "{diretor}" WHERE id = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateGenre(self,id, genero):
        comandoAtualizar = f'UPDATE filmes SET genero = "{genero}" WHERE id = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateYear(self,id, ano):
        comandoAtualizar = f'UPDATE filmes SET ano = "{ano}" WHERE id = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    def updateRating(self,id, classificacao):
        comandoAtualizar = f'UPDATE filmes SET classificacao = "{classificacao}" WHERE id = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    # Atualizar valor de compra do Filme
    def updateValue(self,id, valor):
        comandoAtualizar = f'UPDATE filmes SET valor = "{valor}" WHERE id = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

    # Atualizar número de vendas
    def updateSold(self,id, vendidos):
        comandoAtualizar = f'UPDATE filmes SET vendidos = "{vendidos}" WHERE id = {id}'
        
        cursor.execute(comandoAtualizar)
        conexao.commit()

