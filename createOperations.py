from index import conexaoBanco

conexao, cursor = conexaoBanco()

# CREATE

def createRow(filme, anoFilme):
    nome_filme = filme
    valor_emprestimo = 10
    emprestado = 0
    ano = anoFilme
    quantidade_emprestimo = 0
    comandoCriar = f'INSERT INTO vendas (nomeFilme, valorEmprestimo, emprestado, ano, quantidadeEmprestimo) VALUES ("{nome_filme}", {valor_emprestimo}, {emprestado}, {ano}, {quantidade_emprestimo})'
    cursor.execute(comandoCriar)
    conexao.commit() # edita o banco de dados
    # cursor.close()
    # conexao.close()