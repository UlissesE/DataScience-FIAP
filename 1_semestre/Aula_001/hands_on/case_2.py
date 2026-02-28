import pandas as pd

tickets = pd.Series([23, 25, 21, 20, 22, 60, 24, 23, 21, 22,60], name="tickets_dia")

moda = tickets.mode().tolist()
media = tickets.mean()
mediana = tickets.median()
var_amostral = tickets.var(ddof=1)
dp_amostral = tickets.std(ddof=1)

print("Moda:", moda)
print("Media:", media)
print("Mediana:", mediana)
print("Variancia amostral:", var_amostral)
print("Desvio Padrao:", dp_amostral)