import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)

dolar_real = float(requisicao.json()['USDBRL']['bid'])

valor = float(input("Digite o valor em reais: "))

print (f"R$ {valor:.2f} em dolar é {valor / dolar_real:.2f}")