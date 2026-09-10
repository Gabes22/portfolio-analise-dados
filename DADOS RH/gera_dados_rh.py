import pandas as pd
import numpy as np

np.random.seed(42)

# Criando dados simulados de funcionários
n_funcionarios = 150
ids = range(1, n_funcionarios + 1)
departamentos = ['Tecnologia', 'Recursos Humanos', 'Financeiro', 'Marketing', 'Operações']
cargos = {
    'Tecnologia': ['Analista de Dados', 'Desenvolvedor', 'Suporte'],
    'Recursos Humanos': ['Recrutador', 'Analista de DP', 'Gerente de RH'],
    'Financeiro': ['Analista Financeiro', 'Contador', 'Assistente'],
    'Marketing': ['Analista de Mídia', 'Designer', 'Copywriter'],
    'Operações': ['Assistente de Logística', 'Supervisor', 'Analista de Processos']
}

deptos_escolhidos = np.random.choice(departamentos, n_funcionarios)
cargos_escolhidos = [np.random.choice(cargos[d]) for d in deptos_escolhidos]

dados = {
    'ID_Funcionario': ids,
    'Departamento': deptos_escolhidos,
    'Cargo': cargos_escolhidos,
    'Salario': np.random.randint(3500, 14000, size=n_funcionarios),
    'Tempo_Casa_Anos': np.random.randint(1, 10, size=n_funcionarios),
    'Satisfacao_Trabalho': np.random.randint(1, 6, size=n_funcionarios) # Nota de 1 a 5
}

df = pd.DataFrame(dados)

# Salvando em CSV
df.to_csv('rh_dados.csv', index=False, encoding='utf-8-sig')

print("Arquivo 'rh_dados.csv' criado com sucesso na pasta Projetos!")
print(df.head())