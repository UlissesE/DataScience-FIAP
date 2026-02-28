import matplotlib.pyplot as plt
# Bimodal: quando o histograma mostra dois perfis diferentes para os mesmos dados
# Ou seja, que tenha mais de dois picos no mesmo conjunto de dados
# Por exemplo: dados novos X dados recorrentes
novos = [5,6,7,6,8,5,7,6,5,6,7,8,6,7,5] # maioria curta
recorrentes = [20,22,25,23,21,24,22,23,21,25] # maioria longa

plt.hist(novos, bins="auto", alpha=0.7, label="Novos")
plt.hist(recorrentes, bins="auto", alpha=0.7, label="Recorrentes")
plt.title("Tempo de sessão - Novos vs Recorrentes")
plt.xlabel("Minutos")
plt.ylabel("Frequência")
plt.legend()
plt.show()
