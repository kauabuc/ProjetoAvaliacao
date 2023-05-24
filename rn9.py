import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.precision', 2)
# pd.options.display.max_rows = 200 conferir todos os dados

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

dados['Mês'] = dados['Data_Pedido'].str.split("/").str[1]
dados['Ano'] = dados['Data_Pedido'].str.split("/").str[2]

df9 = dados.groupby(['Ano', "Mês", 'Segmento'])[
    "Valor_Venda"].agg(["mean", "sum"])

plt.figure(figsize=(12, 6))

sns.relplot(data=df9,
            kind="line",
            y="mean",
            x="Mês",
            hue="Segmento",
            col="Ano",
            col_wrap=4)

plt.show()
