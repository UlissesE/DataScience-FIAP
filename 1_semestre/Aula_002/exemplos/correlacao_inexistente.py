import random
import matplotlib.pyplot as plt

x = list(range(1,11))
y = [random.randint(1,10) for _ in range(10)] # valores aleatórios

plt.scatter(x, y, color='green')
plt.title("Exemplo sem correlação")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()