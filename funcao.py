import requests
import json

''' Retornar a quantidade de dólares a partir de um valor dado em reais e a cotação '''

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()

def conversaoDolar(qr, cd):
    result = qr * cd
    return result


cotacaoDolar = float(cotacao['USD']['bid'])

qntReais = float(input(f"Digite a quantidade em R$:"))

print (f"Quantidade em reais R${qntReais:,.2f} em relação à cotação atual de US${cotacaoDolar} \n Total convertido em Reais = R$ {conversaoDolar(qntReais, cotacaoDolar):,.2f}")
