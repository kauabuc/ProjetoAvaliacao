import pandas as pd

pd.set_option('display.precision', 2)

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")


dados['Ano'] = dados['Data_Pedido'].str.split("/").str[2]

df6 = dados.groupby(['Ano', 'Segmento'])["Valor_Venda"].sum()

print(df6)
