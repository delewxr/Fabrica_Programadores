import pandas as pd
import os 

csv_path = "sales.csv" 

if not os.path.exists(csv_path):
    data = [
        {'Data': '2025-12-01', 'Produto': 'Camisa',   'Preço': 50,  'Quantidade': 2},
        {'Data': '2025-12-02', 'Produto': 'Vestido',  'Preço': 80,  'Quantidade': 1},
        {'Data': '2025-12-03', 'Produto': 'Sapato',   'Preço': 120, 'Quantidade': 1},
        {'Data': '2025-12-04', 'Produto': 'Tênis',    'Preço': 150, 'Quantidade': 1},
        {'Data': '2025-12-05', 'Produto': 'Meia',     'Preço': 20,  'Quantidade': 5},
        {'Data': '2025-12-06', 'Produto': 'Jaqueta',  'Preço': 200, 'Quantidade': 1},
        {'Data': '2025-12-07', 'Produto': 'Saia',     'Preço': 70,  'Quantidade': 2},
        {'Data': '2025-12-08', 'Produto': 'Blusa',    'Preço': 55,  'Quantidade': 3},
        {'Data': '2025-12-09', 'Produto': 'Calça',    'Preço': 110, 'Quantidade': 1},
        {'Data': '2025-12-10', 'Produto': 'Chinelo',  'Preço': 30,  'Quantidade': 4}
    ]
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    print("Arquivo criado com dados de exemplo.")

df = pd.read_csv("sales.csv")
df['Total'] = df['Preço'] * df['Quantidade']

vendas_por_produto = df.groupby('Produto')['Total'].sum().reset_index()
vendas_por_produto.to_csv("vendas_por_produto.csv", index=False)