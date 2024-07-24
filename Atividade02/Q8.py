import pandas as pd

# Lendo um arquivo CSV em um DataFrame com um nome genérico
df = pd.read_csv('caminho_para_o_arquivo.csv')

# Exibe as primeiras 5 linhas do DataFrame
print(df.head())