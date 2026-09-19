from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.25, random_state=42, stratify=y
)

# Modelo
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
# Avaliação

print("Acurácia:", dt.score(X_test, y_test))
# Visualização

plt.figure(figsize=(12,8))
plot_tree(dt, filled=True, feature_names=iris.feature_names,
 class_names=iris.target_names)
plt.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Modelo
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Avaliação
print("Acurácia:", rf.score(X_test, y_test))

# Importância das variáveis
importances = rf.feature_importances_
for feat, imp in zip(iris.feature_names, importances):
 print(f"{feat}: {imp:.4f}")