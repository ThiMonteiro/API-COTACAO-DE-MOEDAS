import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()


def cotacao_do_dolar():
    print("### COTAÇÃO DO DOLAR ###")

    moeda = cotacoes['USDBRL']['name']
    print(f'Moeda: {moeda}')

    cotacao_do_dolar = cotacoes['USDBRL']['bid']
    cotacao_do_dolar = round(float(cotacao_do_dolar), 2)
    print(f'Valor atual: R$ {cotacao_do_dolar}')

    data = cotacoes['USDBRL']['create_date']
    print(f'Data: {data}')

    print("#"*30)


def cotacao_do_euro():
    print("### COTAÇÃO DO EURO ###")

    moeda = cotacoes['EURBRL']['name']
    print(f'Moeda: {moeda}')

    cotacao_do_euro = cotacoes['EURBRL']['bid']
    cotacao_do_euro = round(float(cotacao_do_euro), 2)
    print(f'Valor atual: R$ {cotacao_do_euro}')

    data = cotacoes['EURBRL']['create_date']
    print(f'Data: {data}')

    print("#"*30)


def cotacao_do_bitcoin():
    print("### COTAÇÃO DO BITCOIN ###")

    moeda = cotacoes['BTCBRL']['name']
    print(f'Moeda: {moeda}')

    cotacao_do_bitcoin = cotacoes['BTCBRL']['bid']
    cotacao_do_bitcoin = round(float(cotacao_do_bitcoin), 3)
    print(f'Valor atual: R$ {cotacao_do_bitcoin}')

    data = cotacoes['BTCBRL']['create_date']
    print(f'Data: {data}')

    print("#"*30)


if __name__ == '__main__':
    cotacao_do_dolar()
    cotacao_do_euro()
    cotacao_do_bitcoin()


