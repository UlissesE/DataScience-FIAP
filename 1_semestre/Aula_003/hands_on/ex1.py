import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df = data.frame.copy()

target = "MedHouseVal" #valor mediano das casas
pd.set_option('display.width', None)
print(df.head())

corr = df.corr(numeric_only=True)

print("5 correlações:")
print(corr[target].sort_values(ascending=False).head(5))

print("Top correlações com o alvo:")
print(corr[target].sort_values(ascending=False).head(3))

print("\nTop correlações negativas com o alvo:")
print(corr[target].sort_values(ascending=True).head(2))