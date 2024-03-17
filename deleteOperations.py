from index import conexaoBanco

conexao, cursor = conexaoBanco()

#DELETE
def deleteRow(condicaoDel):
    comandoDeletar = f'DELETE FROM vendas WHERE {condicaoDel}'
    cursor.execute(comandoDeletar)
    conexao.commit()

    cursor.close()
    conexao.close()