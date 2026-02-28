import matplotlib.pyplot as plt

tempo_site = [5,10,15,20,25,30,35,40,45,50,120]
valor_compra = [50,80,100,120,150,160,180,200,210,220,30]

plt.scatter(tempo_site, valor_compra, color='green')
plt.title("Correlacao")
plt.xlabel("Tempo no site")
plt.ylabel("Valor da compra (R$)")
plt.show()

# Existe relação positiva ou negativa entre tempo no site e valor da compra?
# Existe uma correlação positiva, com uma exceção de um outlier no final dos dados.

# Há outlier que destoa do padrão?
# Sim.

# Discutir como o outlier pode afetar a interpretação da correlação.
# Um outlier pode significar um limite na correlação entre os valores, podendo indicar uma mudança repentina
# nos valores dos dados a partir daquele ponto.