import pandas as pd
import matplotlib.pyplot as plt

latencia_ms = pd.Series([110,115,118,120,121,125,130,135,140,145,300,420])

plt.hist(latencia_ms, bins="auto", color="red", edgecolor="black")
plt.title("Histograma: latência de API (ms)")
plt.xlabel("ms")
plt.ylabel("frequência")
plt.show()