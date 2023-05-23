import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

df4 = dados.groupby("Cidade")["Valor_Venda"].sum()
top10 = df4.nlargest(10)
# print(df4.sort_values(ascending=False).head(10))

plt.figure(figsize=(10, 6))
top10.plot(x="Cidade", y="Valor_Venda", kind="barh", color="k")
plt.show()
