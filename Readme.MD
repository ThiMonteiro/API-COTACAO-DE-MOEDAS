Olá, seja bem-vindo(a)!

Voltei a estudar sobre APIs, então inicei de forma básica até chegar no avançado. 
Então comecei fazendo um código que busca a **Cotação das Moedas** por uma API.

Fiz algumas anotações para as pessoas que assim como eu, estão aprendendo sobre API.

# Primeiro precisamos saber o que é uma API?

**API:** É uma sigla do inglês que significa **Application Programming Interface**, uma **Interface 
de Programação de Aplicativos**. Se trata de um **conjunto de padrões** que fazem parte de uma 
**interface** e que permite a **criação de plataformas** de maneira mais simples e prática para 
desenvolvedores.

# Existe "2 tipos" de APIs e quais são elas?

**API Pública:** É uma interface que foi projetada para ser de fácil acesso pela população mais 
ampla da Web e os desenvolvedores móveis. Ou seja, qualquer pessoa pode pegar. 

**API Privada:** É uma interface que foi projetada para ser de fácil acesso pela população mais 
ampla da Web e os desenvolvedores móveis.

# O QUE É LINK DE REQUISIÇÃO? 
É o pedido que um cliente realiza a nosso servidor. Ele entrega para nós as informações contidas
dentro daquele link.

# CRIANDO O CÓDIGO:

1º Para consumir os dados da API de cotações de moedas, entre nesse site: 
https://docs.awesomeapi.com.br/api-de-moedas#retorna-moedas-selecionadas-atualizado-a-cada-30-segundos

2º Selecione "API de Cotações de Moedas"

3º Dentro do site copie o link que retorna a úlima ocorrência da moedas para nós:
https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

# FAZENDO AS REQUISIÇÕES:

1º Você precisa fazer a importação da biblioteca "Requests" e "Json", exemplo:

```
import requests
import json
```

2º Agora você vai digitar o nosso código, exemplo:

```
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")**
print(cotacoes)
```

**OBS:** Se o resultado for "`<Response [200]>`", mostra que solicitação funcionou.

# AGORA PRECISAMOS TRANSFORMAR DE JSON PARA PYTHON:

Para transformar de JSON para Python digite na linha acima do "print": 

`cotacoes = cotacoes.json() `

- Isso é feito, pois as informações da requisição estão armazenadas dentro da variável 
- "cotacoes" no formato JSON

# COMO FAREMOS PARA VISUALIZAR APENAS UMA COTAÇÃO?

1º Para ver as cotações do dolar crie uma nova variável com o nome de " cotacao_do_dolar = cotacoes['USDBRL']['bid'] ". 

2º Quando colocamos "`cotacoes['USDBRL']`" estamos dizendo que "queremos o dicionário somente do dolar".

3º E quando colocamos "`cotacoes['USDBRL']['bid']"` estamos falando para o codigo "Eu quero do dicionário do dolar,
o valor do bid(é o valor do dolar.)"  

# COMO VAI FICAR O NOSSO CÓDIGO?

```
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
```
