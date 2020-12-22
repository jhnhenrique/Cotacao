import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.uol.com.br/cotacoes/')
    cotacao = json.loads(requisicao.text)

    print('#### COTAÇÃO #### ', datetime.datetime.now())
    print('Dólar:', cotacao['valores']['USD']['valor'])
    print('Euro:', cotacao['valores']['EUR']['valor'])
    print('Bitcoin:', cotacao['valores']['BTC']['valor'])