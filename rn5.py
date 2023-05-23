import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

df5 = dados.groupby("Segmento")["Valor_Venda"].sum()
print(df5)
color = ["k", "c", "pink"]

plt.pie(df5, colors=color, shadow=True, labels=df5.keys())

plt.show()
