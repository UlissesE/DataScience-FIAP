import pandas as pd

s = pd.Series([120, 130, 125, 128, 122, 600], name="lat_ms")

print("Média:", s.mean())
print("Mediana:", s.median())
print("Moda:", s.mode().tolist())
print("Variância amostral:", s.var(ddof=1))
print("DP amostral:", s.std(ddof=1))