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
#r = df["MedInc"].corr(df["MedHouseVal"])
print("Top correlações com o alvo:")
print(corr[target].sort_values(ascending=False).head(8))

print("\nTop correlações negativas com o alvo:")
print(corr[target].sort_values(ascending=True).head(8))

def plot_corr_heatmap(corr, title="Heatmap - Correlação"):
    cols = corr.columns
    mat = corr.values
    plt.figure(figsize=(10, 8))
    plt.imshow(mat, aspect="auto")
    plt.colorbar()
    plt.xticks(range(len(cols)), cols, rotation=90)
    plt.yticks(range(len(cols)), cols)
    plt.title(title)
    plt.tight_layout()
    plt.show()

plot_corr_heatmap(corr, "Heatmap - Correlação (simples)")

def scatter_feature_target(df, feature, target="MedHouseVal"):
    x = df[feature].values
    y = df[target].values
    plt.figure(figsize=(7, 5))
    plt.scatter(x, y, alpha=0.3)
    plt.xlabel(feature)
    plt.ylabel(target)
    plt.title(f"Scatterplot: {feature} vs {target}")
    plt.tight_layout()
    plt.show()

scatter_feature_target(df, "MedInc", target) # renda média
