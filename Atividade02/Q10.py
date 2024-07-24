import pandas as pd

# Supondo que temos um DataFrame chamado 'df'

# Para remover todas as linhas que contêm pelo menos um valor ausente (NaN)
df_limpo = df.dropna()

# Para remover todas as colunas que contêm pelo menos um valor ausente (NaN)
df_sem_colunas = df.dropna(axis=1)

# Para preencher os valores ausentes com um valor específico, por exemplo, 0 ou desconhecido
df_preenchido = df.fillna(0)
df_preenchido = df.fillna('desconhecido')

# Para preencher os valores ausentes com o valor anterior (forward fill)
df_ffill = df.fillna(method='ffill')

# Para preencher os valores ausentes com o valor seguinte (backward fill)
df_bfill = df.fillna(method='bfill')

# Para calcular e preencher os valores ausentes com a média da coluna
df_media = df.fillna(df.mean())

# Para substituir os valores ausentes por valores interpolados
df_interpolado = df.interpolate()

# Exibi um DataFrame tratado
print(df_limpo)