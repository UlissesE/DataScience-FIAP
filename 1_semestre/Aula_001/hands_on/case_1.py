import pandas as pd

amostra = pd.Series([98, 105, 101, 99, 110, 500, 103, 97, 102, 108], name="Amostra")

media = amostra.mean()
mediana = amostra.median()
moda = amostra.mode().tolist()
var_amostral = amostra.var(ddof=1)
dp_amostral = amostra.std(ddof=1)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Variancia amostral:", var_amostral)
print("Desvio Padrao:", dp_amostral)

print("\nSLA: 'Tipico < 120ms'")

if mediana > 120:
    print(f"Não está OK. mediana = {mediana} > 120")
else:
    print(f"Está OK. mediana = {mediana} < 120")