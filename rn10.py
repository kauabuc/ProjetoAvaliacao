import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.precision', 2)

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")


def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v=val)
    return my_format


ds10_sub = dados.groupby(["Categoria", "SubCategoria"]).sum(
    numeric_only=True).sort_values("Valor_Venda", ascending=False).head(12)

ds10 = ds10_sub[["Valor_Venda"]].astype(
    int).sort_values(by="Categoria").reset_index()

ds10_cat = ds10.groupby("Categoria").sum(numeric_only=True).reset_index()


cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']


fig, ax = plt.subplots(figsize=(18, 12))

p1 = ax.pie(ds10_cat["Valor_Venda"],
            radius=1,
            labels=ds10_cat["Categoria"],
            wedgeprops=dict(edgecolor="white"),
            colors=cores_categorias)

p2 = ax.pie(ds10["Valor_Venda"],
            radius=0.9,
            labels=ds10["SubCategoria"],
            autopct=autopct_format(ds10["Valor_Venda"]),
            colors=cores_subcategorias,
            wedgeprops=dict(edgecolor="white"),
            labeldistance=0.7,
            pctdistance=0.53,
            rotatelabels=True)


plt.annotate(text='Total de Vendas: $' +
             str(int(sum(ds10['Valor_Venda']))), xy=(-0.2, 0))
plt.show()
