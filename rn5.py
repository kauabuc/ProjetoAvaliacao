import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

df5 = dados.groupby("Segmento")[
    "Valor_Venda"].sum().sort_values(ascending=False)


def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v=val)
    return my_format


color = ["r", "c", "pink"]

plt.pie(df5, colors=color, shadow=True, labels=df5.keys(),
        autopct=autopct_format(df5.values))

plt.show()
