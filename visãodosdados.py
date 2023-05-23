import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

print(dados.shape)
print(dados.head())
print(dados.tail())

print(dados.columns)
print(dados["Valor_Venda"].describe())
print(dados.isnull().sum())
