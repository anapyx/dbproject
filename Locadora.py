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
        comandoLerTodosFilmes = "SELECT * FROM filmes"
        cursor.execute(comandoLerTodosFilmes)  # Executa a consulta para selecionar todos os filmes
        temp = cursor.fetchall()  # Busca todos os registros da consulta
        self.totalFilms = len(temp)  # Define o total de filmes com o número de registros encontrados
        print(self.totalFilms)

    def getTotalSoldFilms(self):
        # Consulta SQL para somar todos os valores da coluna 'vendidos'
        comandoSomarVendidos = "SELECT SUM(vendidos) FROM filmes"
        cursor.execute(comandoSomarVendidos)  # Executa a consulta
        total_vendidos = cursor.fetchone()[0]  # Obtém o resultado da soma

        # Se não houver filmes na tabela, o resultado pode ser None, então convertemos para 0
        if total_vendidos is None:
            total_vendidos = 0

        print(total_vendidos) # Retorna o total de filmes vendidos


    #CRIAÇÃO DE UMA LINHA na tabela 'filmes'(id, titulo, diretor, genero, ano, classificacao,
    # valor, vendidos)
    def createRow(self, tituloFilme, diretorFilme, generoFilme, anoFilme, classificaoFilme):
        # Verifica se o filme já existe na tabela 'filmes'
        comandoVerificar = f'SELECT COUNT(*) FROM filmes WHERE titulo = %s AND diretor = %s AND ano = %s'
        cursor.execute(comandoVerificar, (tituloFilme, diretorFilme, anoFilme)) 
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
        colunas_permitidas = ["titulo", "diretor", "genero", "ano", "classificacao"] 
        if not any(coluna in condicaoDel for coluna in colunas_permitidas):
            print("Condição de deleção inválida. Use apenas colunas permitidas.")
            return

        comandoDeletar = f'DELETE FROM filmes WHERE {condicaoDel}'
        cursor.execute(comandoDeletar)
        conexao.commit()

    def deleteRowById(self, idFilme):
        comandoDeletar = "DELETE FROM filmes WHERE id = %s"
        cursor.execute(comandoDeletar, (idFilme,)) 
        conexao.commit()
        resultado = cursor.fetchone()  # Obtém o primeiro resultado, se existir
        return resultado

    def deleteRowByTitle(self, titulo):
        comandoDeletar = "DELETE FROM filmes WHERE titulo = %s"
        cursor.execute(comandoDeletar, (titulo,))
        conexao.commit()
        resultado = cursor.fetchone()  # Obtém o primeiro resultado, se existir
        return resultado

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
        colunas_permitidas = ["titulo", "diretor", "genero", "ano", "classificacao", "valor"]
        condicao_coluna = condicaoLinha.lower().split('=')[0].strip()  # Extrai a coluna da condição

        if condicao_coluna not in colunas_permitidas:
            print("Condição de leitura inválida. Use apenas colunas permitidas.")
            return
        elif condicao_coluna == "valor":
            valueInserted = condicaoLinha.split('=')[1].strip()
            condicaoLinha = f"{condicao_coluna} = Cast({valueInserted} AS FLOAT)"

        comandoLer = f'SELECT * from filmes WHERE {condicaoLinha}'
        cursor.execute(comandoLer)

        resultado = cursor.fetchall()
        for row in resultado:
            print(row)

    def readRowById(self, idFilme):
        # Consulta SQL para verificar se o filme existe com o ID fornecido
        comandoVerificar = "SELECT * FROM filmes WHERE id = %s"
        cursor.execute(comandoVerificar, (idFilme,))
        resultado = cursor.fetchone()  # Obtém o primeiro resultado, se existir
        return resultado
    
    def readRowByTitle(self, titulo):
        # Consulta SQL para verificar se o filme existe com o ID fornecido
        comandoVerificar = "SELECT * FROM filmes WHERE titulo = %s"
        cursor.execute(comandoVerificar, (titulo,))
        resultado = cursor.fetchone()  # Obtém o primeiro resultado, se existir
        return resultado

    # Atualização de valores da tabela Filmes
    def updateTitle(self,id, titulo):
        comandoAtualizar = 'UPDATE filmes SET titulo = %s WHERE id = %s'
        cursor.execute(comandoAtualizar, (titulo, id))
        conexao.commit()

    def updateDirector(self,id, diretor):
        comandoAtualizar = 'UPDATE filmes SET diretor = %s WHERE id = %s'
        cursor.execute(comandoAtualizar, (diretor, id))
        conexao.commit()

    def updateGenre(self,id, genero):
        comandoAtualizar = 'UPDATE filmes SET genero = %s WHERE id = %s'
        
        cursor.execute(comandoAtualizar, (genero, id))
        conexao.commit()

    def updateYear(self,id, ano):
        comandoAtualizar = 'UPDATE filmes SET ano = %s WHERE id = %s'
        
        cursor.execute(comandoAtualizar, (ano, id))
        conexao.commit()

    def updateRating(self,id, classificacao):
        comandoAtualizar = 'UPDATE filmes SET classificacao = %s WHERE id = %s'
        
        cursor.execute(comandoAtualizar, (classificacao, id))
        conexao.commit()

    # Atualizar valor de compra do Filme
    def updateValue(self,id, valor):
        comandoAtualizar = 'UPDATE filmes SET valor = %s WHERE id = %s'
        
        cursor.execute(comandoAtualizar, (valor, id))
        conexao.commit()

    # Atualizar número de vendas
    def updateSold(self,id, vendidos):
        comandoAtualizar = 'UPDATE filmes SET vendidos = %s WHERE id = %s'
        
        cursor.execute(comandoAtualizar, (vendidos, id))
        conexao.commit()

    # Preencher tabela de relatorio
    def fillReport(self):
        cursor.callproc('PreencherRelatorio')
        conexao.commit()
        # fazer try catch para verificar se a procedure foi executada com sucesso