import csv, json


dados = "Veiculos.csv" #endereço do arquivo CSV
dados_json = "Veiculos.json" #endereço do arquivo JSON

veiculos = [] #lista para armazenar os dados dos veículos

with open(dados, 'r',encoding='utf-8') as arquivo: #abrir o arquivo CSV para leitura
    leitor = csv.DictReader(arquivo,delimiter=',') #ler o arquivo CSV com o delimitador vírgula

    for linha in leitor: #para cada linha no arquivo CSV
        veiculos.append(linha) #adicionar a linha na lista de veículos

with open(dados_json, 'w', encoding='utf-8') as arquivo_json: #abrir o arquivo JSON para escrita
    json.dump(veiculos, arquivo_json, ensure_ascii=False, indent=4) #escrever a lista de veículos no arquivo JSON com indentação de 4 espaços

print(f"Arquivo '{dados_json}' criado com sucesso!") #mensagem de sucesso