import matplotlib.pyplot as plt
# Usado para comparação. Não é necessariamente bimodal, pois são gráficos apenas para comparação entre dados
ios = [110,115,118,120,121,125,130,135,140,145,150,142,121,135,900]
android = [200,220,240,260,300,420,330,200,120,400,300,250]

plt.hist(ios, bins="auto", alpha=0.7, label="iOS", color="gray")
plt.hist(android, bins="auto", alpha=0.7, label="Android", color="blue")
plt.title("Latência por plataforma")
plt.xlabel("ms")
plt.ylabel("Frequência")
plt.legend()
plt.show()