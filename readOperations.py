from index import conexaoBanco

conexao, cursor = conexaoBanco()

#READ

comando = f'SELECT * from vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()