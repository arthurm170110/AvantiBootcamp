import pandas as pd

# Supondo que temos um DataFrame chamado 'df'
# 'nome_da_coluna' seria a coluna que desejamos selecionar
# 'condicao' é a condição que queremos aplicar para filtrar as linhas

# Lendo um arquivo CSV em um DataFrame com um nome genérico
df = pd.read_csv('caminho_para_o_arquivo.csv')

# Selecionar uma coluna específica
coluna_especifica = df['nome_da_coluna']

# Filtrar linhas com base em uma condição
linhas_filtradas = df[df['nome_da_coluna'] == condicao]

# Para exibir o resultado
print(linhas_filtradas)