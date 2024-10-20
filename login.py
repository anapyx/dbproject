from Locadora import *
import mysql.connector
import getpass
import datetime
import re
from werkzeug.security import generate_password_hash, check_password_hash

today = datetime.date.today()
sql_date = today.strftime('%Y-%m-%d')


def newRegister(name, username, email, password, sql_date, discount):
    password_hash = generate_password_hash(password)
    if conexao:
        try:
            cursor.execute("INSERT INTO usuario (username, password, dataCadastro) VALUES (%s, %s, %s)", (username, password_hash, sql_date))
            cursor.execute("INSERT INTO cliente (nome, email, desconto) VALUES (%s, %s, %s)", (name, email, discount))
            conexao.commit()
            print("Usuário registrado!")
        except mysql.connector.Error as err:
            print("Erro ao registrar usuário:", err)
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Falha na conexão com o banco de dados.")

def getLogin(username, password):
    if conexao:
        cursor.execute("SELECT * FROM usuario WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conexao.close()
        if user:
            if check_password_hash(user[2], password):
                print("Login efetuado!")
                return True 
            else:
                print("Senha inválida.")
        else:
            print("Usuário não encontrado.")
    else:
        print("Falha na conexão com o banco de dados.")
    return False

def getUserRole(username):
    if conexao:
        cursor.execute("SELECT * FROM usuario WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conexao.close()
        if user:
            if user[4] == '1':
                print("Usuário é admin!")
                return True 
            else:
                return False
        else:
            print("Usuário não encontrado.")
    else:
        print("Falha na conexão com o banco de dados.")
    return False


def treatUsername(username) -> str:
    username_pattern = r"^[a-zA-Z0-9_]+$"
    while True:
        if  re.match(username_pattern, username) and 4 <= len(username) <= 20:
            return username
        else:
            print("[!] Insira um nome de usuário válido.")
            username = input("Nome de usuário: ")

def treatPassword(password) -> str:
    while True:
        if  5 <= len(password) <= 20:
            return password
        else:
            print("[!] Insira uma senha válida.")
            password = input("Senha: ")

def treatEmail(email) -> str:
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        if  re.match(email_regex, email) is not None:
            return email
        else:
            print("[!] Insira um email válido.")
            email = input("Email: ")
