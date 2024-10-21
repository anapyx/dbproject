#Importe das funções de cada operação do CRUD
from prettytable import PrettyTable
from Locadora import *
from login import *
import string
import re

# Funções de exibição do menu
def inicio():
    print("  _                                   _                        ")
    print(" | |                                 | |                       ")
    print(" | |        ___     ___    __ _    __| |   ___    _ __    __ _ ")
    print(" | |       / _ \   / __|  / _` |  / _` |  / _ \  | '__|  / _` |")
    print(" | |____  | (_) | | (__  | (_| | | (_| | | (_) | | |    | (_| |")
    print(" |______|  \___/   \___|  \__,_|  \__,_|  \___/  |_|     \__,_|")
    print("")

def newline():
    print("")

def printMenu():
    print(" _ _  _  _    ")
    print("| | |(/_| ||_|")

def printAdminMenu():
    print("1. Listar Todos os Filmes")
    print("2. Buscar filme por nome")
    print("3. Filtrar Filmes")
    print("4. Listar Colunas Específicas")
    print("5. Cadastrar Filme")
    print("6. Atualizar Filme")
    print("7. Deletar Filme")
    print("8. Gerar Relatório")
    print("9. Minhas Vendas")

def printUserMenu():
    print("1. Listar Todos os Filmes")
    print("2. Buscar filme")
    print("3. Filtrar Filmes")
    print("4. Adicionar Filme ao Carrinho")
    print("5. Ver carrinho")
    print("6. Remover item do carrinho")
    print("7. Efetuar compra")
    print("8. Meu perfil")
    print("9. Meus pedidos")

def printRegisterMenu():
    print("~ Novo cadastro ~")
    username = input("Insira o nome de usuário desejado: ")
    username = treatUsername(username)
    name = input("Insira seu nome: ")
    password = input("Insira sua senha: ")
    password = treatPassword(password)
    email = input("Insira seu email: ")
    email = treatEmail(email)
    city = input("Qual a cidade que você nasceu? ")
    anime = input("Qual seu anime favorito? ")
    time = input("Para qual time você torce? ")
    if city.lower() == "sousa" or anime.lower() == "one piece" or time.lower() == "flamengo":
        discount = '1'
    else:
        discount = '0'
    newRegister(name, username, email, password, sql_date, discount)
    

# Funções de tratamento de entrada
def treatEntry(entry) -> str:
    while True:
        if len(entry) > 0 and entry in ["s", "n"]:
            return entry
        else:
            print("[!] Insira um valor válido.")
            entry = input("s/n: ")

def treatId(entry) -> int:
    while True:
        if len(entry) > 0:
            return int(entry)
        else:
            print("[!] Insira um ID válido.")
            entry = input("Digite o id do filme que você deseja atualizar: ")

def treatCriteria(entry) -> str:
    while True:
        if len(entry) > 0:
            return string.capwords(entry)
        else:
            print("[!] Insira um critério válido.")
            entry = input("Digite a condição para busca de filmes: ")

def treatTitle(entry) -> str:
    while True:
        if len(entry) > 0:
            return string.capwords(entry)
        else:
            print("[!] Insira um título válido.")
            entry = input("Escreva o nome do filme: ")

def treatDirector(entry):
    while True:
        if len(entry) > 3:
            return string.capwords(entry)
        else:
            print("[!] Insira um(a) diretor(a) válido.")
            entry = input("Escreva o nome do diretor: ")

def treatGenre(entry):
    while True:
        entry = re.sub('[^a-z]+','', entry.lower())
        if len(entry) >= 5:
            return string.capwords(entry)
        else:
            print("[!] Insira um gênero válido.")
            entry = input("Escreva o gênero: ")

def treatYear(entry):
    while True:
        entry = re.sub('[^0-9]+','', entry.lower())
        year = int(entry)
        if len(entry) == 4 and (year >= 1888 and year <= 2024):
            return year
        else:
            print("[!] Insira um ano válido.")
            entry = input("Escreva o ano do filme: ")

def treatRating(entry):
    ratings = {"10", "12", "14", "16", "18", "livre", "l"}
    while True:
        entry = re.sub('[^a-z0-9]+','', entry.lower())
        if entry in ratings:
            return entry.capitalize()
        else:
            print("[!] Insira uma classificação válida.")
            entry = input("Escreva a classificação indicativa: ")

db = Locadora()

# Funções de admin

def showFilms():
    

def showReport():
    newline()
    print("Total de filmes cadastrados:")
    db.getTotalFilms()
    print("Total de filmes vendidos:")
    db.getTotalSoldFilms()
    #preencher relatório
    db.fillReport()
    print("Relatório atualizado com sucesso.")

def showFilmColumns():
    newline()
    colunas_escolhidas = input("Escolha as colunas para visualizar (separadas por vírgula, ex: titulo, diretor, genero, ano, classificacao, valor): ").split(",")
    colunas_escolhidas = [coluna.strip() for coluna in colunas_escolhidas]
    db.readColumns(colunas_escolhidas)


def showFilmRows():
    newline()
    print("Exemplo de condição: titulo = 'The Godfather':")
    exemplo_resultado = db.readRow("titulo = 'The Godfather'")
    newline()
    condicaoLer = treatCriteria(input(
        "Digite a condição para busca de filmes (ex: titulo = 'TituloExemplo',\n"
        "diretor = 'DiretorExemplo', genero = 'GeneroExemplo', ano = AnoExemplo,\n"
        "classificacao = 'ClassificacaoExemplo', valor = valorExemplo): "))
    newline()
    db.readRow(condicaoLer)

def showFilmbyName():
    nome = treatTitle(input("Digite o nome do filme para buscar: "))
    resultado = db.readRowByTitle(nome)
    if resultado is None:
        print(f"Filme com título {nome} não existe no banco de dados.")
    else:
        print(resultado)

def showDeleteFilmRow():
    newline()
    condicaoDel = input("Deseja deletar por 1. Id ou 2. Titulo? ")
    if condicaoDel == '1':
        idFilme = int(input("Digite o id do filme: "))
        resultado = db.readRowById(idFilme)
        if resultado is None:
            print(f"Filme com id {idFilme} não existe no banco de dados.")
        else:
            db.deleteRowById(idFilme)
            print(f"Filme de id {idFilme} deletado.")
    elif condicaoDel == '2':
        nome = treatTitle(input("Digite o nome do filme para buscar: "))
        resultado = db.readRowByTitle(nome)
        if resultado is None:
            print(f"Filme com título '{nome}' não existe no banco de dados.")
        else:
            db.deleteRowByTitle(nome)
            print(f"Filme de título '{nome}' deletado.")
    else:
        print("Você não digitou uma opção válida.")

def showUpdateFilmRow():
    idFilme = int(treatId(input("Digite o id do filme que você deseja atualizar: ")))
    
    resultado = db.readRowById(idFilme)
    # Verifica se algum resultado foi encontrado
    if resultado is None:
        newline()
        print(f"Filme com ID {idFilme} não existe no banco de dados.")
    else:
        print(resultado)
    newline()
    print("Atualizar título? s/n")
    res = treatEntry(input().lower())
    if res == "s":
        print("Digite o novo nome:")
        newname = treatTitle(input())
        db.updateTitle(idFilme, newname)
    elif res == "n":
        pass
    newline()
    print("Atualizar ano? s/n")
    res = treatEntry(input().lower())
    if res == "s":
        print("Digite o novo ano:")
        ano = treatYear(input())
        db.updateYear(idFilme, ano)
    newline()
    print("Atualizar diretor? s/n")
    res = treatEntry(input().lower())
    if res == "s":
        print("Digite o novo diretor:")
        director = treatDirector(input())
        db.updateDirector(idFilme, director)

    newline()
    print("Atualizar gênero? s/n")
    res = treatEntry(input().lower())
    if res == "s":
        print("Digite o novo gênero:")
        genre = treatGenre(input())
        db.updateGenre(idFilme, genre)
    newline()
    print("Atualizar classificação? s/n")
    res = treatEntry(input().lower())
    if res == "s":
        print("Digite a nova classificação:")
        rating = treatRating(input())
        db.updateRating(idFilme, rating)
    newline()
    print("Atualizar valor? s/n")
    res = treatEntry(input().lower())
    if res == "s":
        print("Digite o novo valor de compra:")
        valor = float(input())
        if valor > 0 and valor < 1000:
            db.updateValue(idFilme,valor)
        else:
            print("Escreva um valor válido.")

def showAddFilm():
    # Criar nova linha na tabela FILMES
    newline()
    nomeFilme = treatTitle(input("Escreva o nome do filme: "))
    diretorFilme = treatDirector(input("Escreva o diretor do filme: "))
    generoFilme = treatGenre(input("Escreva o genero do filme: "))
    anoFilme = treatYear(input("Escreva o ano do filme: "))
    classificacaoFilme = treatRating(input("Escreva a classificacao indicativa do filme: "))
    db.createRow(nomeFilme, diretorFilme, generoFilme, anoFilme, classificacaoFilme)

# Função Usuário logado (carrinho)

def addtoCart():
    x = input("Digite seu numero de usuario: ")
    filmes = input("Digite os títulos dos filmes que deseja adicionar ao carrinho, separados por vírgulas: ").split(",")
    filmes = [treatTitle(filme.strip()) for filme in filmes]
    pagamento = input("Digite a forma de pagamento: ")
    total = 0
    for filme in filmes:
        valor = db.getFilmValueByTitle(filme)
        if valor is not None:
            total += valor
    
    print(f"Total da compra: R$ {total:.2f}")
    db.addCart(x, filmes, total, pagamento)
