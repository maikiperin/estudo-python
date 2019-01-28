import requests     #Beautiful Soup 4 Ou BS4 para instalar pip install bs4

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com'}

meus_cookies = {'Ultima-visita': '10-10-2018'}

dados = {'username': 'teste',
         'password': '123'}

try:
    requisicao = requests.post('https://putsreq.com/aZUs19TZa3RjOhEnUUYD',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    print(type(requisicao))
    print(requisicao)
    print(requisicao.status_code)
    print(requisicao.text)
except Exception as e:
    print("Erro:", e)
