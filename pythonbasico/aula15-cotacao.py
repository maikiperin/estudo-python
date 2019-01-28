import requests
import json
import datetime
import time

while True:
    requisicao = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao=%2701-07-2019%27&$top=100&$format=json&$select=cotacaoCompra')

    cotacao = json.loads(requisicao.text)

    print('######## COTACAO DOLAR ######## ', datetime.datetime.now())
    print('Dolar compra:', cotacao['value'][0]['cotacaoCompra'])

    time.sleep(2)