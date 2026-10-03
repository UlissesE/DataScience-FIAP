from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=30000, centers=3)

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Conjunto de dados para agrupamento')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

