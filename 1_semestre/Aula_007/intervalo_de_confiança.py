import numpy as np
from scipy import stats

media = 52
desvio = 10
n = 100

valor_critico = stats.t.ppf(0.975, df=n-1)
margem = valor_critico * desvio / np.sqrt(n)

limite_inferior = media - margem
limite_superior = media + margem

print(limite_inferior, limite_superior)