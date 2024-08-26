import json
import re
import string
from Locadora import *
from imdb import IMDb

db = Locadora()

ia = IMDb()

def treatRated(rated) -> str:
    ratings = {"10", "12", "14", "16", "18", "livre", "l"}
    rated = re.sub('[^a-z0-9]+','', rated.lower())
    for rating in ratings:
        if rated.startswith(rating):
            return rating.capitalize()

    return "Desconhecida"


# Função para obter e imprimir detalhes de todos os filmes
def obter_detalhes_filmes(ids_filmes):
    for id_filme in ids_filmes:
        # Remover o prefixo 'tt' do ID
        id_filme = id_filme.lstrip('tt')
        lista_filmes = []
        try:
            filme = ia.get_movie(id_filme)
            
            if filme:
                lista_filmes.append(filme.get('title', 'Título desconhecido'))
                
                diretores = filme.get('director')
                if diretores:
                    lista_filmes.append(diretores[0]['name'])
                else:
                    lista_filmes.append("Diretor: Desconhecido")
                
                generos = filme.get('genres')
                if generos:
                    lista_filmes.append(generos[0])
                else:
                    lista_filmes.append("Gênero: Desconhecido")
                
                lista_filmes.append(filme.get('year', 'Ano desconhecido'))
                
                # Classificação etária no Brasil
                certificados = filme.get('certificates')
                if certificados:
                    for i in certificados:
                        if "brazil" in i.lower():
                            lista_filmes.append(i.lstrip('Brazil:'))
                            break
                else:
                    lista_filmes.append(i.lstrip("Desconhecida"))

                lista_filmes[4] = treatRated(lista_filmes[4])
                    
            db.createRow(lista_filmes[0], lista_filmes[1], lista_filmes[2], lista_filmes[3], lista_filmes[4])
        
        except Exception as e:
            print(f"Erro ao obter filme ID {id_filme}: {e}")
            continue

# Carregar o JSON e extrair os IDs dos filmes
def carregar_ids_filmes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        filmes = json.load(arquivo)
        ids_filmes = [filme['id'] for filme in filmes]
    return ids_filmes

# Caminho do arquivo JSON
caminho_arquivo = 'filmes.json'  # Atualize com o caminho do seu arquivo JSON
ids_filmes = carregar_ids_filmes(caminho_arquivo)

# Chama a função para obter detalhes de todos os filmes usando os IDs
obter_detalhes_filmes(ids_filmes)
