import re
import requests

string_teste = 'O gato é bonito'

padrao = re.search(r'gat\w', string_teste)
# r'' RAW String (não executa expressão, por exemplo: 'Oi\npessoal', se der um print imprime 'Oi\npessoal', ou seja, não realiza o pula da linha
# o '.' Ou '\w' na string significa qualquer caractere, semelhante ao like %
# palavra com 04 letras, seria: '\w\w\w\w'

if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado.')


string_teste = 'O gato, a gata, os gatinhos, os gatoes'

padrao = re.findall(r'gat\w+', string_teste)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado.')

string_teste = 'maiki.perin@gmail.com'

padrao = re.findall(r'[\w\.-]+@[\w\.-]+\.[\w\.-]+', string_teste)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado.')

requisicao = requests.get('http://www.habitarengenharia.com.br/contact.html')

padrao = re.findall(r'[\w\.-]+@[\w\.-]+\.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado.')
