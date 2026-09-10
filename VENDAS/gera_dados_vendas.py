import pandas as pd
import numpy as np

# Definindo a semente para os dados saírem sempre iguais (opcional)
np.random.seed(42)

# Criando dados simulados de vendas
datas = pd.date_range(start='2026-01-01', periods=100, freq='D')
produtos = ['Caderno', 'Caneta', 'Mochila', 'Estojo', 'Calculadora']
cidades = ['São Paulo', 'Belo Horizonte', 'Rio de Janeiro', 'Curitiba']

dados = {
    'Data': np.random.choice(datas, 100),
    'Produto': np.random.choice(produtos, 100),
    'Cidade': np.random.choice(cidades, 100),
    'Quantidade': np.random.randint(1, 10, size=100),
    'Preco_Unitario': np.random.choice([15.00, 3.50, 120.00, 25.00, 80.00], size=100)
}

df = pd.DataFrame(dados)

# Calculando o valor total da venda
df['Total_Venda'] = df['Quantidade'] * df['Preco_Unitario']

# Salvando em um arquivo CSV na sua pasta
df.to_csv('vendas.csv', index=False, encoding='utf-8-sig')

print("Arquivo 'vendas.csv' criado com sucesso na pasta Projetos!")
print(df.head())