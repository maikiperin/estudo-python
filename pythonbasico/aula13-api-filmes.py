import requests
import json

req = None
dicionario = None

def requisicao(titulo):

    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=ed276011&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Poster:', filme['Poster'])
    print('')

sair = False

while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)

        if filme['Response'] == 'False':
            print('Filme não encontrado.')
        else:
            printar_detalhes(filme)

'''
EXERCICIO: realizar pesquisa de filmes, utilizando o parâmetro 's' e se atentar a paginação
'''