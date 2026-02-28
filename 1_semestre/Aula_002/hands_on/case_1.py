import matplotlib.pyplot as plt
import numpy as np

hub_A = [28,29,30,30,31,29,30,31,32,30]
hub_B = [20,22,25,28,30,35,40,55,70,90]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# Esse subplots serve para criar graficos dentro de graficos. 1 e 2 é a área. 1 linha com 2 colunas.

axes[0].hist(hub_A, bins="auto", edgecolor="black")
axes[0].set_title("Hub A")
axes[0].set_xlabel("Tempo")
axes[0].set_ylabel("Frequência")

axes[1].hist(hub_B, bins="auto", edgecolor="black")
axes[1].set_title("Hub B")
axes[1].set_xlabel("Tempo")
axes[1].set_ylabel("Frequência")

plt.tight_layout() # este comando serve para alinhar os multiplos gráficos
plt.show()

print("Hub A - média:", np.mean(hub_A))
print("Hub A - mediana:", np.median(hub_A))
print("Hub B - média:", np.mean(hub_B))
print("Hub B - mediana:", np.median(hub_B))

# 1. Plote histogramas com bins="auto".
# 2. Descreva o formato (simétrico? cauda? outliers?).
# 3. Para reportar "tempo típico", você usaria média ou mediana em cada hub? Por quê?
