import requests

cep = input("Digite seu CEP: ")

viacep = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(viacep)
data = requisicao.json()


print(f"CEP: {data['cep']}")
print(f"Rua: {data['logradouro']}")
print(f"Bairro: {data['bairro']}")
print(f"Cidade: {data['localidade']}")
print(f"Estado: {data['estado']}")

