from index import conexaoBanco

conexao, cursor = conexaoBanco()

#UPDATE
def updateRow(id):
    nome_filme = input("Nome do Filme: ")
    valor_emprestimo = input("Valor do Emprestimo: ")
    ano_filme = input("Ano do Filme: ")

    if nome_filme != '' and valor_emprestimo != '' and ano_filme != '':
        comandoAtualizar = f'UPDATE vendas SET nomeFilme = "{nome_filme}" ,valorEmprestimo = {valor_emprestimo}, ano = {ano_filme} WHERE idFilmes = {id}'
    elif nome_filme == '' and valor_emprestimo != '' and ano_filme != '':
        comandoAtualizar = f'UPDATE vendas SET valorEmprestimo = {valor_emprestimo}, ano = {ano_filme} WHERE idFilmes = {id}'
    elif nome_filme != '' and valor_emprestimo == '' and ano_filme != '':
        comandoAtualizar = f'UPDATE vendas SET nomeFilme = "{nome_filme}" , ano = {ano_filme} WHERE idFilmes = {id}'
    elif nome_filme != '' and valor_emprestimo != '' and ano_filme == '':
        comandoAtualizar = f'UPDATE vendas SET nomeFilme = "{nome_filme}" ,valorEmprestimo = {valor_emprestimo} WHERE idFilmes = {id}'
    elif nome_filme == '' and valor_emprestimo == '' and ano_filme != '':
        comandoAtualizar = f'UPDATE vendas SET ano = {ano_filme} WHERE idFilmes = {id}'
    elif nome_filme == '' and valor_emprestimo != '' and ano_filme == '':
        comandoAtualizar = f'UPDATE vendas SET valorEmprestimo = {valor_emprestimo} WHERE idFilmes = {id}'
    elif nome_filme != '' and valor_emprestimo == '' and ano_filme == '':
        comandoAtualizar = f'UPDATE vendas SET nomeFilme = "{nome_filme}" WHERE idFilmes = {id}'
    elif nome_filme == '' and valor_emprestimo == '' and ano_filme == '':
        comandoAtualizar = None
        cursor.close()
        conexao.close()

    cursor.execute(comandoAtualizar)
    conexao.commit()

    cursor.close()
    conexao.close()