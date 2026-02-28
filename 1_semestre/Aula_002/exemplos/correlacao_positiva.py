import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,8,9,11,12,14,15] # aumenta junto com x

plt.scatter(x, y, color='blue')
plt.title("Exemplo de correlação positiva")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()