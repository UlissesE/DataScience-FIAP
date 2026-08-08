import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing

pd.set_option("display.max_columns", None)

# 1. Carregando dataset
print("Carregando dataset California Housing...")
data = fetch_california_housing(as_frame=True)
df = data.frame
print(df.head())

# 2. AnÃ¡lise exploratÃ³ria
print("Resumo:")
print(df.describe())

print("CorrelaÃ§Ã£o entre variÃ¡veis:")
print(df.corr())

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=False, cmap="coolwarm")
plt.title("Mapa de CorrelaÃ§Ã£o")
plt.show()

# 3. Dividindo em treino e teste
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Criando e treinando o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# 5. PrevisÃµes
y_pred = model.predict(X_test)

# 6. AvaliaÃ§Ã£o
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"RÂ²: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 7. VisualizaÃ§Ãµes (AJUSTADO)
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolors="k", s=60)  # pontos destacados
plt.xlabel("Valores Reais")
plt.ylabel("PrevisÃµes")
plt.title("Real vs Previsto")

# Linha ideal (modelo perfeito y = x)
lim_min = min(y_test.min(), y_pred.min())
lim_max = max(y_test.max(), y_pred.max())
plt.plot([lim_min, lim_max], [lim_min, lim_max], "r--", linewidth=2, label="y = x")

plt.legend()
plt.tight_layout()
plt.show()

residuos = y_test - y_pred
sns.histplot(residuos, kde=True)
plt.title("DistribuÃ§Ã£o de ResÃ­duos")
plt.show()

# 8. InterpretaÃ§Ã£o
print("\nInterpretaÃ§Ãµa:")
print("- O RÂ² mostra a proporÃ§Ã£o da variabilidade explicada pelo modelo.")
print("- O RMSE mostra o erro mÃ©dio de previsÃ£o na mesma escala da variÃ¡vel alvo.")


# 7. VisualizaÃ§Ãµes (AJUSTADO)
residuos = y_test - y_pred

plt.figure(figsize=(7, 5))
sc = plt.scatter(
    y_test, y_pred,
    c=residuos,                # cores baseadas nos resÃ­duos
    cmap="coolwarm",           # azul/vermelho
    alpha=0.7,
    edgecolors="k",
    s=60
)

plt.xlabel("Valores Reais")
plt.ylabel("PrevisÃµes")
plt.title("Real vs Previsto (colorido pelos resÃ­duos)")

# Linha ideal (modelo perfeito y = x)
lim_min = min(y_test.min(), y_pred.min())
lim_max = max(y_test.max(), y_pred.max())
plt.plot([lim_min, lim_max], [lim_min, lim_max], "r--", linewidth=2, label="y = x")

# Barra de cores para interpretar os resÃ­duos
cbar = plt.colorbar(sc)
cbar.set_label("ResÃ­duo (y_real - y_pred)")

plt.legend()
plt.tight_layout()
plt.show()