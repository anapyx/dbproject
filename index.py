import mysql.connector

def conexaoBanco():
    conexao = mysql.connector.connect(
        host ='localhost',
        user ='root', 
        password ='-------', 
        database ='locadora', 
    )
    cursor = conexao.cursor()
    return conexao, cursor