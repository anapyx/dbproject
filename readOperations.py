from index import conexaoBanco

conexao, cursor = conexaoBanco()

#READ
#ler todas as linhas
def readAllRows():
    comandoLerLinhas = f'SELECT * from vendas'
    cursor.execute(comandoLerLinhas)
    resultado = cursor.fetchall()
    print(resultado)

    # # cursor.close()
    # conexao.close()

#ler colunas escolhidas
def readColumns(colunas):
    comandoLerColuna = f"SELECT {', '.join(colunas)} from vendas"
    cursor.execute(comandoLerColuna)
    resultados = cursor.fetchall()
    for resultado in resultados:
        for valor in resultado:
            print(valor, end="\t")
        print()

    # cursor.close()
    # conexao.close()

#ler linhas escolhidas por condição
def readRow(condicaoLinha):
    comandoLer = f'SELECT * from vendas WHERE {condicaoLinha}'
    cursor.execute(comandoLer)
    resultado = cursor.fetchall()
    print(resultado)

    # cursor.close()
    # conexao.close()