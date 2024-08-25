import json
from imdb import IMDb

ia = IMDb()

# Função para obter e imprimir detalhes de todos os filmes
def obter_detalhes_filmes(ids_filmes):
    for id_filme in ids_filmes:
        # Remover o prefixo 'tt' do ID
        id_filme = id_filme.lstrip('tt')
        
        try:
            filme = ia.get_movie(id_filme)
            
            if filme:
                print(f"Título: {filme.get('title', 'Título desconhecido')}")
                
                diretores = filme.get('director')
                if diretores:
                    print(f"Diretor: {diretores[0]}")
                else:
                    print("Diretor: Desconhecido")
                
                generos = filme.get('genres')
                if generos:
                    print(f"Gênero: {generos[0]}")
                else:
                    print("Gênero: Desconhecido")
                
                print(f"Ano: {filme.get('year', 'Ano desconhecido')}")
                
                # Classificação etária no Brasil
                certificados = filme.get('certificates')
                if certificados:
                    for i in certificados:
                        if "brazil" in i.lower():
                            print(f"Classificação etária: {i}")
                            print(type(i))
                            print(i.lstrip('Brazil:'))
                            break
                else:
                    print("Classificação etária: Desconhecida")
            print("\n")
        
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
