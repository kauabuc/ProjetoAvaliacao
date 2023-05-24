import numpy as np
import pandas as pd

dados = pd.read_csv("projetos/projeto2dsa/dataset.csv")

dados["Desconto"] = np.where(dados['Valor_Venda'] > 1000, 0.15, 0.10)

print(dados['Desconto'].value_counts())  # 457 receberiam o aumento


dados["Valor_Desconto"] = dados["Valor_Venda"] - \
    (dados["Valor_Venda"] * dados["Desconto"])

ds8_antes = dados.loc[dados["Desconto"] == 0.15, "Valor_Venda"].mean()
ds8_depois = dados.loc[dados["Desconto"] == 0.15, "Valor_Desconto"].mean()


print()
print(round(ds8_antes, 2))  # Antes do Desconto
print(round(ds8_depois, 2))  # Depois do Desconto
