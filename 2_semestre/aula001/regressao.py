# regressao_linear_simples.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 1) Carregar dataset
data = fetch_california_housing(as_frame=True)
df = data.frame.copy()

# 2) Definir alvo e variÃ¡vel explicativa (RegressÃ£o Linear Simples)
TARGET = "MedHouseVal"
FEATURE = "MedInc"   # renda mediana

X = df[[FEATURE]]          # matriz 2D com 1 coluna
y = df[TARGET]

# 3) Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4) Ajustar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# 5) Prever e avaliar
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"RegressÃ£o Linear Simples ({FEATURE} -> {TARGET})")
print(f"Coeficiente (beta1) = {model.coef_[0]:.6f}")
print(f"Intercepto (beta0)  = {model.intercept_:.6f}")
print(f"RÂ²                  = {r2:.4f}")
print(f"RMSE                = {rmse:.4f}")

# 6) Plot 1: DispersÃ£o X vs Y com reta de regressÃ£o
plt.figure(figsize=(7,5))
plt.scatter(X_test, y_test, alpha=0.5, edgecolors="k", s=40, label="Dados (teste)")
# reta de regressÃ£o no espaÃ§o X vs Y
x_line = np.linspace(X_test.min().item(), X_test.max().item(), 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, "r--", linewidth=2, label="Reta ajustada")
plt.xlabel(FEATURE)
plt.ylabel(TARGET)
plt.title(f"{TARGET} vs {FEATURE} (reta de regressÃ£o)")
plt.legend()
plt.tight_layout()
plt.show()

# 7) Plot 2: Real vs Previsto com linha y=x
plt.figure(figsize=(7,5))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolors="k", s=50, label="ObservaÃ§Ãµes")
lim_min = min(y_test.min(), y_pred.min())
lim_max = max(y_test.max(), y_pred.max())
plt.plot([lim_min, lim_max], [lim_min, lim_max], "r--", linewidth=2, label="y = x (ideal)")
plt.xlabel("Valores Reais")
plt.ylabel("PrevisÃµes")
plt.title("Real vs Previsto (RegressÃ£o Simples)")
plt.legend()
plt.tight_layout()
plt.show()