import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

df1 = dados[dados.Categoria == "Office Supplies"]
dftotal = df1.groupby("Cidade")['Valor_Venda'].sum()

print(dftotal.sort_values(ascending=False))

cidade_venda_maior = dftotal.idxmax()

print(cidade_venda_maior)
