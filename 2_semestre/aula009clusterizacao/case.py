import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carregando os dados
data = pd.read_csv("Mall_Customers.csv")
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

inertia = []
K = range(1, 10)
for k in K:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertia.append(model.inertia_)

plt.plot(K, inertia, 'bo-')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inércia')
plt.title('Método do Cotovelo')
plt.show()

# Padronizando
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicando K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualização

plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'],
 c=data['Cluster'], cmap='Accent')
plt.xlabel('Renda Anual (k$)')
plt.ylabel('Score de Gastos')
plt.title('Segmentação de Clientes com K-Means')
plt.show()
