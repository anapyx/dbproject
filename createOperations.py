from index import conexaoBanco

conexao, cursor = conexaoBanco()

# CREATE
nome_filme = "Titanic"
valor_emprestimo = 10
emprestado = 0
ano = 1997
quantidade_emprestimo = 0
comando = f'INSERT INTO vendas (nomeFilme, valorEmprestimo, emprestado, ano, quantidadeEmprestimo) VALUES ("{nome_filme}", {valor_emprestimo}, {emprestado}, {ano}, {quantidade_emprestimo})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados
cursor.close()
conexao.close()