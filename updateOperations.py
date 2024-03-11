from index import conexaoBanco

conexao, cursor = conexaoBanco()

#UPDATE

nome_filme = "Titanic"
valor_emprestimo = 8

comando = f'UPDATE vendas SET valorEmprestimo = {valor_emprestimo} WHERE nomeFilme = "{nome_filme}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()