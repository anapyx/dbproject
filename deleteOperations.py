from index import conexaoBanco

conexao, cursor = conexaoBanco()

#DELETE

nome_filme = "O Poderoso Chefão"
comando = f'DELETE FROM vendas WHERE nomeFilme = "{nome_filme}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()