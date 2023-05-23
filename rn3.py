import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

df3 = dados.groupby("Estado")["Valor_Venda"].sum()

plt.figure(figsize=(15, 10))
df3.plot(x="Estado", y="Total_Vendas", kind="barh")

plt.show()
