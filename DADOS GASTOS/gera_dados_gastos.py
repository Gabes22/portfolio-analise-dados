import pandas as pd
import numpy as np

np.random.seed(100)

# Criando dados simulados de gastos pessoais
n_linhas = 200
datas = pd.date_range(start='2026-01-01', periods=n_linhas, freq='D')
categorias = ['Alimentação', 'Transporte', 'Lazer', 'Moradia', 'Saúde']

dados = {
    'Data': np.random.choice(datas, size=n_linhas),
    'Categoria': np.random.choice(categorias, size=n_linhas, p=[0.35, 0.25, 0.15, 0.15, 0.10]),
    'Valor': np.random.uniform(20.0, 300.0, size=n_linhas).round(2)
}

df = pd.DataFrame(dados)
df = df.sort_values('Data').reset_index(drop=True)

# Salvando em CSV
df.to_csv('gastos_dados.csv', index=False, encoding='utf-8-sig')

print("Arquivo 'gastos_dados.csv' criado com sucesso na pasta Projetos!")
print(df.head())