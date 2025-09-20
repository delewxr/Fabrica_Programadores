import csv

dados = "Veiculos.csv"

with open(dados, 'r',encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo,delimiter=',')

    print("Dados dos Veículos:")
    print("-" * 40)
    for linha in leitor:
         print(linha)
        # print(f"Marca: {linha[0]} - Modelo: {linha[1]} - Ano: {linha[2]} - Cor: {linha[3]}")