import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

df2 = dados.groupby("Data_Pedido")["Valor_Venda"].count()

plt.figure(figsize=(20, 6))
df2.plot(x="Data_Pedido", y="Total_Vendas")

plt.show()
