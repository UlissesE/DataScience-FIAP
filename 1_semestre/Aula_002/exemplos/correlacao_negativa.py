import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [20,18,16,15,14,12,10,9,7,5] # diminui conforme x aumenta

plt.scatter(x, y, color='red')
plt.title("Exemplo de correlação negativa")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
